# V8 drawer units for Systempak 209 100 ml pots

The Windows checkout is `C:\gh\organization_storage_drawer_unit`. Make-all writes to the checkout containing its script by default. Use `--output-dir` to select another location.

Run the following command from the project folder to regenerate the complete catalogue, run the CAD fit tests and write four manufacturing kits. The build runs locally without AI or online services.

```powershell
python action_make_all.py
```

## Choose a part

The grid describes openings on **one face**. Each unit accepts a second bank of pots from the opposite face. Face dimensions are width × height. The outside faces are 209 mm apart. With caps installed, the assembly measures 218.2 mm front to back. The upper beam stops project 1 mm above the two compact frames.

| Part | Pots per unit | Face size (mm) | Snap / screw beams | Manufacturing kit |
| --- | ---: | --- | --- | --- |
| 1×1 | 2 | 108.5 × 68.5 | 2 / 2 | [1×1 ZIP](parts/oobb_organization_storage_drawer_unit_systempak_209_100_ml_1_column_1_row_v8/print_files.zip) |
| 2×2 | 8 | 197.8 × 99.8 | 6 / 3 | [2×2 ZIP](parts/oobb_organization_storage_drawer_unit_systempak_209_100_ml_2_column_2_row_v8/print_files.zip) |
| 2×7 | 28 | 197.8 × 220.3 | 17 / 4 | [2×7 ZIP](parts/oobb_organization_storage_drawer_unit_systempak_209_100_ml_2_column_7_row_v8/print_files.zip) |
| M3 joiners | — | Two-hole strip and four-hole plate | Fits 1×1 and 2×2 | [Joiner ZIP](parts/oobb_organization_storage_drawer_unit_systempak_209_100_ml_joiners_v8/print_files.zip) |

The 1×1 has one opening per face. The 2×2 and 2×7 preserve their V7 manufacturing geometry. The 2×7 uses the plywood-layout beams and face stops. The former 1×2 and 4×12 are in the [historical catalogue](history/README.md).

## Set up another machine

The tested toolchain is Python 3.12, OpenSCAD 2026.04.16 with the Manifold backend, OOBB v5 and OOMP v5. Install OpenSCAD and put the directory containing its command-line executable on `PATH`. Use the console executable `openscad.com` on Windows. Install the Python dependencies with the same interpreter you will use to generate parts.

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
openscad.com --version
python -c "import oobb, oomp, oomp_populate_helper, manifold3d, ezdxf, trimesh"
python -m unittest discover -s tests
```

## Build and print

| Command | Output |
| --- | --- |
| `python action_make_all.py` | Three frames and the joiner, with meshes, laser drawings, previews, validation and ZIPs |
| `python action_make_all.py --part 1x1` | One frame. Substitute `2x2` or `2x7` to select another |
| `python action_make_all.py --part joiners` | Joiner kit and the two compatible frame builds used as its fit fixtures |
| `python action_make_all.py --output-dir ../drawer-v8-build` | Complete independent build in the specified directory |
| `python action_make_all.py --no-stl --output-dir ../drawer-v8-cad` | Editable SCAD and laser DXFs. Use a separate directory for this source-only build |

Each output root contains `parts_source` for populated definitions, `parts` for OOMP records and manufacturing files, and `navigation_oobb` for the taxonomy view. The web app’s **Run Generation** button calls the same make-all script.

**Frame.** Unzip the kit and read `printing.txt`. Print one handed front, one handed back and each listed batch once. The BOM and mount positions are in `assembly.json`. Beam mounts use M3 × 20 countersunk screws. The kit includes separate 6 mm laser-face and 3 mm reinforced trial DXFs. Cut the complete nested 3 mm drawing once per trial face. Individual spare STLs and editable SCAD sources are in each part folder.

**Joiner.** Use two M3 × 25 countersunk screws and nuts per strip, or four per four-way junction. The kit includes 8.4 mm fronts with 0.8 mm above the installed clip caps, a looser 1.1 mm clearance option, matching extruded backers and a seven-piece trial print. Load the nuts and fit the backer from inside before closing the frame. The [clip clearance section](parts/oobb_organization_storage_drawer_unit_systempak_209_100_ml_joiners_v8/joiners_clip_clearance.png), [screw section](parts/oobb_organization_storage_drawer_unit_systempak_209_100_ml_joiners_v8/joiners_section.png), [installed view](parts/oobb_organization_storage_drawer_unit_systempak_209_100_ml_joiners_v8/joiners_in_use.png) and [fit instructions](joiner_printing.txt) show the screw path, parts and installation order.

## Maintain the design

| Stage | Source and responsibility |
| --- | --- |
| Populate | [working_oomp_populate.py](working_oomp_populate.py) declares the pot, grids, frame or accessory role, host compatibility and taxonomy. [v8_profile.yaml](v8_profile.yaml) holds dimensions in mm. Its `corner_fixing` block defines the shared hardware interface. The `joiner` block belongs to the accessory. |
| OOMP | [working_oomp.py](working_oomp.py) publishes the selected canonical IDs and checks the populated records. |
| SCAD | [working_scad.py](working_scad.py) draws the solids. [working_scad_container_cutout.py](working_scad_container_cutout.py) supplies the cuts, including OOBB countersinks and nut pockets. |
| Export and check | [v8_manufacturing.py](v8_manufacturing.py) exports and packages each part. [v8_validation.py](v8_validation.py) checks the manufactured meshes, the laser contours and the actual hardware placement. |

After changing a dimension or a grid, run make-all again. Use `validation.json` in each completed part folder for its measurements. Checks cover body counts, print batches, both beam types at every receiver, laser contours, compact-frame stop profiles and the assembled joiner. The hardware tests exercise both faces, alternate clasps, nut entry and capture, backer insertion and drawer passage. These are nominal CAD results. The trial print is the check for physical tolerances before committing to a complete unit.

The V8 migration check rebuilt the four records in an independent output directory. All 178 generated SCAD, STL and part YAML files matched byte for byte. The release passed 68 frame mesh checks, 19 laser drawings and 48 installed screw-and-nut checks. At migration the 2×2, 2×7 and original joiner meshes were also compared against the last V7 production solids. The later 8.4 mm joiner revision is tested with the production square cap at every interchangeable receiver.
