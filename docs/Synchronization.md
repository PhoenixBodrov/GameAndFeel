# Synchronization

## Both developers

Accept the repository invitation and clone https://github.com/PhoenixBodrov/GameAndFeel in GitHub Desktop on each computer. Before work, fetch and pull the selected branch. Commit changes, push, then use pull requests to combine the work. The other computer receives them with Fetch and Pull. Each person keeps a separate clone; Git does not silently overwrite local edits.

Run tools/sync_source.py from the clone to fetch and update the current branch only when the working tree is clean. It stops on conflicts or divergent history.

## Playable snapshots

Use the same release tag on both computers. Download its archive and install the exact game and loader specified in dependencies.json. Extract into a new profile folder. Use tools/stage_pack.py to verify the archive and create a fresh installation folder without overwriting an existing installation. Personal saves and accounts are not synchronized.

Source updates include configs and scripts. Mod changes additionally require matching dependency files from the selected release. A Git pull alone does not download release archives or install a loader.

## Server updates

A client archive is not a verified server pack. First identify server compatible mods and create a separate tested server export. The server address, operating system, installation path and stop/start method have not been supplied, so live deployment is not configured.

For each tested server release: stop the server, back up the world and current installation, stage the new server export in a separate folder, copy only the intended world and server specific settings, run compatibility tests, then switch the service to that folder. Keep the previous installation and backup for rollback. Never replace an active server directory with a client snapshot.

The staging tool is suitable for a verified server export too, but it does not stop services, move worlds or deploy remotely.
