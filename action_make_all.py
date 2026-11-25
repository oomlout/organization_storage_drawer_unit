"""Build V8 source records, CAD, manufacturing kits and validation reports."""
import argparse
from working import run
from working_oomp_populate import JOINER, SIZES


def main(**kwargs):
    run(**kwargs)


def cli(default_stl=True):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--part", choices=[*SIZES, JOINER], help="Default: all four catalogue parts")
    parser.add_argument("--output-dir", help="Output root for parts_source, parts and navigation_oobb")
    parser.add_argument("--no-stl", action="store_true", help="Emit editable SCAD and laser DXFs only")
    args = parser.parse_args()
    main(part=args.part, output_dir=args.output_dir, generate_stl=default_stl and not args.no_stl)


if __name__ == "__main__":
    cli()
