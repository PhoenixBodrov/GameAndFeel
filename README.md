# Minecraft modpack

Shared development repository for Phoenix and Vanya.

The original development folder from Vanya will establish the Minecraft version, mod loader, mod list, configs, quests and scripts. Those files have not been imported yet.

## Collaboration

Each contributor works in their own local clone. Pull the latest changes before starting work. Create a branch for each task, keep the change focused, and open a pull request for the other contributor to review.

Keep main as the tested pack. Record the gameplay effect and the checks performed with each change. Test multiplayer changes on a dedicated server when available.

## AI workflow

Provide AGENTS.md as context when using GPT to work on the pack. Also provide the relevant files and installed mod versions. Review generated changes before accepting them, and record which checks were actually run.

## Pack files

Track the pack manifest, configs, scripts, quests, documentation and original assets. Keep worlds, backups, logs, caches, credentials and personal launcher settings out of Git.

The initial ignore rules exclude mod JAR files and exported archives. Adapt these rules to the supplied pack format, and record exact mod versions and download sources before making a release.
