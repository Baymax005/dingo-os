"""
Security View - Security settings and management
"""

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw
import subprocess


class SecurityView(Gtk.Box):
    """Security settings view"""

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_margin_top(24)
        self.set_margin_bottom(24)
        self.set_margin_start(24)
        self.set_margin_end(24)

        # Header
        header = Gtk.Label(label="🔒 Security Center")
        header.add_css_class("title-1")
        self.append(header)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Security Status
        status_label = Gtk.Label(label="Security Status")
        status_label.add_css_class("title-3")
        status_label.set_halign(Gtk.Align.START)
        self.append(status_label)

        status_grid = self.create_status_grid()
        self.append(status_grid)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Firewall
        firewall_label = Gtk.Label(label="Firewall")
        firewall_label.add_css_class("title-3")
        firewall_label.set_halign(Gtk.Align.START)
        self.append(firewall_label)

        firewall_card = self.create_firewall_card()
        self.append(firewall_card)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Quick Actions
        actions_label = Gtk.Label(label="Security Actions")
        actions_label.add_css_class("title-3")
        actions_label.set_halign(Gtk.Align.START)
        self.append(actions_label)

        actions = self.create_security_actions()
        self.append(actions)

    def create_status_grid(self):
        """Create security status grid"""
        grid = Gtk.Grid()
        grid.set_column_spacing(24)
        grid.set_row_spacing(12)
        grid.set_margin_top(12)
        grid.set_column_homogeneous(True)

        status_items = [
            ("Firewall", self.check_firewall_status()),
            ("Updates", "Auto-update enabled"),
            ("AppArmor", self.check_apparmor_status()),
            ("Encryption", "LUKS enabled"),
        ]

        for i, (label, status) in enumerate(status_items):
            card = self.create_status_card(label, status)
            grid.attach(card, i % 2, i // 2, 1, 1)

        return grid

    def create_status_card(self, title, status):
        """Create a status card"""
        card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        card.add_css_class("card")

        title_label = Gtk.Label(label=title)
        title_label.add_css_class("caption")
        title_label.add_css_class("dim-label")
        title_label.set_halign(Gtk.Align.START)
        card.append(title_label)

        status_label = Gtk.Label(label=status)
        status_label.set_halign(Gtk.Align.START)
        if "enabled" in status.lower() or "active" in status.lower():
            status_label.add_css_class("success")
        card.append(status_label)

        return card

    def create_firewall_card(self):
        """Create firewall management card"""
        card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        card.add_css_class("card")
        card.set_margin_top(12)

        # Status
        status_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        
        label = Gtk.Label(label="Status:")
        label.set_halign(Gtk.Align.START)
        status_box.append(label)

        self.firewall_status = Gtk.Label(label="● Active")
        self.firewall_status.add_css_class("success")
        self.firewall_status.set_hexpand(True)
        status_box.append(self.firewall_status)

        # Toggle
        self.firewall_switch = Gtk.Switch()
        self.firewall_switch.set_active(True)
        self.firewall_switch.set_valign(Gtk.Align.CENTER)
        self.firewall_switch.connect("state-set", self.on_firewall_toggle)
        status_box.append(self.firewall_switch)

        card.append(status_box)

        # Rules
        rules_label = Gtk.Label(label="Active rules: 8")
        rules_label.add_css_class("dim-label")
        rules_label.set_halign(Gtk.Align.START)
        card.append(rules_label)

        # Actions
        actions = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        actions.set_margin_top(8)

        manage_btn = Gtk.Button(label="Manage Rules")
        manage_btn.add_css_class("pill")
        actions.append(manage_btn)

        logs_btn = Gtk.Button(label="View Logs")
        logs_btn.add_css_class("pill")
        actions.append(logs_btn)

        card.append(actions)

        return card

    def create_security_actions(self):
        """Create security action buttons"""
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        box.set_margin_top(12)

        actions = [
            ("Run Security Audit", "Scan system for vulnerabilities"),
            ("Update System", "Install security updates"),
            ("Backup Encryption Keys", "Backup LUKS keys safely"),
            ("View Security Logs", "Check authentication logs"),
        ]

        for title, desc in actions:
            btn = self.create_action_button(title, desc)
            box.append(btn)

        return box

    def create_action_button(self, title, description):
        """Create an action button"""
        btn = Gtk.Button()
        btn.add_css_class("card")
        btn.set_margin_top(4)
        btn.set_margin_bottom(4)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)

        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        info_box.set_hexpand(True)

        title_label = Gtk.Label(label=title)
        title_label.set_halign(Gtk.Align.START)
        info_box.append(title_label)

        desc_label = Gtk.Label(label=description)
        desc_label.add_css_class("dim-label")
        desc_label.add_css_class("caption")
        desc_label.set_halign(Gtk.Align.START)
        info_box.append(desc_label)

        box.append(info_box)

        arrow = Gtk.Image.new_from_icon_name("go-next-symbolic")
        box.append(arrow)

        btn.set_child(box)

        return btn

    def check_firewall_status(self):
        """Check UFW firewall status"""
        try:
            result = subprocess.run(
                ['sudo', 'ufw', 'status'],
                capture_output=True,
                text=True,
                timeout=2
            )
            if 'active' in result.stdout.lower():
                return "● Active"
            return "● Inactive"
        except:
            return "Unknown"

    def check_apparmor_status(self):
        """Check AppArmor status"""
        try:
            result = subprocess.run(
                ['sudo', 'aa-status'],
                capture_output=True,
                text=True,
                timeout=2
            )
            if result.returncode == 0:
                return "● Active"
            return "● Inactive"
        except:
            return "Unknown"

    def on_firewall_toggle(self, switch, state):
        """Handle firewall toggle"""
        if state:
            self.firewall_status.set_label("● Active")
            self.firewall_status.add_css_class("success")
            print("Enabling firewall...")
        else:
            self.firewall_status.set_label("● Inactive")
            self.firewall_status.remove_css_class("success")
            print("Disabling firewall...")
        return False
