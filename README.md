# Minecraft modpack

Shared development repository for Phoenix and Vanya.

[Game and Feel project board](https://github.com/users/PhoenixBodrov/projects/1) brings together plans and bugs for both games. [CS:GO](https://github.com/PhoenixBodrov/CSGO) has its own repository. Both repositories are currently owned by PhoenixBodrov.

Two pack lines are planned:

| Pack | Folder |
| --- | --- |
| Minecraft 1.21 NeoForge | `Minecraft 1.21 NeoForge/` |
| Minecraft 1.20.1 Forge | `Minecraft 1.20.1 Forge/` |

Keep each pack's manifest, configs, scripts, quests and documentation in its own folder. The actual development folders have not been imported yet. Confirm their versions and layouts before adding files.

## Collaboration

Each contributor works in their own local clone. Pull the latest changes before starting work. Create a branch for each task, keep the change focused, and open a pull request for the other contributor to review.

Keep main as the tested state of both packs. Record which pack a change affects, its gameplay effect and the checks performed. Test multiplayer changes on a dedicated server when available.

## Ideas and tasks

Use [Issues](../../issues) for feature ideas, development tasks and bug reports. Choose the matching form when creating an issue. Leave future ideas open so both contributors can discuss and refine them. Turn a planned idea into concrete tasks when the scope is clear. Link the issue in the pull request that implements it, and close it after the change is verified.

## Playtesting and community reports

Anyone with a GitHub account can use [New issue](../../issues/new/choose) to submit a playtest report or a bug report while this repository is public. State which pack and version was tested. A playtest report records the commit, test environment, scenarios tried, results and related bugs. Use one bug issue per distinct problem. If an issue already describes the same problem, add your new findings in its comments so all reports stay together. Maintainers can link fixes and close an issue after verification.

Do not post full logs, world saves, player data, private network addresses or secrets. Share only the relevant excerpt after checking it for private information.

This is also the place to move useful ideas from Discord. Add the idea and its context without copying private conversations or personal information.

## AI workflow

Provide AGENTS.md as context when using GPT to work on the pack. Also provide the relevant files and installed mod versions. Review generated changes before accepting them, and record which checks were actually run.

## Pack files

Track the pack manifest, configs, scripts, quests, documentation and original assets. Keep worlds, backups, logs, caches, credentials and personal launcher settings out of Git.

The initial ignore rules exclude mod JAR files and exported archives. Adapt these rules to the supplied pack format, and record exact mod versions and download sources before making a release.
