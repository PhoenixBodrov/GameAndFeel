# Game and Feel

Shared modpack files, bug fixes, development history and downloadable snapshots for Phoenix and kokkas56.

[Board](https://github.com/users/PhoenixBodrov/projects/1) · [Bugs and ideas](https://github.com/PhoenixBodrov/GameAndFeel/issues/new/choose) · [Downloads](https://github.com/PhoenixBodrov/GameAndFeel/releases)

## Minecraft

The folder names mirror the supplied Minecraft directory.

| Folder | Game and loader | Purpose |
| --- | --- | --- |
| Minecraft/Minecraft AI | 1.20.1 Forge 47.4.10 | Experimental development pack |
| Minecraft/SteamPunk | 1.20.1 Forge 47.4.10 | Current stable pack used for play and development |
| Minecraft/Steampunk 1.1 | 1.20.1 Forge 47.4.10 | Older development pack, may be retired |
| Minecraft/Mine Kokka | 1.21.1 NeoForge 21.1.233 | Newest main development pack |
| Minecraft/Mine Kokka compatability modpack | 1.21.1 NeoForge 21.1.250 | Separate bug and compatibility test pack |
| CSGO | Awaiting files | CS:GO modpack |

SteamPunk is the current stable pack, with a planned move to Mine Kokka. Mine Kokka is the newest development pack. Steampunk 1.1 is older work that may be retired. Minecraft AI is for experimental development. The compatibility pack stays separate for testing new mods. The supplied Steampunk 1.1 metadata identifies Forge 1.20.1, despite its description as previous 1.21; retain the recorded version until replacement files confirm otherwise.

Configs, scripts, quests and custom pack data are tracked. Binary dependency inventories record exact checksums. Downloadable archives contain installed mods and resources, without launcher accounts, worlds, logs or generated caches. Snapshots are user supplied and have not been launch tested by this setup process.

## Branches and history

main holds shared changes. Starter work branches are codex/minecraft1201, codex/neoforge1211, codex/neoforgeTests and codex/csgo. Use focused branches and pull requests for fixes. A branch contains the complete repository; edit the intended pack folder.

Each pack has independent release tags and downloads. See [Releases and rollback](docs/Releases%20and%20rollback.md). Do not move published tags.

## Team workflow

Use features & bugs for ideas and reports, in progress Kokk or in progress Rein while developing, To test when a change needs verification, and Completed after verification. Attach logs to bug reports when available. Drag a log file into the issue editor; logs are optional and must not contain passwords or access tokens.

See [Synchronization](docs/Synchronization.md), [Collaboration](CONTRIBUTING.md) and [Testing](docs/Testing.md). Git detects file conflicts; gameplay and mod compatibility still require game tests.
