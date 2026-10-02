# Working together

Phoenix and Vanya use their own clones. GitHub is the shared history and review location. Vanya still needs a collaborator invitation once his GitHub username is supplied.

## A feature or bug fix

1. Find or create an issue, identify the pack and describe the expected result.
2. Fetch the latest changes. Start a focused branch from current `main`, such as `codex/fixMinecraft121Issue7`. The named pack branches can also collect work before review; update them from `main` first.
3. Edit the relevant pack folder. Commit small changes describing the gameplay effect.
4. Open a pull request to `main`, link the issue and record exact versions and tests. The other developer reviews it when available.
5. Resolve conflicts deliberately and retest the combined result. A clean merge does not prove mod compatibility.
6. Merge the reviewed change, verify the bug is fixed and close its issue. Publish a pack release when ready.

`main` is intended for reviewed changes. This is a convention unless branch protection is configured. There are no required automated game tests yet because the pack formats and files are unavailable.

## AI assisted work

Give GPT AGENTS.md, the affected pack files, exact dependency versions and the issue. Ask for a focused diff and test plan. Review generated changes before committing. Distinguish actual test results from suggested tests. Never claim a game was tested unless someone ran it.

## Public reports

Report one distinct bug per issue. Anyone with a GitHub account can comment with versions, reproduction steps or evidence. Maintainers manage project status and closure. Remove private information from screenshots and log excerpts.
