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

## Current Device Roles

- Control Prime: primary KeePassXC vault source
- Arctic Prime: secondary/synced device
- Ford Link `D:`: backup/transfer drive
- `Z:` drive: Control Prime vault storage location

## Sync Style

Offline-first with manual/network merge sync.

If network/IP sync is unreliable, use manual merge or a cloud bridge transfer workflow.
