# WorldCore Custom File Types

WorldCore uses JacobS / Dev's DevForge v1.0.7 / DevF6rge-style structured file concepts as a working foundation for some planning, configuration, command, profile, and worldbuilding data. These files are plain text formats for readable config, profile, log, command, and data records.

DevF6rge is a custom VS Code-recognized structured file format and language package. DevForge v1.0.7 is treated as the current working reference pattern for WorldCore structured files, not a final locked standard. The DevForge README also contains personal notes and suggested file groups; those notes are useful examples, not required WorldCore parser behavior.

This document is for documentation only. It does not create a VS Code extension, parser, or runtime behavior.

## Required Rules

- Categories use bracket syntax.
- Subcategories use the same bracket syntax.
- Parsers should validate structure and syntax, not naming conventions, unless application logic reserves specific names.
- Extensions are case-insensitive unless a future implementation overrides that rule.
- Formatting and spacing may vary by parser or tool implementation.
- Applications may reserve custom groups, categories, keys, or category names for their own behavior.
- WorldCore may expand the format later as systems become more defined.

## DevForge Reference File Types

These are the current DevForge v1.0.7 recognized file types that WorldCore may use as a reference. Some file types may remain experimental, temporary, or project-specific until WorldCore systems define them more clearly.

| Extension | Purpose |
| --- | --- |
| `.Dev` / `.dev` / `.DEV` | DevF6rge-style structured development, config, or command file. |
| `.Log` / `.log` / `.LOG` | Logs, diagnostics, and runtime records. |
| `.Master` / `.master` | Master profile or system authority file. |
| `.Slave` / `.slave` | Fictional WorldCore dependency or subordinate-system profile file. |
| `.NPC` / `.npc` | NPC or character structured data file. |
| `.Battle` / `.battle` | Battle, combat, or event system data file. |
| `.Ships` / `.ships` | Ship, fleet, vehicle, or world-travel data file. |
| `.Dex` / `.DEX` / `.dex` | Registry or database-style data file. |
| `.Gen` / `.GEN` / `.gen` | Generated content, generated config, or template output file. |

DevF6rge `package.json` currently appears to include `.Dex,` with a comma in one extension string. WorldCore does not fix or modify DevF6rge from this repository; this documentation records the intended `.Dex` / `.DEX` / `.dex` forms.

## Planned WorldCore Examples

These planned WorldCore-specific aliases are examples and targets for future organization. They are not required parser behavior yet.

| Extension | Purpose |
| --- | --- |
| `.core` | WorldCore core config. |
| `.world` | World definition. |
| `.zone` | Zone definition. |
| `.character` | Character profile. |
| `.ai` | AI behavior or profile config. |
| `.pix` | PIX bridge metadata. |
| `.template` | Reusable templates. |

## Example Structure

This example shows the bracket category style WorldCore expects to use:

```text
[WorldCore]:{
    [ControlPrime]:{
        Role=Main Workstation
        Status=Active
    }
    [ArcticPrime]:{
        Role=Control Hub
        Status=Active
    }
}
```

Suggested groups, categories, and file names are examples only unless a WorldCore application reserves them.

## PIX Rules

`PIX/Pix.dev` is local-only and must not be committed.

PIX `.dev` files with "Control Prime" or "Arctic Prime" in the filename are transfer or courier files. They are meant to be copied or moved between working areas and should normally stay out of GitHub unless JacobS / Dev specifically says they are safe to commit.

Transfer files may be deleted, recreated, or renamed if sync gets stuck.

Stable information should be moved into `README.md`, `Docs/`, or `PIX/perchance.org.md`.

Do not ignore the whole `PIX` folder. Keep tracked PIX documentation, including `PIX/perchance.org.md`, available in Git.
