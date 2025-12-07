"""
Gaming View - Gaming mode and GPU management
"""

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw
import subprocess
import os


class GamingView(Gtk.Box):
    """Gaming features view"""

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_margin_top(24)
        self.set_margin_bottom(24)
        self.set_margin_start(24)
        self.set_margin_end(24)

        # Header
        header = Gtk.Label(label="🎮 Gaming Mode")
        header.add_css_class("title-1")
        self.append(header)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Gaming mode toggle
        self.create_gaming_toggle()

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # GPU Information
        gpu_label = Gtk.Label(label="GPU Information")
        gpu_label.add_css_class("title-3")
        gpu_label.set_halign(Gtk.Align.START)
        self.append(gpu_label)

        gpu_info = self.create_gpu_info()
        self.append(gpu_info)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Installed Games
        games_label = Gtk.Label(label="Game Platforms")
        games_label.add_css_class("title-3")
        games_label.set_halign(Gtk.Align.START)
        self.append(games_label)

        platforms = self.create_platforms_list()
        self.append(platforms)

    def create_gaming_toggle(self):
        """Create gaming mode toggle"""
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        box.add_css_class("card")
        box.set_margin_top(12)

        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        info_box.set_hexpand(True)

        title = Gtk.Label(label="Gaming Mode")
        title.add_css_class("heading")
        title.set_halign(Gtk.Align.START)
        info_box.append(title)

        desc = Gtk.Label(label="Optimize system performance for gaming")
        desc.add_css_class("dim-label")
        desc.add_css_class("caption")
        desc.set_halign(Gtk.Align.START)
        info_box.append(desc)

        box.append(info_box)

        # Toggle switch
        switch = Gtk.Switch()
        switch.set_valign(Gtk.Align.CENTER)
        switch.connect("state-set", self.on_gaming_toggle)
        box.append(switch)

        self.append(box)

    def create_gpu_info(self):
        """Create GPU information display"""
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        box.set_margin_top(12)

        # Get GPU info
        gpu_name = self.get_gpu_name()
        
        info_card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        info_card.add_css_class("card")

        name_label = Gtk.Label(label=gpu_name)
        name_label.add_css_class("title-3")
        name_label.set_halign(Gtk.Align.START)
        info_card.append(name_label)

        # Driver info
        driver = self.get_driver_info()
        driver_label = Gtk.Label(label=f"Driver: {driver}")
        driver_label.add_css_class("dim-label")
        driver_label.set_halign(Gtk.Align.START)
        info_card.append(driver_label)

        box.append(info_card)

        # Driver actions
        action_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        action_box.set_margin_top(12)

        update_btn = Gtk.Button(label="Update Drivers")
        update_btn.add_css_class("pill")
        action_box.append(update_btn)

        settings_btn = Gtk.Button(label="GPU Settings")
        settings_btn.add_css_class("pill")
        action_box.append(settings_btn)

        box.append(action_box)

        return box

    def create_platforms_list(self):
        """Create list of game platforms"""
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        box.set_margin_top(12)

        platforms = [
            ("Steam", "steam", "Steam gaming platform"),
            ("Lutris", "lutris", "Open gaming platform"),
            ("Heroic", "heroic", "Epic Games & GOG launcher"),
        ]

        for name, cmd, desc in platforms:
            row = self.create_platform_row(name, cmd, desc)
            box.append(row)

        return box

    def create_platform_row(self, name, cmd, description):
        """Create a platform row"""
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        row.add_css_class("card")
        row.set_margin_top(4)
        row.set_margin_bottom(4)

        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        info_box.set_hexpand(True)

        name_label = Gtk.Label(label=name)
        name_label.set_halign(Gtk.Align.START)
        info_box.append(name_label)

        desc_label = Gtk.Label(label=description)
        desc_label.add_css_class("dim-label")
        desc_label.add_css_class("caption")
        desc_label.set_halign(Gtk.Align.START)
        info_box.append(desc_label)

        row.append(info_box)

        # Status
        installed = os.path.exists(f"/usr/bin/{cmd}") or os.path.exists(f"/usr/games/{cmd}")
        
        if installed:
            launch_btn = Gtk.Button(label="Launch")
            launch_btn.add_css_class("pill")
            launch_btn.add_css_class("suggested-action")
            row.append(launch_btn)
        else:
            install_btn = Gtk.Button(label="Install")
            install_btn.add_css_class("pill")
            row.append(install_btn)

        return row

    def on_gaming_toggle(self, switch, state):
        """Handle gaming mode toggle"""
        if state:
            print("Enabling gaming mode...")
            # TODO: Enable GameMode
        else:
            print("Disabling gaming mode...")
            # TODO: Disable GameMode
        return False

    def get_gpu_name(self):
        """Get GPU name"""
        try:
            result = subprocess.run(
                ['lspci'],
                capture_output=True,
                text=True
            )
            for line in result.stdout.split('\n'):
                if 'VGA' in line or '3D' in line:
                    parts = line.split(': ')
                    if len(parts) > 1:
                        return parts[1]
            return "GPU not detected"
        except:
            return "Unknown GPU"

    def get_driver_info(self):
        """Get driver information"""
        # Check for NVIDIA
        if os.path.exists('/proc/driver/nvidia/version'):
            try:
                with open('/proc/driver/nvidia/version', 'r') as f:
                    return f.readline().strip()
            except:
                pass
        
        # Check for AMD
        if os.path.exists('/sys/module/amdgpu'):
            return "AMDGPU (Open Source)"
        
        return "Unknown driver"
