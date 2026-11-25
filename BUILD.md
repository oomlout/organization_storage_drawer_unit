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
| `python action_make_all.py` | Three frames and the joiner, with meshes, laser drawings, part READMEs, studio views, assembly booklets and print ZIPs |
| `python action_make_all.py --part 1x1` | One frame. Substitute `2x2` or `2x7` to select another |
| `python action_make_all.py --part joiners` | Joiner kit and the two compatible frame builds used as its fit fixtures |
| `python action_make_all.py --output-dir ../drawer-v8-build` | Complete independent build in the specified directory |
| `python action_make_all.py --no-stl --output-dir ../drawer-v8-cad` | Editable SCAD and laser DXFs. Use a separate directory for this source-only build |

Each output root contains `parts_source` for populated definitions, `parts` for OOMP records and manufacturing files, and `navigation_oobb` for the taxonomy view. The web app’s **Run Generation** button calls the same make-all script.

**Frame.** Unzip the kit and read `printing.txt`. Print one handed front, one handed back and each listed batch once. The BOM and mount positions are in `assembly.json`. Beam mounts use M3 × 20 countersunk screws. The kit includes separate 6 mm laser-face and 3 mm reinforced trial DXFs. Cut the complete nested 3 mm drawing once per trial face. Individual spare STLs and editable SCAD sources are in each part folder.

**Joiner.** Use two M3 × 25 countersunk screws and nuts per strip, or four per four-way junction. The kit includes 8.4 mm fronts with 0.8 mm above the installed clip caps, a looser 1.1 mm clearance option, matching extruded backers and a seven-piece trial print. Load the nuts and fit the backer from inside before closing the frame. The [clip clearance section](parts/oobb_organization_storage_drawer_unit_systempak_209_100_ml_joiners_v8/joiners_clip_clearance.png), [screw section](parts/oobb_organization_storage_drawer_unit_systempak_209_100_ml_joiners_v8/joiners_section.png), [installed view](parts/oobb_organization_storage_drawer_unit_systempak_209_100_ml_joiners_v8/joiners_in_use.png) and [fit instructions](joiner_printing.txt) show the screw path, parts and installation order.

The current 100 ml frames measure 218.2 mm deep with caps installed. The upper stops extend 1 mm above the two compact frames. The 2×7 uses the plywood-layout beams and stops. The former 1×2 and 4×12 units are in the [historical catalogue](history/README.md).

## Maintain the design

| Stage | Source and responsibility |
| --- | --- |
| Populate | [working_oomp_populate.py](working_oomp_populate.py) declares the pot, grids, frame or accessory role, host compatibility and taxonomy. [v8_profile.yaml](v8_profile.yaml) holds dimensions in mm. Its `corner_fixing` block defines the shared hardware interface. The `joiner` block belongs to the accessory. |
| OOMP | [working_oomp.py](working_oomp.py) publishes the selected canonical IDs and checks the populated records. |
| SCAD | [working_scad.py](working_scad.py) draws the solids. [working_scad_container_cutout.py](working_scad_container_cutout.py) supplies the cuts, including OOBB countersinks and nut pockets. |
| Export and check | [v8_manufacturing.py](v8_manufacturing.py) exports and packages each part. [v8_validation.py](v8_validation.py) checks the manufactured meshes, the laser contours and the actual hardware placement. |

After changing a dimension or a grid, run make-all again. Use `validation.json` in each completed part folder for its measurements. Checks cover body counts, print batches, both beam types at every receiver, laser contours, compact-frame stop profiles and the assembled joiner. The hardware tests exercise both faces, alternate clasps, nut entry and capture, backer insertion and drawer passage. These are nominal CAD results. The trial print is the check for physical tolerances before committing to a complete unit.

## Add a grid or tray family

Edit `TRAYS` in [working_oomp_populate.py](working_oomp_populate.py). A layout's key is its unique CLI selector. For another grid using the existing 100 ml pot, add a layout entry such as this inside its `layouts` dictionary:

```python
"1x3": {"grid": (1, 3), "mounts": "top_braces"},
```

For another tray size, add a family with its own stable taxonomy key. Supply the tray's display name, capacity in ml, full OOMP container ID, short name, dimensions and layouts. Use a different selector, such as `150ml-1x3`, if another family already uses the same grid. `across` is the rim width across the face opening, `height` is the working pot height and `depth` runs into the frame. All three are millimetres. The V8 geometry assumes the stepped lip and side-running support described in [v8_profile.yaml](v8_profile.yaml). A different rim profile needs its own mechanical fit check.

Choose `top_braces` for the compact layout or `four_corner_replacements` for the multi-row plywood layout. Mark a layout `"joiner": True` to opt into the V8 corner hardware and its fit checks. One `"featured": True` layout supplies the landing-page example. Archived version links are maintained in the population file's `VERSIONS` table.

Run `python action_make_all.py`. Population publishes the new records, the SCAD stage exports and validates the parts, and the presentation stage draws and documents each part for the size and hardware declared. The landing page groups completed builds by tray family. Use `--part SELECTOR` during development and a full build before publishing. Source-only builds skip presentation rendering.

## Rebuild the guides

Each canonical `parts/<id>/` folder contains `README.md`, `presentation.jpg`, four numbered assembly images, `assembly.pdf` and `assembly.html`. The offline viewer embeds the pages from the PDF. Open the downloaded HTML in a browser. It starts on the four-step spread and supports the arrow keys, zoom, printing and full-screen viewing.

Run `python -m presentation.refresh` to rebuild the catalogue, part READMEs, PDFs and HTML using existing meshes and studio images. Add `--render` to redraw the images. Use `--part joiners` or a frame selector to refresh one manual. Both commands accept `--output-dir`. Titles, counts and mount positions come from the population and assembly records. Edit the instructions in [catalogue.py](presentation/catalogue.py), the mesh poses in [scenes.py](presentation/scenes.py), and the booklet layout in [manual.py](presentation/manual.py). The generated README and manuals will be replaced by the next full build.

The assembly booklet follows the [OOBB assembly guide](https://github.com/oomlout/oomlout_oobb_version_5/blob/main/ASSEMBLY_INSTRUCTIONS_GUIDE.md). Its two blank pages preserve the print signature. The project uses the [OOBB page viewer template](https://github.com/oomlout/oomlout_oobb_version_5/blob/main/presentation/templates/assembly_page_viewer.html).
