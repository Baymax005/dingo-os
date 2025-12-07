"""
Dingo Control Center Application
"""

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw, Gio, GLib

from .window import DingoWindow


class DingoControlCenterApp(Adw.Application):
    """Main application class for Dingo Control Center"""

    def __init__(self):
        super().__init__(
            application_id="org.dingoos.ControlCenter",
            flags=Gio.ApplicationFlags.FLAGS_NONE
        )
        
        self.set_resource_base_path("/org/dingoos/ControlCenter")
        
        # Create actions
        self.create_actions()

    def create_actions(self):
        """Create application actions"""
        # Quit action
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.on_quit)
        self.add_action(quit_action)
        self.set_accels_for_action("app.quit", ["<Ctrl>q"])

        # About action
        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.on_about)
        self.add_action(about_action)

        # Preferences action
        prefs_action = Gio.SimpleAction.new("preferences", None)
        prefs_action.connect("activate", self.on_preferences)
        self.add_action(prefs_action)
        self.set_accels_for_action("app.preferences", ["<Ctrl>comma"])

    def do_activate(self):
        """Called when the application is activated"""
        win = self.props.active_window
        if not win:
            win = DingoWindow(application=self)
        win.present()

    def on_quit(self, action, param):
        """Handle quit action"""
        self.quit()

    def on_about(self, action, param):
        """Show about dialog"""
        about = Adw.AboutWindow(
            transient_for=self.props.active_window,
            application_name="Dingo Control Center",
            application_icon="org.dingoos.ControlCenter",
            developer_name="Dingo OS Team",
            version="1.0.0",
            developers=["Dingo OS Team"],
            copyright="© 2024 Dingo OS Project",
            license_type=Gtk.License.GPL_3_0,
            website="https://dingoos.io",
            issue_url="https://github.com/dingo-os/dingo-os/issues",
            comments="A unified dashboard for managing Dingo OS"
        )
        about.present()

    def on_preferences(self, action, param):
        """Show preferences dialog"""
        # TODO: Implement preferences window
        pass
