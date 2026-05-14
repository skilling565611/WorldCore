# KeePassXC Workflow

## Mode

Offline-first with manual or network merge sync.

## Devices

- Primary device: Control Prime.
- Secondary device: Arctic Prime.
- Backup/transfer device: Ford Link `D:`.

## Vault Location

- Primary vault location: Control Prime `Z:` drive / KeePassXC area.
- KeeShare can work when the network is available.
- Direct IP/network sync can be unreliable if Arctic Prime's IP changes.
- A cloud bridge may be used later as a transfer copy, not as the only main vault.

## Rules

- Edit Control Prime first whenever possible.
- If offline or the network is iffy, edit only one vault.
- If both devices were edited, back up both before merging.
- After a successful merge, save both vaults and create a dated backup.
- Never store passwords, vaults, recovery codes, 2FA codes, sync codes, API tokens, or private credentials in GitHub.
