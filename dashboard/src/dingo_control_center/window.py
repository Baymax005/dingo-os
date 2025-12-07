"""
Dingo Control Center Main Window
"""

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw, GLib

from .views.dashboard_view import DashboardView
from .views.developer_view import DeveloperView
from .views.gaming_view import GamingView
from .views.blockchain_view import BlockchainView
from .views.security_view import SecurityView
from .views.settings_view import SettingsView


class DingoWindow(Adw.ApplicationWindow):
    """Main window for Dingo Control Center"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.set_title("Dingo Control Center")
        self.set_default_size(1200, 800)
        
        # Build UI
        self.build_ui()
        
        # Start system monitor
        self.start_monitoring()

    def build_ui(self):
        """Build the main UI"""
        # Main layout
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_content(self.main_box)

        # Header bar
        header = Adw.HeaderBar()
        
        # Title
        title = Adw.WindowTitle(
            title="Dingo Control Center",
            subtitle="System Management Dashboard"
        )
        header.set_title_widget(title)

        # Menu button
        menu_button = Gtk.MenuButton()
        menu_button.set_icon_name("open-menu-symbolic")
        menu_button.set_menu_model(self.create_menu())
        header.pack_end(menu_button)

        self.main_box.append(header)

        # Navigation split view
        self.split_view = Adw.NavigationSplitView()
        self.main_box.append(self.split_view)
        
        # Sidebar
        sidebar = self.create_sidebar()
        self.split_view.set_sidebar(sidebar)

        # Content area
        self.content_stack = Gtk.Stack()
        self.content_stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
        
        # Add views
        self.dashboard_view = DashboardView()
        self.developer_view = DeveloperView()
        self.gaming_view = GamingView()
        self.blockchain_view = BlockchainView()
        self.security_view = SecurityView()
        self.settings_view = SettingsView()

        self.content_stack.add_named(self.dashboard_view, "dashboard")
        self.content_stack.add_named(self.developer_view, "developer")
        self.content_stack.add_named(self.gaming_view, "gaming")
        self.content_stack.add_named(self.blockchain_view, "blockchain")
        self.content_stack.add_named(self.security_view, "security")
        self.content_stack.add_named(self.settings_view, "settings")

        content_page = Adw.NavigationPage(
            title="Dashboard",
            child=self.content_stack
        )
        self.split_view.set_content(content_page)

    def create_sidebar(self):
        """Create the navigation sidebar"""
        sidebar_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        sidebar_box.set_size_request(250, -1)

        # Logo/Brand area
        brand_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        brand_box.set_margin_top(20)
        brand_box.set_margin_bottom(20)
        brand_box.set_margin_start(16)
        brand_box.set_margin_end(16)

        logo_label = Gtk.Label(label="🦘")
        logo_label.add_css_class("title-1")
        brand_box.append(logo_label)

        title_label = Gtk.Label(label="Dingo OS")
        title_label.add_css_class("title-2")
        brand_box.append(title_label)

        sidebar_box.append(brand_box)
        sidebar_box.append(Gtk.Separator())

        # Navigation list
        nav_list = Gtk.ListBox()
        nav_list.set_selection_mode(Gtk.SelectionMode.SINGLE)
        nav_list.add_css_class("navigation-sidebar")
        nav_list.connect("row-selected", self.on_nav_selected)

        # Navigation items
        nav_items = [
            ("dashboard", "🏠", "Dashboard", "System overview and quick actions"),
            ("developer", "🛠️", "Developer", "Development tools and environment"),
            ("gaming", "🎮", "Gaming", "Gaming mode and GPU settings"),
            ("blockchain", "⛓️", "Blockchain", "Blockchain tools and nodes"),
            ("security", "🔒", "Security", "Security settings and firewall"),
            ("settings", "⚙️", "Settings", "Application preferences"),
        ]

        for item_id, icon, title, subtitle in nav_items:
            row = self.create_nav_row(item_id, icon, title, subtitle)
            nav_list.append(row)

        # Select first row
        nav_list.select_row(nav_list.get_row_at_index(0))

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_vexpand(True)
        scrolled.set_child(nav_list)
        sidebar_box.append(scrolled)

        # Status bar at bottom
        status_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        status_box.set_margin_top(12)
        status_box.set_margin_bottom(12)
        status_box.set_margin_start(16)
        status_box.set_margin_end(16)

        self.status_label = Gtk.Label(label="System: Healthy")
        self.status_label.add_css_class("dim-label")
        self.status_label.set_halign(Gtk.Align.START)
        status_box.append(self.status_label)

        self.profile_label = Gtk.Label(label="Profile: Standard")
        self.profile_label.add_css_class("dim-label")
        self.profile_label.set_halign(Gtk.Align.START)
        status_box.append(self.profile_label)

        sidebar_box.append(Gtk.Separator())
        sidebar_box.append(status_box)

        sidebar_page = Adw.NavigationPage(
            title="Navigation",
            child=sidebar_box
        )
        
        return sidebar_page

    def create_nav_row(self, item_id, icon, title, subtitle):
        """Create a navigation row"""
        row = Gtk.ListBoxRow()
        row.set_name(item_id)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        box.set_margin_top(12)
        box.set_margin_bottom(12)
        box.set_margin_start(16)
        box.set_margin_end(16)

        icon_label = Gtk.Label(label=icon)
        icon_label.add_css_class("title-3")
        box.append(icon_label)

        text_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        
        title_label = Gtk.Label(label=title)
        title_label.set_halign(Gtk.Align.START)
        title_label.add_css_class("heading")
        text_box.append(title_label)

        subtitle_label = Gtk.Label(label=subtitle)
        subtitle_label.set_halign(Gtk.Align.START)
        subtitle_label.add_css_class("dim-label")
        subtitle_label.add_css_class("caption")
        text_box.append(subtitle_label)

        box.append(text_box)
        row.set_child(box)

        return row

    def on_nav_selected(self, listbox, row):
        """Handle navigation selection"""
        if row:
            page_name = row.get_name()
            self.content_stack.set_visible_child_name(page_name)

    def create_menu(self):
        """Create the application menu"""
        menu = Gio.Menu()
        menu.append("Preferences", "app.preferences")
        menu.append("About Dingo Control Center", "app.about")
        menu.append("Quit", "app.quit")
        return menu

    def start_monitoring(self):
        """Start system monitoring"""
        # Update status every 5 seconds
        GLib.timeout_add_seconds(5, self.update_status)
        self.update_status()

    def update_status(self):
        """Update system status"""
        # This would be replaced with actual system monitoring
        self.status_label.set_text("System: ✓ Healthy")
        return True  # Continue timeout
