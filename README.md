# Game and Feel

Shared modpack development for Phoenix and Vanya. This repository keeps the files, bug fixes and history for all three packs together.

[Planning board](https://github.com/users/PhoenixBodrov/projects/1) · [Bugs and ideas](https://github.com/PhoenixBodrov/GameAndFeel/issues/new/choose) · [Saved releases](https://github.com/PhoenixBodrov/GameAndFeel/releases)

## Packs

| Pack | Folder | Development branch | Release tag example |
| --- | --- | --- | --- |
| Minecraft 1.21 NeoForge | [Minecraft/1.21 NeoForge](Minecraft/1.21%20NeoForge) | `codex/minecraft121` | `minecraft121/v0.1.0` |
| Minecraft 1.20.1 Forge | [Minecraft/1.20.1 Forge](Minecraft/1.20.1%20Forge) | `codex/minecraft1201` | `minecraft1201/v0.1.0` |
| CS:GO | [CSGO](CSGO) | `codex/csgo` | `csgo/v0.1.0` |

The folders currently contain documentation only. The working pack files must be supplied before the first playable baseline or release can be saved. No game compatibility or successful launch has been verified yet.

## Development

Choose the pack folder, create an issue, and work on a branch. Open a pull request, review the diff together, test the affected pack, then merge into `main`. Every branch is a snapshot of the whole repository; keep changes focused on the intended pack folder.

Read the [collaboration guide](CONTRIBUTING.md) and [testing guide](docs/Testing.md). GitHub checks textual merge conflicts; game behavior must also be tested in the game.

## History and rollback

Commits preserve each saved change. Release tags identify tested snapshots for each pack. Release assets provide that pack's installable export. A Minecraft release does not require a CS:GO release.

[Releases and rollback](docs/Releases%20and%20rollback.md) explains how to save a tested version, run an older release, revert a bad fix, or restore one pack folder while preserving the other packs and the history. The tags above are examples, not published releases.

## Bugs and plans

Anyone with a GitHub account can open issues or comment on existing bugs. Forms cover bugs, features, tasks and playtests and identify the affected pack. Add new evidence to a matching bug.

The Game and Feel board groups plans and progress. Maintainers add issues to it and move them through Todo, In Progress and Done. Verify fixes before closing bugs.

Track manifests, exact dependency versions, configs, scripts, quests, documentation and original assets. Keep credentials, personal launcher settings, logs, caches, saves and generated outputs outside Git. Preserve download sources and redistribution permissions for third party mods.
