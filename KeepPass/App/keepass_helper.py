"""WorldCore KeepPass Helper.

This GUI is a safe file workflow helper for encrypted KeePassXC vault files.
It never opens, parses, decrypts, or displays vault contents.
"""

from __future__ import annotations

import os
import platform
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
except ModuleNotFoundError as exc:
    if exc.name != "tkinter":
        raise
    print(
        "WorldCore KeepPass Helper requires Python with Tkinter/Tcl-Tk support.\n"
        "The current Python interpreter does not include tkinter.\n\n"
        "Fix on Windows:\n"
        "1. Install or repair the standard Python from python.org.\n"
        "2. During setup, enable the Tcl/Tk and IDLE feature.\n"
        "3. Run this app with that Python, for example:\n"
        "   C:\\Path\\To\\Python\\python.exe KeepPass\\App\\keepass_helper.py\n\n"
        "Do not use 'python -m install tkinter'; tkinter is not installed that way."
    )
    raise SystemExit(1) from exc


APP_TITLE = "WorldCore KeepPass Helper"
DEFAULT_LOG_FILE = "KeepPass/LOG/PIX_Device.log"
ROOT_SIGNS = ("Docs", "Commands", "PIX", "KeepPass")
SYSTEM_STATUS_PATHS = (
    ("Docs/Devices", Path("Docs/Devices")),
    ("Commands/Git_Commands.LOG", Path("Commands/Git_Commands.LOG")),
    ("PIX/LOG/PIX_Control_Prime.LOG", Path("PIX/LOG/PIX_Control_Prime.LOG")),
    ("KeepPass/LOG/PIX_Device.log", Path("KeepPass/LOG/PIX_Device.log")),
    ("KeepPass/Config/keepass_paths.example.json", Path("KeepPass/Config/keepass_paths.example.json")),
)


class KeepPassHelperApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title(APP_TITLE)
        self.root.minsize(860, 680)

        self.worldcore_root = self.detect_worldcore_root()

        self.local_vault_path = tk.StringVar()
        self.backup_folder = tk.StringVar()
        self.bridge_folder = tk.StringVar()
        self.log_file = tk.StringVar(value=self._default_log_file())

        self.status_text = tk.StringVar(value="Ready. This app never asks for passwords.")
        self.root_text = tk.StringVar(value=self._root_status_text())

        self._build_ui()

    def _build_ui(self) -> None:
        wrapper = ttk.Frame(self.root, padding=16)
        wrapper.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        wrapper.columnconfigure(1, weight=1)

        title = ttk.Label(wrapper, text=APP_TITLE, font=("Segoe UI", 16, "bold"))
        title.grid(row=0, column=0, columnspan=3, sticky="w")

        warning = (
            "File workflow helper only. Not a password manager. "
            "Does not read, decrypt, display, or store vault contents or passwords."
        )
        ttk.Label(wrapper, text=warning, wraplength=760).grid(
            row=1, column=0, columnspan=3, sticky="ew", pady=(4, 14)
        )

        ttk.Label(wrapper, textvariable=self.root_text, wraplength=760).grid(
            row=2, column=0, columnspan=3, sticky="ew", pady=(0, 12)
        )

        self._add_path_row(wrapper, 3, "Local vault path", self.local_vault_path, self._browse_vault)
        self._add_path_row(wrapper, 4, "Backup folder", self.backup_folder, self._browse_backup)
        self._add_path_row(wrapper, 5, "Bridge folder", self.bridge_folder, self._browse_bridge)
        self._add_path_row(wrapper, 6, "Log file", self.log_file, self._browse_log)

        buttons = ttk.Frame(wrapper)
        buttons.grid(row=7, column=0, columnspan=3, sticky="ew", pady=(16, 8))
        for index in range(3):
            buttons.columnconfigure(index, weight=1)

        button_specs = [
            ("Check Paths", self.check_paths),
            ("Check WorldCore System", self.check_worldcore_system),
            ("Backup Vault", self.backup_vault),
            ("Push Vault To Bridge", self.push_vault_to_bridge),
            ("Pull Vault From Bridge", self.pull_vault_from_bridge),
            ("Open WorldCore Root", self.open_worldcore_root),
            ("Open Local Vault Folder", lambda: self.open_path(self._parent_of(self.local_vault_path.get()))),
            ("Open Backup Folder", lambda: self.open_path(self.backup_folder.get())),
            ("Open Bridge Folder", lambda: self.open_path(self.bridge_folder.get())),
            ("Open Log File", lambda: self.open_path(self.log_file.get())),
            ("Write Test Log Entry", self.write_test_log_entry),
        ]

        for index, (text, command) in enumerate(button_specs):
            ttk.Button(buttons, text=text, command=command).grid(
                row=index // 3,
                column=index % 3,
                sticky="ew",
                padx=4,
                pady=4,
            )

        notes = (
            "Close KeePassXC before copying vault files. "
            "Use Control Prime as the primary source whenever possible. "
            "If both devices were edited, back up both vaults before merging."
        )
        ttk.Label(wrapper, text=notes, wraplength=760).grid(
            row=8, column=0, columnspan=3, sticky="ew", pady=(8, 8)
        )

        ttk.Label(wrapper, text="System Status").grid(row=9, column=0, sticky="w", pady=(4, 2))
        self.system_status = tk.Text(wrapper, height=7, wrap="word")
        self.system_status.grid(row=10, column=0, columnspan=3, sticky="nsew", pady=(0, 8))
        wrapper.rowconfigure(10, weight=1)
        self._set_system_status(
            "Click Check WorldCore System to verify Docs, Commands, PIX logs, and KeepPass logs."
        )

        status = ttk.Label(wrapper, textvariable=self.status_text, relief="sunken", anchor="w", padding=6)
        status.grid(row=11, column=0, columnspan=3, sticky="ew", pady=(8, 0))

    def _add_path_row(
        self,
        parent: ttk.Frame,
        row: int,
        label: str,
        variable: tk.StringVar,
        browse_command,
    ) -> None:
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", pady=4)
        ttk.Entry(parent, textvariable=variable).grid(row=row, column=1, sticky="ew", padx=8, pady=4)
        ttk.Button(parent, text="Browse", command=browse_command).grid(row=row, column=2, sticky="ew", pady=4)

    def _browse_vault(self) -> None:
        path = filedialog.askopenfilename(
            title="Select encrypted KeePassXC vault file",
            filetypes=[("KeePassXC vault files", "*.kdbx"), ("All files", "*.*")],
        )
        if path:
            self.local_vault_path.set(path)

    def _browse_backup(self) -> None:
        self._browse_folder(self.backup_folder)

    def _browse_bridge(self) -> None:
        self._browse_folder(self.bridge_folder)

    def _browse_folder(self, variable: tk.StringVar) -> None:
        path = filedialog.askdirectory()
        if path:
            variable.set(path)

    def _browse_log(self) -> None:
        path = filedialog.asksaveasfilename(
            title="Select safe log file",
            defaultextension=".log",
            filetypes=[("Log files", "*.log"), ("All files", "*.*")],
        )
        if path:
            self.log_file.set(path)

    def check_paths(self) -> None:
        vault = Path(self.local_vault_path.get())
        backup = Path(self.backup_folder.get())
        bridge = Path(self.bridge_folder.get())
        log_file = self._resolve_path(self.log_file.get())

        results = [
            f"Local vault exists: {vault.is_file()}",
            f"Backup folder exists: {backup.is_dir()}",
            f"Bridge folder exists: {bridge.is_dir()}",
            f"Log parent exists: {log_file.parent.is_dir()}",
        ]
        message = "\n".join(results)
        self.log_action("path check result", message)
        self.status_text.set("Path check complete.")
        messagebox.showinfo("Path Check", message)

    def check_worldcore_system(self) -> None:
        if self.worldcore_root is None:
            message = (
                "WorldCore root was not auto-detected. "
                "Path fields can still be edited manually."
            )
            self._set_system_status(message)
            self.status_text.set("WorldCore root not detected.")
            messagebox.showerror("WorldCore Root Missing", message)
            return

        lines = [f"WorldCore root: {self.worldcore_root}", ""]
        missing: list[str] = []

        for label, relative_path in SYSTEM_STATUS_PATHS:
            exists = (self.worldcore_root / relative_path).exists()
            state = "OK" if exists else "MISSING"
            lines.append(f"{state}: {label}")
            if not exists:
                missing.append(label)

        message = "\n".join(lines)
        self._set_system_status(message)

        detail = "missing: none" if not missing else f"missing: {', '.join(missing)}"
        self.log_action("worldcore system check", detail, use_default_log=True)

        self.status_text.set("WorldCore system check complete.")
        if missing:
            messagebox.showwarning("WorldCore System Check", message)
        else:
            messagebox.showinfo("WorldCore System Check", message)

    def backup_vault(self) -> Path | None:
        vault = self._validated_vault_path()
        if vault is None:
            return None

        backup_dir = self._validated_folder(self.backup_folder.get(), "Backup folder")
        if backup_dir is None:
            return None

        backup_path = self._timestamped_backup_path(vault, backup_dir)
        try:
            shutil.copy2(vault, backup_path)
        except OSError as exc:
            self._show_error("Backup failed", exc)
            return None

        self.log_action("backup created", f"{vault.name} -> {backup_path.name}")
        self.status_text.set(f"Backup created: {backup_path.name}")
        messagebox.showinfo("Backup Created", f"Backup created:\n{backup_path}")
        return backup_path

    def push_vault_to_bridge(self) -> None:
        vault = self._validated_vault_path()
        if vault is None:
            return

        bridge_dir = self._validated_folder(self.bridge_folder.get(), "Bridge folder")
        if bridge_dir is None:
            return

        target = bridge_dir / vault.name
        if not self._confirm_overwrite(target):
            return

        try:
            shutil.copy2(vault, target)
        except OSError as exc:
            self._show_error("Push failed", exc)
            return

        self.log_action("push copied file", f"{vault.name} -> bridge")
        self.status_text.set(f"Pushed vault to bridge: {target.name}")
        messagebox.showinfo("Push Complete", f"Copied encrypted vault file to bridge:\n{target}")

    def pull_vault_from_bridge(self) -> None:
        local_vault = self._validated_vault_path(allow_missing=True)
        if local_vault is None:
            return

        bridge_dir = self._validated_folder(self.bridge_folder.get(), "Bridge folder")
        if bridge_dir is None:
            return

        source = bridge_dir / local_vault.name
        if not source.is_file():
            messagebox.showerror("Missing Bridge Vault", f"Bridge vault was not found:\n{source}")
            self.log_action("error", "pull failed: bridge vault missing")
            return

        if local_vault.exists():
            backup = self.backup_vault()
            if backup is None:
                messagebox.showerror("Pull Stopped", "Local backup failed. Pull was stopped.")
                return

        if not self._confirm_overwrite(local_vault):
            return

        try:
            local_vault.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, local_vault)
        except OSError as exc:
            self._show_error("Pull failed", exc)
            return

        self.log_action("pull copied file", "bridge -> local vault path")
        self.status_text.set(f"Pulled vault from bridge: {local_vault.name}")
        messagebox.showinfo("Pull Complete", f"Copied encrypted vault file from bridge:\n{source}")

    def write_test_log_entry(self) -> None:
        self.log_action("test log entry", "safe test entry")
        self.status_text.set("Test log entry written.")
        messagebox.showinfo("Log Entry Written", "Safe test log entry written.")

    def open_worldcore_root(self) -> None:
        if self.worldcore_root is None:
            messagebox.showerror(
                "WorldCore Root Missing",
                "WorldCore root was not auto-detected. Path fields can still be edited manually.",
            )
            return
        self.open_path(str(self.worldcore_root))

    def open_path(self, path_text: str) -> None:
        if not path_text:
            messagebox.showerror("Missing Path", "No path is set.")
            return

        path = self._resolve_path(path_text)
        if not path.exists():
            messagebox.showerror("Missing Path", f"Path does not exist:\n{path}")
            return

        try:
            if platform.system() == "Windows":
                os.startfile(path)  # type: ignore[attr-defined]
            elif platform.system() == "Darwin":
                subprocess.run(["open", str(path)], check=False)
            else:
                subprocess.run(["xdg-open", str(path)], check=False)
        except OSError as exc:
            self._show_error("Open failed", exc)
            return

        self.log_action("opened path", path.name or "worldcore root")

    def log_action(self, action: str, detail: str, use_default_log: bool = False) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        safe_detail = detail.replace("\n", " | ")
        line = f"{timestamp} | {action} | {safe_detail}\n"
        log_file = self._resolve_path(DEFAULT_LOG_FILE if use_default_log else self.log_file.get() or DEFAULT_LOG_FILE)
        try:
            log_file.parent.mkdir(parents=True, exist_ok=True)
            with log_file.open("a", encoding="utf-8") as handle:
                handle.write(line)
        except OSError as exc:
            messagebox.showerror("Log Error", f"Could not write safe log entry:\n{exc}")

    def _validated_vault_path(self, allow_missing: bool = False) -> Path | None:
        path_text = self.local_vault_path.get().strip()
        if not path_text:
            messagebox.showerror("Missing Local Vault Path", "Set a local encrypted vault path first.")
            return None

        path = Path(path_text)
        if path.suffix.lower() != ".kdbx":
            if not messagebox.askyesno(
                "Confirm File Type",
                "The selected file does not end in .kdbx. Continue with file copy only?",
            ):
                return None

        if not allow_missing and not path.is_file():
            messagebox.showerror("Missing Vault File", f"Local vault file was not found:\n{path}")
            self.log_action("error", "local vault missing")
            return None

        return path

    def _validated_folder(self, path_text: str, label: str) -> Path | None:
        if not path_text.strip():
            messagebox.showerror(f"Missing {label}", f"Set the {label.lower()} first.")
            return None

        path = Path(path_text)
        if not path.is_dir():
            if not messagebox.askyesno(label, f"{label} does not exist:\n{path}\n\nCreate it?"):
                return None
            try:
                path.mkdir(parents=True, exist_ok=True)
            except OSError as exc:
                self._show_error(f"Could not create {label.lower()}", exc)
                return None

        return path

    def _timestamped_backup_path(self, vault: Path, backup_dir: Path) -> Path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return backup_dir / f"{vault.stem}_{timestamp}{vault.suffix}"

    def _confirm_overwrite(self, target: Path) -> bool:
        if not target.exists():
            return True
        return messagebox.askyesno("Confirm Overwrite", f"This file already exists:\n{target}\n\nOverwrite it?")

    def _show_error(self, title: str, exc: OSError) -> None:
        self.log_action("error", title)
        self.status_text.set(title)
        messagebox.showerror(title, str(exc))

    @staticmethod
    def _parent_of(path_text: str) -> str:
        return str(Path(path_text).parent) if path_text else ""

    @staticmethod
    def detect_worldcore_root() -> Path | None:
        start = Path(__file__).resolve()
        for candidate in (start.parent, *start.parents):
            if all((candidate / sign).exists() for sign in ROOT_SIGNS):
                return candidate
        return None

    def _default_log_file(self) -> str:
        if self.worldcore_root is not None:
            return str(self.worldcore_root / DEFAULT_LOG_FILE)
        return DEFAULT_LOG_FILE

    def _root_status_text(self) -> str:
        if self.worldcore_root is None:
            return "WorldCore root: not detected. Manual paths can still be edited."
        return f"WorldCore root: {self.worldcore_root}"

    def _resolve_path(self, path_text: str) -> Path:
        path = Path(path_text)
        if path.is_absolute() or self.worldcore_root is None:
            return path
        return self.worldcore_root / path

    def _set_system_status(self, text: str) -> None:
        self.system_status.configure(state="normal")
        self.system_status.delete("1.0", "end")
        self.system_status.insert("1.0", text)
        self.system_status.configure(state="disabled")


def main() -> None:
    root = tk.Tk()
    app = KeepPassHelperApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
