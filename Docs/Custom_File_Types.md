# WorldCore Custom File Types

WorldCore uses JacobS / Dev's DevF6rge-style structured file concepts as a working foundation for some planning, configuration, command, profile, and worldbuilding data. These files are plain text formats that can group information with bracketed categories and simple key/value records.

DevF6rge is treated as the current reference pattern for WorldCore structured files, not a final locked standard. WorldCore may expand the format later as systems become more defined.

This document is for documentation only. It does not create a VS Code extension, parser, or runtime behavior.

## Core File Types

| Extension | Purpose |
| --- | --- |
| `.Dev` / `.dev` / `.DEV` | DevF6rge-style structured development, config, or command file. |
| `.Master` / `.master` | Master profile or system authority file. |
| `.Slave` / `.slave` | Fictional WorldCore dependency or subordinate-system profile file. |
| `.NPC` / `.npc` | NPC or character structured data file. |
| `.Battle` / `.battle` | Battle, combat, or event system data file. |
| `.Log` / `.log` / `.LOG` | Logs, diagnostics, and runtime records. |
| `.Ships` / `.ships` | Ship, fleet, vehicle, or world-travel data file. |
| `.Dex` / `.DEX` / `.dex` | Registry or database-style data file. |
| `.Gen` / `.GEN` / `.gen` | Generated content, generated config, or template output file. |

## Planned WorldCore Aliases

| Extension | Purpose |
| --- | --- |
| `.core` | WorldCore core config. |
| `.world` | World definition. |
| `.zone` | Zone definition. |
| `.character` | Character profile. |
| `.ai` | AI behavior or profile config. |
| `.pix` | PIX bridge metadata. |
| `.template` | Reusable templates. |

## Syntax Rules

Categories use bracket syntax. Subcategories use the same bracket syntax.

Example:

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

The parser should validate structure and syntax, not naming conventions, unless application logic reserves specific names.

Extensions are case-insensitive unless a future implementation overrides that rule. Formatting and spacing may vary by parser or tool implementation.

Applications may reserve custom groups, categories, keys, or category names for their own behavior.

## PIX Rules

`PIX/Pix.dev` is local-only and must not be committed.

PIX `.dev` files with "Control Prime" or "Arctic Prime" in the filename are transfer or courier files. They are meant to be copied or moved between working areas and should normally stay out of GitHub unless JacobS / Dev specifically says they are safe to commit.

Transfer files may be deleted, recreated, or renamed if sync gets stuck.

Stable information should be moved into `README.md`, `Docs/`, or `PIX/perchance.org.md`.

Do not ignore the whole `PIX` folder. Keep tracked PIX documentation, including `PIX/perchance.org.md`, available in Git.
