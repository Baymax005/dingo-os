"""
Settings View - Application settings
"""

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw


class SettingsView(Gtk.Box):
    """Settings view"""

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_margin_top(24)
        self.set_margin_bottom(24)
        self.set_margin_start(24)
        self.set_margin_end(24)

        # Header
        header = Gtk.Label(label="⚙️ Settings")
        header.add_css_class("title-1")
        self.append(header)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Profile Selection
        profile_label = Gtk.Label(label="Active Profile")
        profile_label.add_css_class("title-3")
        profile_label.set_halign(Gtk.Align.START)
        self.append(profile_label)

        profiles = self.create_profile_selector()
        self.append(profiles)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Preferences
        prefs_label = Gtk.Label(label="Preferences")
        prefs_label.add_css_class("title-3")
        prefs_label.set_halign(Gtk.Align.START)
        self.append(prefs_label)

        prefs = self.create_preferences()
        self.append(prefs)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # About
        about_label = Gtk.Label(label="About")
        about_label.add_css_class("title-3")
        about_label.set_halign(Gtk.Align.START)
        self.append(about_label)

        about = self.create_about_section()
        self.append(about)

    def create_profile_selector(self):
        """Create profile selector"""
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        box.set_margin_top(12)

        profiles = [
            ("standard", "Standard", "Balanced settings for general use"),
            ("developer", "Developer", "Optimized for software development"),
            ("gaming", "Gaming", "Maximum gaming performance"),
            ("blockchain", "Blockchain", "Node and network optimizations"),
            ("security", "Security", "Maximum security hardening"),
        ]

        for profile_id, name, desc in profiles:
            row = self.create_profile_row(profile_id, name, desc)
            box.append(row)

        return box

    def create_profile_row(self, profile_id, name, description):
        """Create a profile row"""
        btn = Gtk.Button()
        btn.add_css_class("card")
        btn.set_margin_top(4)
        btn.set_margin_bottom(4)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)

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

        box.append(info_box)

        if profile_id == "developer":  # Default selected
            check = Gtk.Image.new_from_icon_name("object-select-symbolic")
            check.add_css_class("success")
            box.append(check)

        btn.set_child(box)

        return btn

    def create_preferences(self):
        """Create preferences list"""
        list_box = Gtk.ListBox()
        list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        list_box.add_css_class("boxed-list")
        list_box.set_margin_top(12)

        # Auto-update
        auto_update = self.create_pref_row(
            "Automatic Updates",
            "Install security updates automatically",
            True
        )
        list_box.append(auto_update)

        # Notifications
        notifications = self.create_pref_row(
            "Notifications",
            "Show system notifications",
            True
        )
        list_box.append(notifications)

        # Start on Boot
        autostart = self.create_pref_row(
            "Start on Boot",
            "Launch Control Center on system startup",
            False
        )
        list_box.append(autostart)

        return list_box

    def create_pref_row(self, title, description, active):
        """Create a preference row"""
        row = Adw.ActionRow()
        row.set_title(title)
        row.set_subtitle(description)

        switch = Gtk.Switch()
        switch.set_active(active)
        switch.set_valign(Gtk.Align.CENTER)
        row.add_suffix(switch)

        return row

    def create_about_section(self):
        """Create about section"""
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        box.add_css_class("card")
        box.set_margin_top(12)

        # Logo
        logo = Gtk.Label(label="🦘")
        logo.add_css_class("title-1")
        box.append(logo)

        # Name
        name = Gtk.Label(label="Dingo OS Control Center")
        name.add_css_class("title-2")
        box.append(name)

        # Version
        version = Gtk.Label(label="Version 1.0.0")
        version.add_css_class("dim-label")
        box.append(version)

        # Copyright
        copyright_label = Gtk.Label(label="© 2024 Dingo OS Project")
        copyright_label.add_css_class("caption")
        copyright_label.add_css_class("dim-label")
        box.append(copyright_label)

        # Links
        links = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        links.set_halign(Gtk.Align.CENTER)
        links.set_margin_top(12)

        website_btn = Gtk.LinkButton(label="Website", uri="https://dingoos.io")
        website_btn.add_css_class("pill")
        links.append(website_btn)

        docs_btn = Gtk.LinkButton(label="Documentation", uri="https://docs.dingoos.io")
        docs_btn.add_css_class("pill")
        links.append(docs_btn)

        github_btn = Gtk.LinkButton(label="GitHub", uri="https://github.com/dingo-os/dingo-os")
        github_btn.add_css_class("pill")
        links.append(github_btn)

        box.append(links)

        return box
