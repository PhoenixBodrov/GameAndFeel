# Game and Feel

Shared modpack files, bug fixes, development history and downloadable snapshots for Phoenix and kokkas56.

[Board](https://github.com/users/PhoenixBodrov/projects/1) · [Bugs and ideas](https://github.com/PhoenixBodrov/GameAndFeel/issues/new/choose) · [Downloads](https://github.com/PhoenixBodrov/GameAndFeel/releases)

## Minecraft

The folder names mirror the supplied Minecraft directory.

| Folder | Game and loader | Purpose |
| --- | --- | --- |
| Minecraft/Minecraft AI | 1.20.1 Forge 47.4.10 | Existing pack source |
| Minecraft/SteamPunk | 1.20.1 Forge 47.4.10 | Downloadable existing snapshot |
| Minecraft/Steampunk 1.1 | 1.20.1 Forge 47.4.10 | Downloadable existing snapshot |
| Minecraft/Mine Kokka | 1.21.1 NeoForge 21.1.233 | Existing NeoForge pack source |
| Minecraft/Mine Kokka compatability modpack | 1.21.1 NeoForge 21.1.250 | Separate bug and compatibility test pack |
| CSGO | Awaiting files | CS:GO modpack |

Development currently focuses on Minecraft 1.20.1. The exact active folder has not been confirmed. The test pack stays separate from the full NeoForge pack. Updated 1.21.1 files can be committed when supplied.

Configs, scripts, quests and custom pack data are tracked. Binary dependency inventories record exact checksums. Downloadable archives contain installed mods and resources, without launcher accounts, worlds, logs or generated caches. Snapshots are user supplied and have not been launch tested by this setup process.

## Branches and history

main holds shared changes. Starter work branches are codex/minecraft1201, codex/neoforge1211, codex/neoforgeTests and codex/csgo. Use focused branches and pull requests for fixes. A branch contains the complete repository; edit the intended pack folder.

Each pack has independent release tags and downloads. See [Releases and rollback](docs/Releases%20and%20rollback.md). Do not move published tags.

## Team workflow

Use features & bugs for ideas and reports, in progress Kokk or in progress Rein while developing, To test when a change needs verification, and Completed after verification. Attach logs to bug reports when available. Drag a log file into the issue editor; logs are optional and must not contain passwords or access tokens.

See [Synchronization](docs/Synchronization.md), [Collaboration](CONTRIBUTING.md) and [Testing](docs/Testing.md). Git detects file conflicts; gameplay and mod compatibility still require game tests.
