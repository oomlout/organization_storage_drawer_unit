"""Run with Blender in background mode. The scene file contains production-mesh poses in millimetres."""

import json
import sys
from pathlib import Path

import bpy
from mathutils import Matrix, Vector

job = json.loads(Path(sys.argv[sys.argv.index("--") + 1]).read_text(encoding="utf-8"))
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.engine = "CYCLES"
scene.cycles.samples = 12
scene.cycles.use_denoising = True
try:
    devices = bpy.context.preferences.addons["cycles"].preferences
    devices.compute_device_type = "OPTIX"
    devices.refresh_devices()
    gpu = [d for d in devices.devices if d.type == "OPTIX"]
    if gpu:
        for d in devices.devices:
            d.use = d in gpu
        scene.cycles.device = "GPU"
except (TypeError, RuntimeError):
    pass

scene.render.resolution_x, scene.render.resolution_y = 1100, 800
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "JPEG"
scene.render.image_settings.quality = 91
scene.world = bpy.data.worlds.new("Studio")
scene.world.use_nodes = True
scene.world.node_tree.nodes["Background"].inputs[0].default_value = (0.82, 0.85, 0.87, 1)
scene.world.node_tree.nodes["Background"].inputs[1].default_value = 0.45
scene.view_settings.view_transform = "AgX"
scene.view_settings.look = "AgX - Medium High Contrast"
colors = {
    "ply_cap": "d7ac77",
    "ply_side": "d7ac77",
    "dowel": "ba8759",
    "aluminium": "adb7bf",
    "frame": "00B1B7",
    "joint": "FEC600",
    "rail": "323b40",
    "cap": "20282b",
    "metal": "a2aab2",
    "pp": "edf7f5",
    "stock_metal": "353b3c",
    "tray": "dae4df",
    "backer": "45484d",
    "floor": "f9f7f1",
}


def material(role):
    mat = bpy.data.materials.get(role)
    if mat:
        return mat
    mat = bpy.data.materials.new(role)
    mat.use_nodes = True
    shader = mat.node_tree.nodes.get("Principled BSDF")
    if role.startswith("decal:"):
        texture = mat.node_tree.nodes.new("ShaderNodeTexImage")
        texture.image = bpy.data.images.load(role[6:], check_existing=True)
        geometry = mat.node_tree.nodes.new("ShaderNodeNewGeometry")
        paper = mat.node_tree.nodes.new("ShaderNodeMixRGB")
        paper.inputs[2].default_value = (0.95, 0.95, 0.95, 1)
        mat.node_tree.links.new(geometry.outputs["Backfacing"], paper.inputs[0])
        mat.node_tree.links.new(texture.outputs["Color"], paper.inputs[1])
        mat.node_tree.links.new(paper.outputs[0], shader.inputs["Base Color"])
        shader.inputs["Roughness"].default_value = 0.73
        return mat
    rgb = [int(colors[role][i : i + 2], 16) / 255 for i in (0, 2, 4)]
    shader.inputs["Base Color"].default_value = [
        ((v + 0.055) / 1.055) ** 2.4 if v > 0.04045 else v / 12.92 for v in rgb
    ] + [1]
    shader.inputs["Metallic"].default_value = 0.75 if role == "metal" else 0
    shader.inputs["Roughness"].default_value = 0.38 if role != "floor" else 0.85
    if role == "pp":
        shader.inputs["Transmission Weight"].default_value = 0.85
        shader.inputs["Roughness"].default_value = 0.17
        shader.inputs["IOR"].default_value = 1.49
    if role == "stock_metal":
        shader.inputs["Metallic"].default_value = 0.76
    if role == "aluminium":
        shader.inputs["Metallic"].default_value = .8
    if role.startswith("ply_"):
        # Long veneer grain on faces, alternating plies across exposed edges.
        nodes=mat.node_tree.nodes
        link=mat.node_tree.links.new
        coord=nodes.new("ShaderNodeTexCoord").outputs["Generated"]
        scale=nodes.new("ShaderNodeVectorMath");scale.operation="MULTIPLY"
        scale.inputs[1].default_value=(2,22,36) if role=="ply_cap" else (22,2,36)
        link(coord,scale.inputs[0])
        noise=nodes.new("ShaderNodeTexNoise");noise.inputs["Scale"].default_value=2.5
        link(scale.outputs[0],noise.inputs[0])
        grain=nodes.new("ShaderNodeValToRGB"); link(noise.outputs["Fac"],grain.inputs[0])
        grain.color_ramp.elements[0].color=(.43,.23,.105,1)
        grain.color_ramp.elements[1].color=(.9,.69,.42,1)
        sep=nodes.new("ShaderNodeSeparateXYZ");link(coord,sep.inputs[0])
        freq=nodes.new("ShaderNodeMath");freq.operation="MULTIPLY";freq.inputs[1].default_value=22
        link(sep.outputs["Y" if role=="ply_cap" else "X"],freq.inputs[0])
        wave=nodes.new("ShaderNodeMath");wave.operation="PINGPONG";wave.inputs[1].default_value=1
        link(freq.outputs[0],wave.inputs[0])
        layers=nodes.new("ShaderNodeValToRGB");link(wave.outputs[0],layers.inputs[0])
        layers.color_ramp.elements[0].color=(.31,.16,.07,1)
        layers.color_ramp.elements[1].color=(.84,.62,.36,1)
        normal=nodes.new("ShaderNodeSeparateXYZ");link(nodes.new("ShaderNodeNewGeometry").outputs["Normal"],normal.inputs[0])
        broad=nodes.new("ShaderNodeMath");broad.operation="ABSOLUTE";link(normal.outputs["Z" if role=="ply_cap" else "X"],broad.inputs[0])
        mix=nodes.new("ShaderNodeMixRGB");link(broad.outputs[0],mix.inputs[0]);link(layers.outputs[0],mix.inputs[1]);link(grain.outputs[0],mix.inputs[2])
        link(mix.outputs[0],shader.inputs["Base Color"])
    return mat


cache = {}
world = Matrix(((1, 0, 0, 0), (0, 0, 1, 0), (0, -1, 0, 0), (0, 0, 0, 1)))
for view in job["views"]:
    for obj in list(scene.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    stocked = Path(view["output"]).stem.startswith("stocked-")
    scene.render.resolution_x, scene.render.resolution_y = (2200, 1600) if stocked else (1100, 800)
    scene.cycles.samples = 20 if stocked else 12
    if "focus" in view:
        scene.render.resolution_x, scene.render.resolution_y = 2000, 820
    if "resolution" in view:
        scene.render.resolution_x,scene.render.resolution_y=view["resolution"]
    scene.cycles.samples = view.get("samples",scene.cycles.samples)
    scene.render.image_settings.file_format = "PNG" if Path(view["output"]).suffix.lower()==".png" else "JPEG"
    points = []
    for path, role, values in view["items"]:
        key = (path, role)
        if key not in cache:
            if role == "decal":
                bpy.ops.mesh.primitive_plane_add(size=1)
            else:
                bpy.ops.wm.stl_import(filepath=path, use_mesh_validate=False)
            obj = bpy.context.selected_objects[0]
            obj.data.materials.clear()
            obj.data.materials.append(material("decal:" + path if role == "decal" else role))
            cache[key] = obj.data
        else:
            obj = bpy.data.objects.new(role, cache[key])
            scene.collection.objects.link(obj)
        obj.matrix_world = world @ Matrix(values)
        points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)

    low = Vector([min(p[i] for p in points) for i in range(3)])
    high = Vector([max(p[i] for p in points) for i in range(3)])
    center = (low + high) / 2
    span = max(high - low)
    direction = Vector(view.get("eye", (0.85, -1.8, 0.85))).normalized()
    rotation = (-direction).to_track_quat("-Z", "Y")
    local = [rotation.inverted() @ (p - center) for p in points]
    left, right = min(p.x for p in local), max(p.x for p in local)
    bottom, top = min(p.y for p in local), max(p.y for p in local)
    aim = center + rotation @ Vector(((left + right) / 2, (top + bottom) / 2, 0))
    if "focus" in view:
        aim = Vector(view["focus"])
    bpy.ops.object.camera_add(location=aim + direction * span * 3)
    camera = bpy.context.object
    camera.rotation_euler = rotation.to_euler()
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = max(right - left, (top - bottom) * 1100 / 800) * 1.09
    if "width" in view:
        camera.data.ortho_scale = view["width"]
    camera.data.clip_end = span * 12
    scene.camera = camera
    for offset, power, size in [
        ((-0.8, -1.2, 1.9), 95, 1.5),
        ((1.3, -0.3, 0.9), 45, 1.1),
        ((0.1, 1.5, 1.3), 75, 1),
    ]:
        bpy.ops.object.light_add(type="AREA", location=center + Vector(offset) * span)
        lamp = bpy.context.object
        lamp.rotation_euler = (center - lamp.location).to_track_quat("-Z", "Y").to_euler()
        lamp.data.energy = 0.32 * power * span**2
        lamp.data.shape = "DISK"
        lamp.data.size = size * span
    bpy.ops.mesh.primitive_plane_add(size=span * 200, location=(center.x, center.y, low.z - 0.5))
    bpy.context.object.data.materials.append(material("floor"))
    scene.render.filepath = view["output"]
    bpy.ops.render.render(write_still=True)
