"""One-off version split, retained in the release snapshot for provenance."""
from pathlib import Path
import hashlib
import json
import shutil
import yaml

root = Path(__file__).resolve().parent
release = root / 'releases' / 'ai_version_1_2026_10_19'
release.mkdir(parents=True, exist_ok=False)
sources = ['working_oomp_populate.py', 'working_scad.py', 'working_scad_container_cutout.py',
           'working_oomp.py', 'scad_help.py', 'AI_VERSION_1.md', 'AGENTS.md',
           'action_validate_ai_version_1.py']
for name in sources:
    shutil.copy2(root / name, release / name)
manifest = {'date': '2026-10-19', 'parts': {}}
for path in sorted((root / 'parts').glob('*/working.yaml')):
    part = yaml.safe_load(path.read_text(encoding='utf-8'))
    if part.get('style') != 'ai_version_1':
        continue
    folder = release / 'parts' / path.parent.name
    folder.mkdir(parents=True)
    for name in ['working.yaml', 'thing.yaml', '3dpr.scad', '3dpr.stl', 'validation.json']:
        if (path.parent / name).exists():
            shutil.copy2(path.parent / name, folder / name)
    manifest['parts'][path.parent.name] = {
        'scad_sha256': hashlib.sha256((folder / '3dpr.scad').read_text().encode()).hexdigest(),
        'oobb_details': part['oobb_details'],
    }
assert len(manifest['parts']) == 14
(release / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')

path = root / 'working_oomp_populate.py'
text = path.read_text()
start = text.index('    if True:')
end = text.index('    #load from working_manual.yaml')
block = text[start:end].rstrip()
options = 'def get_ai_version_1_options():\n    # Frozen release options, including the unchanged basic reference models.\n    options = []\n' + block + '\n    return options\n\n\n'
options2 = options.replace('ai_version_1', 'ai_version_2').replace('Frozen release options, including the unchanged basic reference models.', 'Development options: independent copy of the version 1 release.').replace('["basic","ai_version_2"]', '["ai_version_2"]')
text = text[:start] + '    options = get_ai_version_1_options() + get_ai_version_2_options()\n\n' + text[end:]
insert = text.index('def get_ai_version_1_defaults():')
text = text[:insert] + options + options2 + text[insert:]
start = text.index('def get_ai_version_1_defaults():')
end = text.index('# Call main automatically')
defaults2 = text[start:end].replace('ai_version_1', 'ai_version_2')
text = text[:end] + defaults2 + text[end:]
path.write_text(text)

path = root / 'working_scad.py'
text = path.read_text()
start = text.index('def get_ai_version_1(')
end = text.index('def get_basic(')
block = text[start:end].replace('ai_version_1', 'ai_version_2').replace('container = get_container_details(', 'container = get_ai_version_2_container_details(')
text = text[:end] + '# Version 2 is an independent development copy of the released version 1.\n' + block + text[end:]
# Freeze both dimension mappings independently from the basic-style helper.
start = text.index('def get_container_details(')
end = text.index('def get_container_cutout(', start)
mapping = text[start:end]
text = text[:end] + mapping.replace('get_container_details', 'get_ai_version_1_container_details') + mapping.replace('get_container_details', 'get_ai_version_2_container_details') + text[end:]
text = text.replace('container = get_container_details(', 'container = get_ai_version_1_container_details(')
path.write_text(text)

path = root / 'working_scad_container_cutout.py'
text = path.read_text()
text = text.replace('def get_container_cutout_ai_version_1(', 'def get_container_cutout_ai_legacy_straight(')
start = text.index('def get_container_cutout_ai_version_2(')
end = text.index('def get_container_cutout_version_1(', start)
block = text[start:end]
text = text[:start] + block.replace('get_container_cutout_ai_version_2', 'get_container_cutout_ai_version_1') + block + text[end:]
start = text.index('def get_base(')
end = text.index('def get_container_cutout_ai_legacy_straight(')
text = text[:start] + '''def get_base(pos, thing, **kwargs):
    if kwargs.get("style") == "ai_version_1":
        get_container_cutout_ai_version_1(pos, thing, **kwargs)
    elif kwargs.get("style") == "ai_version_2":
        get_container_cutout_ai_version_2(pos, thing, **kwargs)
    else:
        get_container_cutout_version_1(pos, thing, **kwargs)

''' + text[end:]
path.write_text(text)
shutil.copy2(__file__, release / Path(__file__).name)
print('Saved version 1 release and created independent version 2 sources')
