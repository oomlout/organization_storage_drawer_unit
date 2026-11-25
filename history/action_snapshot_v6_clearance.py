"""Capture existing inputs/CAD before the new clearance kit; never overwrite."""
import hashlib
import json
from pathlib import Path
import yaml


def main():
    root=Path(__file__).resolve().parent
    output=root/'validation_v6_clearance'
    output.mkdir(exist_ok=True)
    path=output/'previous_models_baseline.json'
    if path.exists():
        raise FileExistsError(path)
    records={}
    for f in root.glob('parts/*ai_version_[56]_style*/working.yaml'):
        records[f.parent.name]={
            'inputs':yaml.safe_load(f.read_text())['oobb_details'],
            'scad':{s.name:hashlib.sha256(s.read_bytes()).hexdigest() for s in f.parent.glob('*.scad')},
        }
    path.write_text(json.dumps(records,indent=2))
    print('Captured',len(records),'existing models without changing them')


if __name__=='__main__':
    main()
