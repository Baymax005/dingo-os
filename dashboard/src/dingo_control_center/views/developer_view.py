"""
Developer View - Development tools management
"""

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw
import subprocess
import shutil


class DeveloperView(Gtk.Box):
    """Developer tools view"""

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_margin_top(24)
        self.set_margin_bottom(24)
        self.set_margin_start(24)
        self.set_margin_end(24)

        # Header
        header = Gtk.Label(label="🛠️ Developer Tools")
        header.add_css_class("title-1")
        self.append(header)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Installed Languages
        lang_label = Gtk.Label(label="Installed Languages")
        lang_label.add_css_class("title-3")
        lang_label.set_halign(Gtk.Align.START)
        self.append(lang_label)

        lang_list = self.create_language_list()
        self.append(lang_list)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Development Tools
        tools_label = Gtk.Label(label="Development Tools")
        tools_label.add_css_class("title-3")
        tools_label.set_halign(Gtk.Align.START)
        self.append(tools_label)

        tools_list = self.create_tools_list()
        self.append(tools_list)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Quick Actions
        actions_label = Gtk.Label(label="Quick Actions")
        actions_label.add_css_class("title-3")
        actions_label.set_halign(Gtk.Align.START)
        self.append(actions_label)

        actions = self.create_dev_actions()
        self.append(actions)

    def create_language_list(self):
        """Create list of installed languages"""
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        box.set_margin_top(12)

        languages = [
            ("Python", "python3", "--version"),
            ("Node.js", "node", "--version"),
            ("Go", "go", "version"),
            ("Rust", "rustc", "--version"),
            ("Java", "java", "--version"),
        ]

        for name, cmd, arg in languages:
            row = self.create_language_row(name, cmd, arg)
            box.append(row)

        return box

    def create_language_row(self, name, cmd, arg):
        """Create a language row"""
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        row.add_css_class("card")
        row.set_margin_top(4)
        row.set_margin_bottom(4)

        # Name
        name_label = Gtk.Label(label=name)
        name_label.set_width_chars(15)
        name_label.set_halign(Gtk.Align.START)
        row.append(name_label)

        # Version
        version = self.get_version(cmd, arg)
        version_label = Gtk.Label(label=version)
        version_label.add_css_class("dim-label")
        version_label.set_halign(Gtk.Align.START)
        version_label.set_hexpand(True)
        row.append(version_label)

        # Status
        status = "✓ Installed" if version != "Not installed" else "✗ Not found"
        status_label = Gtk.Label(label=status)
        if version != "Not installed":
            status_label.add_css_class("success")
        row.append(status_label)

        return row

    def create_tools_list(self):
        """Create list of development tools"""
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        box.set_margin_top(12)

        tools = [
            ("Git", "git"),
            ("Docker", "docker"),
            ("VS Code", "code"),
            ("Neovim", "nvim"),
        ]

        for name, cmd in tools:
            row = self.create_tool_row(name, cmd)
            box.append(row)

        return box

    def create_tool_row(self, name, cmd):
        """Create a tool row"""
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        row.add_css_class("card")
        row.set_margin_top(4)
        row.set_margin_bottom(4)

        name_label = Gtk.Label(label=name)
        name_label.set_width_chars(15)
        name_label.set_halign(Gtk.Align.START)
        row.append(name_label)

        installed = shutil.which(cmd) is not None
        status = "✓ Installed" if installed else "✗ Not found"
        status_label = Gtk.Label(label=status)
        if installed:
            status_label.add_css_class("success")
        status_label.set_hexpand(True)
        status_label.set_halign(Gtk.Align.START)
        row.append(status_label)

        if installed:
            launch_btn = Gtk.Button(label="Launch")
            launch_btn.add_css_class("pill")
            row.append(launch_btn)

        return row

    def create_dev_actions(self):
        """Create development actions"""
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        box.set_margin_top(12)

        actions = [
            "Open Terminal",
            "Open VS Code",
            "Start Docker",
            "Database Manager",
        ]

        for action in actions:
            btn = Gtk.Button(label=action)
            btn.add_css_class("pill")
            box.append(btn)

        return box

    def get_version(self, cmd, arg):
        """Get version of a command"""
        try:
            result = subprocess.run(
                [cmd, arg],
                capture_output=True,
                text=True,
                timeout=2
            )
            output = result.stdout + result.stderr
            # Extract version number
            lines = output.split('\n')
            if lines:
                return lines[0][:50]  # Truncate long output
            return "Installed"
        except:
            return "Not installed"
