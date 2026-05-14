# VM Arguments

WorldCore uses the project term **VM Argument** for runtime and launch configuration across languages.

For Python, VM Argument means:

- Python executable
- Virtual environment path
- Working directory
- Script path
- Script arguments
- Environment variables
- Runtime mode
- Dependency/add-on sandbox

## Python Runtime

- WorldCore uses `.venv` as the Python add-on/plugin sandbox.
- Packages should be installed only while `.venv` is active.
- The KeepPass GUI should run from the WorldCore root.
- Control Prime is the main runtime target.
- Arctic Prime is secondary/support.
- The runtime should not store secrets.

## Safety

- Do not commit `.venv`.
- Do not store passwords, vault files, recovery codes, sync/share codes, API tokens, GitHub tokens, or private credentials in runtime config.
- Do not install Tkinter with pip. Tkinter must come from the Python/Tcl-Tk install.
