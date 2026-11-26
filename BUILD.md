# Build the drawer catalogue

Run commands from the checkout containing `action_make_all.py`. Make-all writes there by default, even if launched from another working directory.

## Set up another machine

The tested toolchain is Python 3.12, OpenSCAD 2026.04.16 with the Manifold backend, OOBB v5, OOMP v5 and Blender 5.2. Make-all uses Blender in background mode for the studio views. Put its executable on the same PATH as OpenSCAD. The renderer can use OptiX or CPU, and needs no online service. Install OpenSCAD and put the directory containing its command-line executable on `PATH`. Use the console executable `openscad.com` on Windows. Install the Python dependencies with the same interpreter you will use to generate parts.

```powershell
python -m pip install -r requirements.txt
```

If OOBB and OOMP are already importable, proceed to the checks below. For a fresh setup, these PowerShell commands put the tested library revisions in a directory alongside this project. Run them from this project folder. Set `PYTHONPATH` in the shell where you run make-all.

```powershell
$cadLib = Join-Path (Resolve-Path ..) 'drawer-cad-libraries'
New-Item -ItemType Directory -Force $cadLib | Out-Null
git clone https://github.com/oomlout/oomlout_oobb_version_5.git "$cadLib/oobb"
git -C "$cadLib/oobb" checkout 09a1e86dac72c1bbc75666dfa249901dfc5794a1
git clone https://github.com/oomlout/oomlout_oomp_version_5.git "$cadLib/oomp"
git -C "$cadLib/oomp" checkout 276231cba29fbbbcc8dd3a45c5dc6564320be858
$env:PYTHONPATH = "$cadLib/oobb;$cadLib/oomp;$env:PYTHONPATH"
```

```powershell
blender --version
openscad.com --version
python -c "import oobb, oomp, oomp_populate_helper, manifold3d, ezdxf, trimesh"
python -m unittest discover -s tests
```

## Build and print

| Command | Output |
| --- | --- |
| `python action_make_all.py` | Three frames, both joint types, the bare array and the plywood cabinet, with meshes, laser drawings, part READMEs, studio views, assembly booklets and loose print files |
| `python action_make_all.py --part 1x1` | One frame. Substitute `2x2` or `2x7` to select another |
| `python action_make_all.py --part joiners` | Joiner kit and all three compatible frame builds used as its fit fixtures |
| `python action_make_all.py --part array-3x3` | Nine joined 2 × 7 frames, the complete colour-separated kit, assembly drawing, render and fit report |
| `python action_make_all.py --output-dir ../drawer-v8-build` | Complete independent build in the specified directory |
| `python action_make_all.py --no-stl --output-dir ../drawer-v8-cad` | Editable SCAD and laser DXFs. Use a separate directory for this source-only build |

Each output root contains `parts_source` for populated definitions, `parts` for OOMP records and manufacturing files, and `navigation_oobb` for the taxonomy view. The web app’s **Run Generation** button calls the same make-all script.

### Bambu Studio print kits

Open `working.3mf` in a part folder as a project and print each plate once. The supplied P1S 0.4 mm setup has teal faceplates and screw beams, black snap beams and clip caps, and yellow adapters and joining plates. In the **Objects** tab, change a piece's filament assignment to use another spool. Each physical copy is independently selectable and its single child part inherits the object assignment.

Make-all uses the retained OOBB P1S template in `source_file/default.3mf`. It checks the editable-object and plate bindings and slices every plate with the Bambu Studio CLI. Install Bambu Studio on the build machine. The generator looks for `bambu-studio` on PATH or the standard Windows installation. The part folder includes the plate inventory in `print-plates.json` and the slice results in `slice-validation.json`. Screws, nuts, aluminium runners, pots and plywood are listed separately for assembly.

**Frame.** Open the part folder and read `printing.txt`. Print one handed front, one handed back and each listed batch once. The BOM and mount positions are in `assembly.json`. Beam mounts use M3 × 20 countersunk screws. The kit includes separate 6 mm laser-face and 3 mm reinforced trial DXFs. Cut the complete nested 3 mm drawing once per trial face. Individual spare STLs and editable SCAD sources are in each part folder.

**Joining brackets.** The joining plates are 3 mm thick. Remove the individual adapters at the adjoining outer screw beams. Install the printed two- or four-hole bracket and reuse the M3 x 20 screws and captive nuts. Select the pitch shown for the frame and tier gap in the joiner part README.

**Plywood joint.** Build with `python action_make_all.py --part plywood-joint`. The 3 mm single-contact plate attaches one outer beam. The two-contact plate ties the outer beams of two stacked frames to the same side. Select the hole pitch for your frame and tier gap. Both plates reach the outside edge of the 12 mm plywood and take one 3.5 x 16 mm countersunk wood screw on its centreline. Drill the 2.5 mm pilot 16 mm deep. For older compact frames, replace the two outer bottom snap beams with screw beams and load the nuts before installing the joints.

The faces are 209 mm apart. The 1x1 measures 213.8 mm over its screw adapters. The 2x2 and 2x7 measure 218.2 mm over their snap caps. The upper stops extend 1 mm above the two compact frames. The 2×7 uses the plywood-layout beams and stops. The former 1×2 and 4×12 units are in the [historical catalogue](history/README.md).

## Maintain the design

| Stage | Source and responsibility |
| --- | --- |
| Populate | [working_oomp_populate.py](working_oomp_populate.py) declares the pot, grids, frame or accessory role, host compatibility and taxonomy. [v8_profile.yaml](v8_profile.yaml) holds dimensions in mm. The screw-beam profile defines the common countersink and receiver pilot. |
| OOMP | [working_oomp.py](working_oomp.py) publishes the selected canonical IDs and checks the populated records. |
| SCAD | [working_scad.py](working_scad.py) draws the solids. [working_scad_container_cutout.py](working_scad_container_cutout.py) supplies the cuts, including OOBB countersinks and nut pockets. |
| Export and check | [v8_manufacturing.py](v8_manufacturing.py) exports and packages each part. [v8_validation.py](v8_validation.py) checks the manufactured meshes, the laser contours and the actual hardware placement. |

After changing a dimension or a grid, run make-all again. Use `validation.json` in each completed part folder for its measurements. Checks cover body counts, print batches, both beam types at every receiver, laser contours, compact-frame stop profiles and the assembled joiner. The joint checks compare the guide and countersink to the standard beam adapter. The cabinet fit report covers both faces, wood pilots and pot withdrawal. These are nominal CAD results. The trial print is the check for physical tolerances before committing to a complete unit.

## Add a grid or tray family

Edit `TRAYS` in [working_oomp_populate.py](working_oomp_populate.py). A layout's key is its unique CLI selector. For another grid using the existing 100 ml pot, add a layout entry such as this inside its `layouts` dictionary:

```python
"1x3": {"grid": (1, 3), "mounts": "top_braces"},
```

For another tray size, add a family with its own stable taxonomy key. Supply the tray's display name, capacity in ml, full OOMP container ID, short name, dimensions and layouts. Use a different selector, such as `150ml-1x3`, if another family already uses the same grid. `across` is the rim width across the face opening, `height` is the working pot height and `depth` runs into the frame. All three are millimetres. The V8 geometry assumes the stepped lip and side-running support described in [v8_profile.yaml](v8_profile.yaml). A different rim profile needs its own mechanical fit check.

Choose `top_braces` for the compact layout or `four_corner_replacements` for the multi-row plywood layout. Every Systempak 209 layout uses the corner screw-beam interface. One `"featured": True` layout supplies the landing-page example.

Run `python action_make_all.py`. Population publishes the new records, the SCAD stage exports and validates the parts, and the presentation stage draws and documents each part for the size and hardware declared. The landing page groups completed builds by tray family. Use `--part SELECTOR` during development and a full build before publishing. Source-only builds skip presentation rendering.

## Rebuild the guides

Each frame's canonical `parts/<id>/` folder contains `README.md`, `presentation.jpg`, four numbered assembly images, `assembly.pdf` and `assembly.html`. The offline viewer embeds the pages from the PDF. Open the downloaded HTML in a browser. It starts on the four-step spread and supports the arrow keys, zoom, printing and full-screen viewing.

Run `python -m presentation.refresh` to rebuild the catalogue, part READMEs, PDFs and HTML using existing meshes and studio images. Add `--render` to redraw the images. Use `--part joiners` or a frame selector to refresh one manual. Both commands accept `--output-dir`. Titles, counts and mount positions come from the population and assembly records. Edit the instructions in [catalogue.py](presentation/catalogue.py), the mesh poses in [scenes.py](presentation/scenes.py), and the booklet layout in [manual.py](presentation/manual.py). The generated README and manuals will be replaced by the next full build.

The assembly booklet follows the [OOBB assembly guide](https://github.com/oomlout/oomlout_oobb_version_5/blob/main/ASSEMBLY_INSTRUCTIONS_GUIDE.md). Its two blank pages preserve the print signature. The project uses the [OOBB page viewer template](https://github.com/oomlout/oomlout_oobb_version_5/blob/main/presentation/templates/assembly_page_viewer.html).

## Packaging references and drawer labels

The 100 ml frames use the open SystemPAK 209 from OOMP packaging. Make-all picks up built parts from a sibling `oomp_packaging` checkout or the project directory specified by `OOMP_PACKAGING_ROOT`. For standalone builds it uses the mesh snapshot in `presentation/packaging/<container-id>/`. The pot and lid share millimetre coordinates with Z up. Each frame's `pot-fit.json` checks the installed open pots against the assembled frame and the opposite bank. The nominal opening is 28.5 mm high, the modelled bare pot is 27 mm high and the closed package is 29 mm high. The full renders use open pots.

To import a revised packaging part, build it in the packaging project with `python action_make_all.py --part <container-id>`. From the drawer project run `python -m presentation.sync_packaging "<packaging part folder>"`, followed by `python action_make_all.py`. The snapshot makes the drawer build independent of either checkout's drive letter. Layouts with no registered reference retain the simplified envelope illustration until a matching snapshot is imported.

Each supported frame includes stocked front and rear views, two actual-size sticker PDFs, individual PNGs in `labels/`, and `label-map.json`. Print the sheets at 100%. The small label goes on the fixed frame beside the opening. Read X left to right and Y top to bottom while facing that bank. F and R distinguish the front and rear. The larger OOMP-style label on the pot identifies its current contents.

The default screws and OOMP short codes are examples from `presentation/example_contents.json`. For another physical unit, or to reassign contents, create `label_assignments/<variant>.json` in this project. Give each physical unit a unique stable `unit`. Keep it when you change contents. Keys in `contents` address individual slots. For example:

```json
{"unit":"CAB-A","contents":{"F-X1-Y1":{"id":"hardware_nut_m3","title":"M3 nut","detail":"Hex · standard","category":"Hardware","code":"3VB5B"}}}
```

Use the actual part identifier and short code for your inventory. The address QR stores the unit, face and XY coordinate. The contents QR stores the OOMP ID. Rebuild with `python -m presentation.refresh --render --part 2x7` or run make-all. Changing an assignment leaves every location sticker identical. Generic items get their new label. The stocked screw geometry is available for the demonstrated screws.


## Build the nine-unit plywood cabinet

Run `python action_make_all.py --part cabinet-3x3` to regenerate the 2×7 host and the cabinet. A full make-all includes both. The top and bottom finish flush with the 12 mm sides. The cabinet entry in `working_oomp_populate.py` defines the plywood thickness, cap projection beyond the sides (zero for flush) and fitting allowances. The canonical cabinet part folder contains the stocked and exploded model, drill patterns, cut list, labels, fit report and individual workshop files. The upper tiers use narrow inter-tier support strips. The original 2×7 kit remains usable individually.
