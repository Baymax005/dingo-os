"""
Blockchain View - Blockchain tools management
"""

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw


class BlockchainView(Gtk.Box):
    """Blockchain tools view"""

    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_margin_top(24)
        self.set_margin_bottom(24)
        self.set_margin_start(24)
        self.set_margin_end(24)

        # Header
        header = Gtk.Label(label="⛓️ Blockchain Tools")
        header.add_css_class("title-1")
        self.append(header)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Local Testnet
        testnet_label = Gtk.Label(label="Local Development Network")
        testnet_label.add_css_class("title-3")
        testnet_label.set_halign(Gtk.Align.START)
        self.append(testnet_label)

        testnet_card = self.create_testnet_card()
        self.append(testnet_card)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Development Tools
        tools_label = Gtk.Label(label="Development Frameworks")
        tools_label.add_css_class("title-3")
        tools_label.set_halign(Gtk.Align.START)
        self.append(tools_label)

        tools_list = self.create_tools_list()
        self.append(tools_list)

        self.append(Gtk.Separator(margin_top=20, margin_bottom=20))

        # Nodes
        nodes_label = Gtk.Label(label="Blockchain Nodes")
        nodes_label.add_css_class("title-3")
        nodes_label.set_halign(Gtk.Align.START)
        self.append(nodes_label)

        nodes_list = self.create_nodes_list()
        self.append(nodes_list)

    def create_testnet_card(self):
        """Create local testnet card"""
        card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        card.add_css_class("card")
        card.set_margin_top(12)

        # Status
        status_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        
        status_label = Gtk.Label(label="Status:")
        status_label.set_halign(Gtk.Align.START)
        status_box.append(status_label)

        self.testnet_status = Gtk.Label(label="● Stopped")
        self.testnet_status.add_css_class("error")
        status_box.append(self.testnet_status)

        card.append(status_box)

        # Info
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        
        rpc_label = Gtk.Label(label="RPC URL: http://localhost:8545")
        rpc_label.add_css_class("dim-label")
        rpc_label.set_halign(Gtk.Align.START)
        info_box.append(rpc_label)

        chain_label = Gtk.Label(label="Chain ID: 31337")
        chain_label.add_css_class("dim-label")
        chain_label.set_halign(Gtk.Align.START)
        info_box.append(chain_label)

        card.append(info_box)

        # Actions
        actions = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        actions.set_margin_top(8)

        self.start_btn = Gtk.Button(label="Start Testnet")
        self.start_btn.add_css_class("pill")
        self.start_btn.add_css_class("suggested-action")
        self.start_btn.connect("clicked", self.on_testnet_toggle)
        actions.append(self.start_btn)

        reset_btn = Gtk.Button(label="Reset")
        reset_btn.add_css_class("pill")
        actions.append(reset_btn)

        card.append(actions)

        return card

    def create_tools_list(self):
        """Create blockchain tools list"""
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        box.set_margin_top(12)

        tools = [
            ("Hardhat", "Ethereum development environment", True),
            ("Foundry", "Blazing fast Ethereum toolkit", True),
            ("Truffle", "Classic development framework", False),
            ("Brownie", "Python-based framework", False),
        ]

        for name, desc, installed in tools:
            row = self.create_tool_row(name, desc, installed)
            box.append(row)

        return box

    def create_tool_row(self, name, description, installed):
        """Create a tool row"""
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

        if installed:
            status = Gtk.Label(label="✓ Installed")
            status.add_css_class("success")
            row.append(status)
        else:
            install_btn = Gtk.Button(label="Install")
            install_btn.add_css_class("pill")
            row.append(install_btn)

        return row

    def create_nodes_list(self):
        """Create blockchain nodes list"""
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        box.set_margin_top(12)

        nodes = [
            ("Ethereum (Geth)", "Ethereum execution client", False),
            ("Bitcoin Core", "Bitcoin full node", False),
        ]

        for name, desc, running in nodes:
            row = self.create_node_row(name, desc, running)
            box.append(row)

        return box

    def create_node_row(self, name, description, running):
        """Create a node row"""
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

        status = Gtk.Label(label="● Stopped" if not running else "● Running")
        if not running:
            status.add_css_class("error")
        else:
            status.add_css_class("success")
        row.append(status)

        action_btn = Gtk.Button(label="Start" if not running else "Stop")
        action_btn.add_css_class("pill")
        row.append(action_btn)

        return row

    def on_testnet_toggle(self, button):
        """Handle testnet toggle"""
        current_label = self.testnet_status.get_label()
        
        if "Stopped" in current_label:
            self.testnet_status.set_label("● Running")
            self.testnet_status.remove_css_class("error")
            self.testnet_status.add_css_class("success")
            self.start_btn.set_label("Stop Testnet")
            self.start_btn.remove_css_class("suggested-action")
            self.start_btn.add_css_class("destructive-action")
        else:
            self.testnet_status.set_label("● Stopped")
            self.testnet_status.remove_css_class("success")
            self.testnet_status.add_css_class("error")
            self.start_btn.set_label("Start Testnet")
            self.start_btn.remove_css_class("destructive-action")
            self.start_btn.add_css_class("suggested-action")
