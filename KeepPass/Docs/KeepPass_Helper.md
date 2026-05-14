# KeepPass Helper

## Purpose

The WorldCore KeepPass Helper is a safe Python/Tkinter GUI for KeePassXC file workflow tasks. It helps move encrypted vault files between local, backup, and bridge folders without reading vault contents.

This app is not a password manager.

## What It Can Do

- Check whether configured paths exist.
- Create timestamped backups of an encrypted vault file.
- Copy an encrypted vault file to a bridge folder.
- Pull an encrypted vault file from a bridge folder.
- Create a backup before replacing the local vault during pull.
- Open configured folders or the safe log file.
- Write safe workflow log entries.
- Check the existing WorldCore folder system.
- Open the detected WorldCore repository root.

## What It Must Never Do

- Read, parse, decrypt, or display KeePassXC vault contents.
- Ask for a vault password or master password.
- Store passwords, recovery codes, sync/share codes, API tokens, GitHub tokens, or private credentials.
- Create placeholder secrets that look real.
- Copy vault files into GitHub repo docs or public notes.

## Safety Rules

- Close KeePassXC before copying vault files.
- Back up before pulling from a bridge folder.
- Confirm before overwriting any existing file.
- Keep real secrets only inside KeePassXC.
- Keep WorldCore limited to safe code, docs, logs, templates, and workflow helpers.

## Workflow

### WorldCore System Check

The helper connects to the existing WorldCore folder system by auto-detecting the repository root from the script location. It walks upward until it finds the expected WorldCore areas:

- `Docs/`
- `Commands/`
- `PIX/`
- `KeepPass/`

Use **Check WorldCore System** to verify that these expected integration paths exist:

- `Docs/Devices`
- `Commands/Git_Commands.LOG`
- `PIX/LOG/PIX_Control_Prime.LOG`
- `KeepPass/LOG/PIX_Device.log`
- `KeepPass/Config/keepass_paths.example.json`

The result appears in the GUI System Status area and is logged safely to `KeepPass/LOG/PIX_Device.log`.

Use **Open WorldCore Root** to open the detected repository root folder.

The system check does not create secrets, inspect vault contents, or replace any existing WorldCore docs, command notes, PIX logs, or KeepPass logs.

### Check Paths

Use **Check Paths** to verify the local vault file, backup folder, bridge folder, and log parent folder.

### Backup

Use **Backup Vault** to copy the encrypted vault file into the backup folder with a timestamped filename.

### Push To Bridge

Use **Push Vault To Bridge** to copy the encrypted local vault file to the bridge folder. This does not read the vault contents.

### Pull From Bridge

Use **Pull Vault From Bridge** to copy the encrypted bridge vault file back to the local vault path. If the local vault already exists, the helper creates a backup before pulling.

## Important Warning

The helper does not decrypt, unlock, inspect, or read vault contents. It only performs safe file movement around encrypted `.kdbx` files.

Real secrets belong only inside KeePassXC.

The helper works alongside Control Prime notes, Arctic Prime notes, KeePassXC workflow docs, command logs, PIX logs, and KeepPass logs. It does not replace or overwrite those systems.

## Tkinter Troubleshooting

If running the helper prints `ModuleNotFoundError: No module named 'tkinter'`, the active Python interpreter does not include Tcl/Tk support.

On Windows, install or repair the standard Python install and enable the **Tcl/Tk and IDLE** feature. Then run the helper with that Python executable.

Do not use `python -m install tkinter`; Tkinter is part of a Python installation, not a normal package installed that way.

You can also run the included launcher from the WorldCore root:

```powershell
powershell -ExecutionPolicy Bypass -File KeepPass/App/Run_KeepPass_Helper.ps1
```

If Python is installed in a specific location, pass it explicitly:

```powershell
powershell -ExecutionPolicy Bypass -File KeepPass/App/Run_KeepPass_Helper.ps1 -PythonPath C:/Path/To/Python/python.exe
```
