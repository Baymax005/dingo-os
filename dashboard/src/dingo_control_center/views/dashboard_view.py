"""
Dashboard View - Main overview page
"""

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw
import psutil
import subprocess


class DashboardView(Gtk.Box):
    """Main dashboard view showing system overview"""

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_margin_top(24)
        self.set_margin_bottom(24)
        self.set_margin_start(24)
        self.set_margin_end(24)

        # Welcome section
        welcome_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        
        welcome_label = Gtk.Label(label="Welcome to Dingo OS 🦘")
        welcome_label.add_css_class("title-1")
        welcome_box.append(welcome_label)

        subtitle = Gtk.Label(label="Your all-in-one development, gaming, and productivity system")
        subtitle.add_css_class("dim-label")
        welcome_box.append(subtitle)

        self.append(welcome_box)
        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Stats grid
        stats_grid = Gtk.Grid()
        stats_grid.set_column_spacing(24)
        stats_grid.set_row_spacing(24)
        stats_grid.set_column_homogeneous(True)

        # System status card
        system_card = self.create_card(
            "System Status",
            "✓ Healthy",
            "All systems operational",
            "success"
        )
        stats_grid.attach(system_card, 0, 0, 1, 1)

        # Updates card
        updates_card = self.create_card(
            "Updates",
            "5 Available",
            "Click to update system",
            "warning"
        )
        stats_grid.attach(updates_card, 1, 0, 1, 1)

        # Profile card
        profile_card = self.create_card(
            "Active Profile",
            "Developer",
            "Optimized for development",
            "info"
        )
        stats_grid.attach(profile_card, 2, 0, 1, 1)

        self.append(stats_grid)

        # System info section
        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))
        
        info_label = Gtk.Label(label="System Information")
        info_label.add_css_class("title-3")
        info_label.set_halign(Gtk.Align.START)
        self.append(info_label)

        # System info grid
        info_grid = self.create_system_info()
        self.append(info_grid)

        # Quick actions
        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))
        
        actions_label = Gtk.Label(label="Quick Actions")
        actions_label.add_css_class("title-3")
        actions_label.set_halign(Gtk.Align.START)
        self.append(actions_label)

        actions_box = self.create_quick_actions()
        self.append(actions_box)

    def create_card(self, title, value, description, card_type):
        """Create a status card"""
        card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        card.add_css_class("card")
        card.set_margin_top(12)
        card.set_margin_bottom(12)
        card.set_margin_start(12)
        card.set_margin_end(12)

        title_label = Gtk.Label(label=title)
        title_label.add_css_class("caption")
        title_label.add_css_class("dim-label")
        title_label.set_halign(Gtk.Align.START)
        card.append(title_label)

        value_label = Gtk.Label(label=value)
        value_label.add_css_class("title-1")
        value_label.set_halign(Gtk.Align.START)
        card.append(value_label)

        desc_label = Gtk.Label(label=description)
        desc_label.add_css_class("caption")
        desc_label.set_halign(Gtk.Align.START)
        card.append(desc_label)

        return card

    def create_system_info(self):
        """Create system information display"""
        grid = Gtk.Grid()
        grid.set_column_spacing(12)
        grid.set_row_spacing(12)
        grid.set_margin_top(12)

        # Get system info
        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        info_items = [
            ("CPU Usage:", f"{cpu_percent:.1f}%"),
            ("Memory:", f"{memory.percent:.1f}% ({memory.used // (1024**3)}GB / {memory.total // (1024**3)}GB)"),
            ("Disk:", f"{disk.percent:.1f}% ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)"),
            ("Kernel:", self.get_kernel_version()),
        ]

        for i, (label_text, value_text) in enumerate(info_items):
            label = Gtk.Label(label=label_text)
            label.add_css_class("dim-label")
            label.set_halign(Gtk.Align.START)
            grid.attach(label, 0, i, 1, 1)

            value = Gtk.Label(label=value_text)
            value.set_halign(Gtk.Align.START)
            grid.attach(value, 1, i, 1, 1)

        return grid

    def create_quick_actions(self):
        """Create quick actions buttons"""
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        box.set_margin_top(12)

        actions = [
            ("Update System", "system-software-update-symbolic"),
            ("Open Terminal", "utilities-terminal-symbolic"),
            ("System Settings", "preferences-system-symbolic"),
        ]

        for label, icon in actions:
            btn = Gtk.Button()
            btn_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
            
            btn_icon = Gtk.Image.new_from_icon_name(icon)
            btn_box.append(btn_icon)
            
            btn_label = Gtk.Label(label=label)
            btn_box.append(btn_label)
            
            btn.set_child(btn_box)
            btn.add_css_class("pill")
            box.append(btn)

        return box

    def get_kernel_version(self):
        """Get kernel version"""
        try:
            result = subprocess.run(['uname', '-r'], capture_output=True, text=True)
            return result.stdout.strip()
        except:
            return "Unknown"
