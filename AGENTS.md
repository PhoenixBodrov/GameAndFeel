# Shared Minecraft development

This project is maintained by Phoenix and Vanya.

Read the README and existing pack files before editing. Determine the Minecraft version, loader, mod versions and scripting tools from the supplied project. Ask when the project does not establish a required fact.

The Minecraft 1.21 NeoForge and Minecraft 1.20.1 Forge packs are separate pack lines. Identify the affected pack before editing. Keep its files in its own folder and do not copy configuration or scripts between pack lines without checking version compatibility.

Keep each task focused. Preserve unrelated configs, recipes, quests and assets. Do not update mods or change the loader unless the task explicitly requires it.

Verify APIs and recipe formats against the installed mod versions. Do not invent mod identifiers, item identifiers or script functions.

Do not commit credentials, personal launcher settings, worlds, backups, logs or caches. Do not redistribute third party mod binaries without checking the applicable permission.

Use a separate branch for each task. Describe the gameplay effect, changed files and validation performed when presenting changes. Never claim that Minecraft was launched or a server was tested unless it actually happened.

Use the existing pack management format. If packwiz is present, refresh its index after changing pack files.

For gameplay changes, validate the affected behavior in a test world. For changes affecting multiplayer, check the dedicated server when available. State any checks that still require a human.

Do not use dash characters in user visible prose unless required by technical syntax.
