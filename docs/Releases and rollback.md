# Releases and rollback

## Save a playable version

1. Test the pack from an exact commit on `main` and link the test report.
2. Update the pack's CHANGELOG.md with its version, fixes, known issues and save compatibility limits.
3. Create a GitHub Release with a new pack specific tag: `minecraft121/v0.1.0`, `minecraft1201/v0.1.0` or `csgo/v0.1.0`. Point it at the tested commit. Never move a published tag to different code.
4. Attach the pack's reproducible export or installer manifest with exact dependencies and installation instructions. Include only assets permitted for redistribution.
5. Verify a fresh installation from that release.

A GitHub source archive contains the whole repository and is not automatically a playable modpack. Each tag records the repository snapshot, but its release and export refer to one pack. Keep the three packs' version numbers independent. No playable release exists until actual files have been saved and tested.

## Run an older version

Choose the pack and version under Releases and install its export in a separate profile. Back up worlds and saves first. Older game or mod versions may not understand newer saves. Git history does not back up personal worlds.

## Undo a bad fix

Create a branch from current `main`, revert the bad commit through GitHub Desktop or `git revert`, test and open a pull request. Reverting preserves shared history. Avoid force pushing or resetting the shared branch.

## Restore only one pack

From a clean working tree, create a branch and restore the affected folder from an existing tested tag. Example:

```powershell
git switch -c codex/restoreMinecraft121
git restore --source=minecraft121/v0.1.0 --staged --worktree -- "Minecraft/1.21 NeoForge"
git diff --cached
```

Review, commit, test and open a pull request. This targets only the named folder. The example tag will not work until that release exists. Check shared tooling and documentation separately.
