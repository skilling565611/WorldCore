# KeepPass Area

This folder stores safe code, scripts, logs, templates, and documentation for the KeePassXC workflow.

## Purpose

The KeepPass area is used for:

- KeePassXC workflow helper scripts
- Backup/transfer scripts
- Cloud bridge helper scripts
- Safe setup notes
- Safe logs
- Templates for device/account organization

## Security Rule

This folder must never contain real secrets.

Do not store:

- KeePassXC `.kdbx` vault files
- Key files
- Master passwords
- Sync/share codes
- Recovery codes
- 2FA backup codes
- API tokens
- GitHub tokens
- Microsoft/Google passwords
- Private credential files

Real secrets belong only inside KeePassXC.

## File Safety Rule

Do not delete, rename, move, merge, overwrite, or clean up existing indie/individual workflow files without explicit permission. If a file looks outdated, duplicated, messy, or unused, report it first and leave it in place.

## Current Device Roles

- Control Prime: primary KeePassXC vault source
- Arctic Prime: secondary/synced device
- Ford Link `D:`: backup/transfer drive
- `Z:` drive: Control Prime vault storage location

## Sync Style

Offline-first with manual/network merge sync.

If network/IP sync is unreliable, use manual merge or a cloud bridge transfer workflow.

## Helper GUI

The WorldCore KeepPass Helper GUI lives at:

```text
KeepPass/App/keepass_helper.py
```

Launcher:

```text
KeepPass/App/Run_KeepPass_Helper.ps1
```

It is a safe file workflow helper for encrypted KeePassXC vault backups and transfers. It is not a password manager and does not read, decrypt, display, store, or log passwords.

See:

```text
KeepPass/Docs/KeepPass_Helper.md
```
