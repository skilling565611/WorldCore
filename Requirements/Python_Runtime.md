# Python Runtime

## Overview

- Python is installed on Control Prime.
- `pip` is installed.
- Project dependencies should go into `.venv`.
- `.venv` should not be committed.
- Deleting `.venv` removes installed project add-ons/packages.
- Tkinter must be available in the Python install used to run the GUI.
- Do not use `pip install tkinter`.
- If Tkinter is missing, repair or reinstall Python with Tcl/Tk and IDLE enabled.

## Commands

Create virtual environment:

```powershell
python -m venv .venv
```

Activate in PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Activate in CMD:

```cmd
.venv\Scripts\activate.bat
```

Check Python:

```powershell
python --version
```

Check pip:

```powershell
python -m pip --version
```

Check Tkinter:

```powershell
python -m tkinter
```

Run KeepPass Helper:

```powershell
python KeepPass/App/keepass_helper.py
```

Install normal dependencies:

```powershell
python -m pip install -r Requirements/requirements.txt
```

Install dev dependencies:

```powershell
python -m pip install -r Requirements/dev-requirements.txt
```

Save current dependencies:

```powershell
python -m pip freeze > Requirements/requirements.txt
```

Deactivate:

```powershell
deactivate
```
