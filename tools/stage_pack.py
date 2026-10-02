"""Validate and unpack a snapshot into a new folder. Never overwrite a profile."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

def stage(archive, target):
    target = Path(target).resolve()
    if target.exists():
        raise ValueError('Choose a new empty destination path that does not exist.')
    with zipfile.ZipFile(archive) as z:
        for item in z.infolist():
            dest = (target / item.filename).resolve()
            if not dest.is_relative_to(target) or '\\' in item.filename or ':' in item.filename:
                raise ValueError('Unsafe archive path.')
            if (item.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError('Archive links are not allowed.')
        manifest = json.loads(z.read('dependencies.json'))
        for item in manifest['files']:
            h = hashlib.sha256()
            with z.open(item['path']) as f:
                for chunk in iter(lambda: f.read(1024 * 1024), b''):
                    h.update(chunk)
            if h.hexdigest() != item['sha256']:
                raise ValueError('Checksum mismatch: ' + item['path'])
        target.mkdir(parents=True)
        z.extractall(target)
    return target

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('archive')
    p.add_argument('destination')
    args = p.parse_args()
    print('Staged at ' + str(stage(args.archive, args.destination)))
    print('Install the game and loader from dependencies.json before launching.')
