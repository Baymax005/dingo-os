#!/usr/bin/env python3
"""
Dingo Control Center - Entry Point
"""

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gio

from .app import DingoControlCenterApp


def main():
    """Main entry point for Dingo Control Center"""
    app = DingoControlCenterApp()
    return app.run(sys.argv)


if __name__ == "__main__":
    sys.exit(main())
