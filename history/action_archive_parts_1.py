"""One-time, lossless archive of the pre-cleanup generated catalogue."""
import hashlib
import json
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parent
MANIFEST=ROOT/'parts_old_1_manifest.json'


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream,'sha256').hexdigest()


def verify():
    records=json.loads(MANIFEST.read_text(encoding='utf-8'))
    records={folder:{n:sha for n,sha in files.items() if not n.lower().endswith(".zip")} for folder,files in records.items()}
    for folder,files in records.items():
        base=ROOT/folder
        actual={p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}
        assert actual==set(files),(folder,'archive file set changed')
        for name,sha in files.items():
            assert digest(base/name)==sha,(folder,name,'archive changed')
    return {folder:len(files) for folder,files in records.items()}


def main():
    if MANIFEST.exists():
        print('Archive verified:',verify());return
    moves=[('parts','parts_old_1'),('parts_source','parts_source_old_1'),
           ('navigation_oobb','navigation_oobb_old_1')]
    for source,target in moves:
        assert (ROOT/source).resolve().parent==ROOT
        assert (ROOT/target).resolve().parent==ROOT
        assert (ROOT/source).is_dir(),source
    records={}
    for source,target in moves:
        base=ROOT/source
        records[target]={p.relative_to(base).as_posix():digest(p)
                         for p in sorted(base.rglob('*')) if p.is_file()}
        # An interrupted native Move-Item may have copied part of one folder.
        # Accept existing files only when they match the still-complete source.
        for path in (ROOT/target).rglob('*'):
            if path.is_file():
                relative=path.relative_to(ROOT/target).as_posix()
                assert records[target].get(relative)==digest(path),(target,relative)
    for source,target in moves:shutil.copytree(ROOT/source,ROOT/target,dirs_exist_ok=True)
    MANIFEST.write_text(json.dumps(records,indent=2),encoding='utf-8')
    print('Archive complete and verified:',verify())


if __name__=='__main__':main()
