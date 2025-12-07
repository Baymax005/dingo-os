#!/usr/bin/env python3
"""
Dingo OS Daemon - System management service
Provides D-Bus interface for system operations
"""

import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GLib
import subprocess
import json
import logging
import sys
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('dingod')

# D-Bus constants
BUS_NAME = 'org.dingoos.Daemon'
OBJECT_PATH = '/org/dingoos/Daemon'

# Config paths
CONFIG_DIR = Path('/etc/dingo')
PROFILES_DIR = CONFIG_DIR / 'profiles'
STATE_FILE = Path('/var/lib/dingo/state.json')


class DingoState:
    """Manages Dingo OS state"""
    
    def __init__(self):
        self.state = self.load_state()
    
    def load_state(self):
        """Load state from disk"""
        if STATE_FILE.exists():
            try:
                with open(STATE_FILE, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load state: {e}")
        
        # Default state
        return {
            'profile': 'standard',
            'gaming_mode': False,
            'services': {},
            'last_update': None,
        }
    
    def save_state(self):
        """Save state to disk"""
        try:
            STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(STATE_FILE, 'w') as f:
                json.dump(self.state, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save state: {e}")
    
    def get(self, key, default=None):
        """Get state value"""
        return self.state.get(key, default)
    
    def set(self, key, value):
        """Set state value"""
        self.state[key] = value
        self.save_state()


class DingoDaemon(dbus.service.Object):
    """Main Dingo OS daemon"""
    
    def __init__(self, bus, object_path):
        super().__init__(bus, object_path)
        self.state = DingoState()
        logger.info("Dingo daemon initialized")
    
    @dbus.service.method(BUS_NAME, out_signature='a{sv}')
    def GetStatus(self):
        """Get system status"""
        logger.info("GetStatus called")
        
        status = {
            'profile': self.state.get('profile'),
            'gaming_mode': self.state.get('gaming_mode'),
            'health': 'healthy',
            'updates_available': self.check_updates(),
        }
        
        return status
    
    @dbus.service.method(BUS_NAME, in_signature='s', out_signature='b')
    def SetProfile(self, profile_name):
        """Set active profile"""
        logger.info(f"SetProfile called: {profile_name}")
        
        valid_profiles = ['standard', 'developer', 'gaming', 'blockchain', 'security']
        if profile_name not in valid_profiles:
            logger.error(f"Invalid profile: {profile_name}")
            return False
        
        # Apply profile
        profile_file = PROFILES_DIR / f"{profile_name}.conf"
        if not profile_file.exists():
            logger.error(f"Profile file not found: {profile_file}")
            return False
        
        try:
            # Load and apply profile settings
            self.apply_profile(profile_file)
            self.state.set('profile', profile_name)
            logger.info(f"Profile set to: {profile_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to set profile: {e}")
            return False
    
    @dbus.service.method(BUS_NAME, in_signature='as', out_signature='b')
    def InstallPackages(self, packages):
        """Install packages"""
        logger.info(f"InstallPackages called: {packages}")
        
        try:
            cmd = ['apt-get', 'install', '-y'] + list(packages)
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                logger.info("Packages installed successfully")
                return True
            else:
                logger.error(f"Package installation failed: {result.stderr}")
                return False
        except Exception as e:
            logger.error(f"Failed to install packages: {e}")
            return False
    
    @dbus.service.method(BUS_NAME, in_signature='b', out_signature='b')
    def SetGamingMode(self, enabled):
        """Enable/disable gaming mode"""
        logger.info(f"SetGamingMode called: {enabled}")
        
        try:
            if enabled:
                # Enable GameMode
                self.run_command(['systemctl', '--user', 'start', 'gamemoded'])
                # Set performance governor
                self.run_command(['cpupower', 'frequency-set', '-g', 'performance'])
            else:
                # Disable GameMode
                self.run_command(['systemctl', '--user', 'stop', 'gamemoded'])
                # Set powersave governor
                self.run_command(['cpupower', 'frequency-set', '-g', 'powersave'])
            
            self.state.set('gaming_mode', enabled)
            return True
        except Exception as e:
            logger.error(f"Failed to set gaming mode: {e}")
            return False
    
    @dbus.service.method(BUS_NAME, in_signature='s', out_signature='b')
    def StartService(self, service_name):
        """Start a service"""
        logger.info(f"StartService called: {service_name}")
        
        try:
            result = subprocess.run(
                ['systemctl', 'start', service_name],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except Exception as e:
            logger.error(f"Failed to start service: {e}")
            return False
    
    @dbus.service.method(BUS_NAME, in_signature='s', out_signature='b')
    def StopService(self, service_name):
        """Stop a service"""
        logger.info(f"StopService called: {service_name}")
        
        try:
            result = subprocess.run(
                ['systemctl', 'stop', service_name],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except Exception as e:
            logger.error(f"Failed to stop service: {e}")
            return False
    
    @dbus.service.method(BUS_NAME, out_signature='b')
    def RunSecurityAudit(self):
        """Run security audit"""
        logger.info("RunSecurityAudit called")
        
        try:
            # Run security checks
            checks = [
                ('ufw', ['ufw', 'status']),
                ('fail2ban', ['fail2ban-client', 'status']),
                ('apparmor', ['aa-status']),
            ]
            
            results = {}
            for name, cmd in checks:
                result = subprocess.run(cmd, capture_output=True, text=True)
                results[name] = result.returncode == 0
            
            logger.info(f"Security audit results: {results}")
            return all(results.values())
        except Exception as e:
            logger.error(f"Security audit failed: {e}")
            return False
    
    @dbus.service.signal(BUS_NAME, signature='ss')
    def StatusChanged(self, component, status):
        """Signal when status changes"""
        logger.info(f"Status changed: {component} -> {status}")
    
    def apply_profile(self, profile_file):
        """Apply profile configuration"""
        logger.info(f"Applying profile: {profile_file}")
        
        # Read profile config
        with open(profile_file, 'r') as f:
            config = f.read()
        
        # Parse and apply settings
        # TODO: Implement profile application logic
        pass
    
    def check_updates(self):
        """Check for available updates"""
        try:
            result = subprocess.run(
                ['apt-get', 'upgrade', '--dry-run'],
                capture_output=True,
                text=True
            )
            
            # Count upgradable packages
            lines = result.stdout.split('\n')
            upgradable = [l for l in lines if 'upgraded' in l]
            
            if upgradable:
                # Parse number
                parts = upgradable[0].split()
                if parts:
                    return int(parts[0])
            
            return 0
        except:
            return 0
    
    def run_command(self, cmd):
        """Run a command"""
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Command failed: {result.stderr}")
        return result.stdout


def main():
    """Main entry point"""
    logger.info("Starting Dingo daemon...")
    
    # Setup D-Bus
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    
    try:
        bus = dbus.SystemBus()
        name = dbus.service.BusName(BUS_NAME, bus)
        daemon = DingoDaemon(bus, OBJECT_PATH)
        
        logger.info(f"Daemon registered on {BUS_NAME}")
        
        # Run main loop
        loop = GLib.MainLoop()
        logger.info("Entering main loop")
        loop.run()
    except KeyboardInterrupt:
        logger.info("Daemon stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Daemon error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
