# Synchronization

## Both developers

Accept the repository invitation and clone https://github.com/PhoenixBodrov/GameAndFeel in GitHub Desktop on each computer. Before work, fetch and pull the selected branch. Commit changes, push, then use pull requests to combine the work. The other computer receives them with Fetch and Pull. Each person keeps a separate clone; Git does not silently overwrite local edits.

Run tools/sync_source.py from the clone to fetch and update the current branch only when the working tree is clean. It stops on conflicts or divergent history.

## Playable snapshots

Use the same release tag on both computers. Download its archive and install the exact game and loader specified in dependencies.json. Extract into a new profile folder. Use tools/stage_pack.py to verify the archive and create a fresh installation folder without overwriting an existing installation. Personal saves and accounts are not synchronized.

Source updates include configs and scripts. Mod changes additionally require matching dependency files from the selected release. A Git pull alone does not download release archives or install a loader.

## Local multiplayer over Radmin VPN

The team uses local hosts over Radmin VPN and shares the world when changing hosts. Both players should use the same pack snapshot and matching game and loader versions. Radmin provides the connection; pack files and world saves are transferred separately.

Before changing hosts, the current host saves and closes the world or stops the local server. Back up the complete world folder and send a private archive to the next host. Record the pack release tag with the backup. The next host extracts it into the matching local installation and becomes the only active host of that world. Do not edit two copies and try to merge their world files.

Keep world archives outside this public repository. Git tracks pack configuration and scripts, while world backups are transferred privately. For a pack update, test a copy of the world first and retain the previous pack plus its matching world backup for rollback. Opening a world in a newer game version can make returning to an older version unsafe.

No remote deployment service is needed for the current setup. Automatic world transfer is not configured. The staging tool prepares pack files in a new folder; it does not move saves or start a local server.
