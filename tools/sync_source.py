"""Update a clean clone without overwriting local work."""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
def git(*args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()

if git('status', '--porcelain'):
    raise SystemExit('Commit or stash local changes before synchronization.')
branch = git('symbolic-ref', '--short', 'HEAD')
git('fetch', 'origin')
git('merge', '--ff-only', 'origin/' + branch)
print('Updated ' + branch + ' to ' + git('rev-parse', '--short', 'HEAD'))
