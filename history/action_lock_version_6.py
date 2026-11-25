"""Create once, then verify the pre-V7 release; never refresh its baseline."""
import hashlib
import json
from pathlib import Path
import shutil
import yaml
from catalogue_archive import historical_parts

ROOT = Path(__file__).resolve().parent
RELEASE = ROOT / 'releases/ai_version_6'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check():
    manifest = json.loads((RELEASE / 'manifest.json').read_text(encoding='utf-8'))
    actual = {p.name for p in (historical_parts(ROOT)).glob('*ai_version_[1-6]_style*') if p.is_dir()}
    assert actual == set(manifest['parts']), 'Pre-V7 catalogue changed'
    for name, expected in manifest['parts'].items():
        folder = historical_parts(ROOT) / name
        actual = yaml.safe_load((folder / 'working.yaml').read_text(encoding='utf-8'))['oobb_details']
        assert actual == expected['inputs'], (name, 'drawing inputs changed')
        for filename, sha in expected['files'].items():
            assert digest(folder / filename) == sha, (name, filename, 'released geometry changed')
    for filename, sha in manifest['snapshot_files'].items():
        assert digest(RELEASE / filename) == sha, ('release snapshot changed', filename)
    print(f"V6 release PASS: {len(manifest['parts'])} prior models, "
          f"{sum(len(p['files']) for p in manifest['parts'].values())} geometry files")
    return manifest


def main():
    if (RELEASE / 'manifest.json').exists():
        return check()
    assert not RELEASE.exists(), 'Incomplete release exists; inspect it before proceeding'
    RELEASE.mkdir(parents=True)
    sources = ['working.py', 'working_oomp.py', 'working_oomp_populate.py',
               'working_oomp_populate_comparison.py', 'working_scad.py',
               'working_scad_container_cutout.py', 'working_scad_tiling.py',
               'working_scad_double_sided.py', 'working_scad_v6_clearance.py',
               'scad_help.py', 'AGENTS.md', 'V6_SCREW_RAILS.md',
               'AI_VERSION_6_DOUBLE_SIDED.md', 'V6_LATCH_CLEARANCE_TESTS.md']
    for filename in sources:
        shutil.copy2(ROOT / filename, RELEASE / filename)
    parts = {}
    for folder in sorted((ROOT / 'parts').glob('*ai_version_*')):
        if not (folder / 'working.yaml').exists():
            continue
        details = yaml.safe_load((folder / 'working.yaml').read_text(encoding='utf-8'))['oobb_details']
        files = list(folder.glob('*.scad'))
        if details.get('style') == 'ai_version_6':
            files += list(folder.glob('*.stl')) + list(folder.glob('*.zip'))
            target = RELEASE / 'parts' / folder.name
            target.mkdir(parents=True)
            for path in [folder / 'working.yaml', *files, *folder.glob('*.json'), *folder.glob('*.txt')]:
                shutil.copy2(path, target / path.name)
            source = ROOT / 'parts_source' / folder.name / 'working.yaml'
            source_target = RELEASE / 'parts_source' / folder.name
            source_target.mkdir(parents=True)
            shutil.copy2(source, source_target / 'working.yaml')
        parts[folder.name] = dict(inputs=details, files={p.name: digest(p) for p in files})
    snapshot = {p.relative_to(RELEASE).as_posix(): digest(p)
                for p in RELEASE.rglob('*') if p.is_file()}
    manifest = dict(version=6, locked_on='2026-10-31', next_development_version=7,
                    description='Pre-V7 sample-37 mixed snap/screw cabinets and historical CAD',
                    parts=parts, snapshot_files=snapshot)
    (RELEASE / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    check()


if __name__ == '__main__':
    main()
