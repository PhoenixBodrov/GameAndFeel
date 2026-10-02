# Testing and compatibility

Record the pack, commit or release, game version, loader where applicable, relevant mod versions and environment in a Playtest report.

1. Confirm the files belong to the intended pack and dependencies match its game and loader.
2. Launch an isolated test profile. Record loading errors and relevant warnings.
3. Reproduce the bug, apply the fix and repeat the exact steps. Check nearby gameplay for regressions.
4. Test multiplayer changes on the intended server setup with matching client versions.
5. Retest the combined branch after resolving conflicts or merging other changes.
6. Link results to the issue and pull request. State checks still outstanding.

For Minecraft, use a disposable test world or a backed up copy. Check quests, recipes, scripts, resource loading and server startup when affected. For CS:GO, test affected maps, configs, scripts and client or server behavior.

Git detects textual merge conflicts, not mod compatibility. Pack specific automated checks can be added after the actual files and build tools are available.
