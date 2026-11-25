"""Editable comparison inputs, applied by ordinary population (never edit output YAML).

CAD mass assumes solid PLA at 1.24 g/cm3, including adhesion ears. It is not
a slicer estimate. Pot prices include 20% VAT, exclude shipping, and allocate
a single 500-piece carton; lids are purchased but are not used or weighed.
"""
import hashlib
import json
from pathlib import Path

from oomp_populate_helper import build_oomp_id

ROOT = Path(__file__).resolve().parent
FILAMENT_GBP_PER_GRAM = 0.01
PLA_DENSITY_G_PER_CM3 = 1.24

POTS = {
    "209": {
        "manufacturer": "Systempak",
        "part_number": "209",
        "capacity_ml": 100,
        "pack_quantity": 500,
        "pack_price_ex_vat_gbp": 60.95,
        "vat_rate": 0.20,
        "weight_g": 8.0,
        "price_source_url": "https://systempak.net/product/100ml-rectangular-tamper-evident-containers-and-lids/",
        "weight_source_url": "https://systempak.net/wp-content/uploads/2024/03/TDS-209-100ML.pdf",
        "checked_date": "2026-10-18",
        "availability": "On backorder",
        "price_basis": "Single carton of 500 pots and lids; lids unused; delivery excluded",
    },
    "214": {
        "manufacturer": "Systempak",
        "part_number": "214",
        "capacity_ml": 550,
        "pack_quantity": 500,
        "pack_price_ex_vat_gbp": 80.95,
        "vat_rate": 0.20,
        "weight_g": 16.0,
        "price_source_url": "https://systempak.net/product/550ml-rectangular-tamper-evident-containers-and-lids/",
        "weight_source_url": "https://systempak.net/wp-content/uploads/2024/03/TDS-214-550ML.pdf",
        "checked_date": "2026-10-18",
        "availability": "On backorder",
        "price_basis": "Single carton of 500 pots and lids; lids unused; delivery excluded",
    },
}


def geometry_fingerprint(part):
    digest = hashlib.sha256(json.dumps(part["oobb_details"], sort_keys=True).encode())
    for filename in ["working_scad.py", "working_scad_container_cutout.py", "scad_help.py"]:
        digest.update((ROOT / filename).read_bytes())
    if part["oobb_details"].get("connector_design") == "tiled_hybrid" or part.get("style") == "ai_version_6":
        digest.update((ROOT / "working_scad_tiling.py").read_bytes())
    return digest.hexdigest()


def enrich(extras):
    cache_path = ROOT / "drawer_comparison" / "cad_measurements.json"
    measurements = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    for part in extras:
        if not part.get("oobb_details"):
            continue
        code = part["container"].rsplit("_", 1)[-1]
        pot = dict(POTS[code])
        # Prefer explicit price data on a local container record when available.
        # The container record is separate from the generated frame record.
        import yaml
        for directory in [ROOT / "parts", Path("C:/gh/oomlout_oomp_version_5/parts")]:
            path = directory / part["container"] / "working.yaml"
            if path.exists():
                data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
                if data.get("price_gbp") is not None and data.get("price_includes_vat") is True:
                    pot["unit_price_gbp"] = data["price_gbp"] / data.get("price_quantity", 1)
                    pot["price_basis"] = "Existing container working.yaml; VAT-inclusive price / price_quantity"
                    pot["price_source_url"] = data.get("for_sale_url", pot["price_source_url"])
                    break
        pot.setdefault("unit_price_gbp", pot["pack_price_ex_vat_gbp"] * (1 + pot["vat_rate"]) / pot["pack_quantity"])
        role = part.get("part_role", "frame")
        count = part["column"] * part["row"] * (2 if role == "bank_layout" else part.get("drawer_sides", 1))
        component = part.get("assembly_half") in ["front", "back"]
        joint_trial = "joint_test_depth" in part
        modular_sample = part.get("style") in ["ai_version_4", "ai_version_5", "ai_version_6"] and role != "frame"
        part.update({
            "record_type": "printed_drawer_unit",
            "product_name": f"Printed {part['column']} × {part['row']} · Systempak {code} · {part['style'].replace('_', ' ')}" + (f" · {part['variant'].replace('_', ' ')}" if part.get("variant") else ""),
            "manufacturer": "oomlout",
            "drawer_count": count,
            "drawer_capacity_ml": pot["capacity_ml"],
            "drawer_capacity_basis": "manufacturer_nominal",
            "comparison_sample": role != "frame" or component or joint_trial,
            "assembly_component": component,
            "pot_quantity": 0 if component or joint_trial or modular_sample else count,
            "print_instruction": ("3dpr.scad contains both halves flat. Use front.scad and back.scad for separate plates; assembled.scad shows the assembly."
                                  if part.get("style") in ["ai_version_2", "ai_version_3"] and role == "frame" and not component
                                  else "Print outer face on bed, joint facing up." if component else ""),
            "hardware_cost_basis": "M3 screws and nuts excluded; hardware price not supplied" if part.get("style") in ["ai_version_2", "ai_version_3", "ai_version_4"] and role in ["frame", "modular_test"] else "No assembly hardware",
            "pot_cost_details": pot,
            "filament_gbp_per_gram": FILAMENT_GBP_PER_GRAM,
            "filament_density_g_per_cm3": PLA_DENSITY_G_PER_CM3,
            "filament_mass_basis": "Solid CAD volume × assumed PLA density; includes adhesion ears; excludes purge/supports",
            "price_includes_vat": True,
            "price_excludes_delivery": True,
            "availability": "Print yourself; pots on backorder at research date",
            "comparison_image": "comparison.png",
        })
        if part.get("style") == "ai_version_4":
            part["print_instruction"] = "Print one front plate with a lip and one back plate without, plus the rail batches; see assembly.json. face_plate aliases front; assembled is reference only."
        if part.get("style") == "ai_version_5" and role == "frame":
            part.update({
                "print_instruction": "Print each front/back tile and numbered rail batch once; retain the supplied P1P orientation. See assembly.json and printing.txt.",
                "filament_density_g_per_cm3": 1.27,
                "filament_mass_basis": "Solid CAD volume × assumed PETG density 1.27 g/cm3; excludes removable tile ears, supports and purge",
                "hardware_cost_basis": "M3 countersunk screws and nuts excluded; hardware price not supplied",
                "availability": "Experimental tiled PETG assembly; physical fit unverified",
            })
        if part.get("style") == "ai_version_6":
            part.update(
                print_instruction="Print one front and one identical back plate, plus every numbered rail batch once. See assembly.json and printing.txt.",
                filament_density_g_per_cm3=1.27,
                filament_mass_basis="Solid assembled CAD volume x PETG density 1.27 g/cm3; excludes supports and purge",
                hardware_cost_basis="No assembly hardware",
                availability="Experimental double sided PETG assembly; physical fit unverified",
            )
            if part.get('screw_rail_settings'):
                part['hardware_cost_basis']='Eight M3 x 20 countersunk screws and eight M3 nuts excluded; hardware prices not supplied'
        if part.get("style") in ["ai_version_5","ai_version_6"] and role == "connector_test":
            part.update({
                "product_name": f"PETG connector trial · {part['variant'].replace('_', ' ')} · version {part['style'].rsplit('_',1)[-1]}",
                "drawer_count": 0, "drawer_capacity_ml": None,
                "drawer_capacity_basis": "not_applicable_connector_test",
                "pot_cost_details": {}, "seller": "Print your own PETG coupons",
                "availability": "Unverified connector trial",
                "print_instruction": "Print the connector kit as arranged; see printing.txt. Experimental coupons, not a drawer unit.",
                "filament_density_g_per_cm3": 1.27,
                "filament_mass_basis": "Solid CAD volume × assumed PETG density 1.27 g/cm3; not a slicer measurement",
                "hardware_cost_basis": "Reference M3 screw/nut excluded" if part["connector_design"] in ["screw_reference", "connector_suite"] else "No assembly hardware",
            })
        record = measurements.get(build_oomp_id(part), {})
        if record.get("fingerprint") != geometry_fingerprint(part):
            part["comparison_measurement_status"] = "Run action_prepare_drawer_comparison.py to refresh CAD measurements"
            continue
        mass = record["volume_mm3"] / 1000 * part["filament_density_g_per_cm3"]
        filament = mass * FILAMENT_GBP_PER_GRAM
        pots = 0 if component or joint_trial or modular_sample else count * pot["unit_price_gbp"]
        total = filament + pots
        weight = (mass + (0 if component or joint_trial or modular_sample else count * pot["weight_g"])) / 1000
        part.update({
            "cad_volume_mm3": record["volume_mm3"],
            "filament_mass_g": round(mass, 3),
            "filament_cost_gbp": round(filament, 4),
            "pots_cost_gbp": round(pots, 4),
            "price_gbp": round(total, 4),
            "cost_per_drawer_gbp": round(total / count, 4),
            "weight_kg": round(weight, 6),
            "weight_basis": ("estimated_joint_fit_pair_no_pots_or_hardware" if joint_trial else
                             "estimated_modular_fit_sample_no_pots_or_hardware" if modular_sample else
                             "estimated_solid_PLA_half_including_ears_no_pots_or_hardware" if component else
                             "estimated_solid_PLA_frame_including_ears_plus_lidless_pots_excluding_hardware"),
            "cost_per_kg_gbp": round(total / weight, 4),
            "cost_per_kg_basis": "Estimated empty assembled unit including pots and adhesion ears",
            "width_mm": record["finished_envelope_mm"][0],
            "height_mm": record["finished_envelope_mm"][1],
            "depth_mm": record["finished_envelope_mm"][2],
            "comparison_measurement_status": "current",
        })
        if part.get("style") == "ai_version_6":
            part.update(weight_basis="estimated_solid_PETG_frame_plus_lidless_pots",
                        cost_per_kg_basis="Estimated PETG frame plus lidless pots")
        if part.get("style") == "ai_version_5" and role == "frame":
            part.update(weight_basis="estimated_solid_PETG_tiled_frame_plus_lidless_pots_excluding_ears_and_hardware",
                        cost_per_kg_basis="Estimated PETG frame plus lidless pots, excluding removable ears and hardware")
        if part.get("style") in ["ai_version_5","ai_version_6"] and role == "connector_test":
            part.update(cost_per_drawer_gbp=None,
                        weight_basis="estimated_solid_PETG_connector_kit_no_pots_or_hardware",
                        cost_per_kg_basis="Estimated PETG connector specimens; no pots or hardware")
