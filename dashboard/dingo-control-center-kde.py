#!/usr/bin/env python3
"""
Dingo Control Center 
Made By: Muhammad Ali (Github: Baymax005)
"""

import sys
import subprocess
import psutil
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame, QScrollArea, QGridLayout,
    QStackedWidget, QListWidget, QListWidgetItem, QProgressBar,
    QGroupBox, QSplitter
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QIcon


class DingoControlCenter(QMainWindow):
    """Main window for Dingo Control Center (KDE Edition)"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dingo Control Center")
        self.setGeometry(100, 100, 1200, 800)
        
        # Apply KDE Plasma styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #31363b;
            }
            QLabel {
                color: #eff0f1;
            }
            QPushButton {
                background-color: #3daee9;
                color: #eff0f1;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #42b5f0;
            }
            QPushButton:pressed {
                background-color: #2fa7e3;
            }
            QFrame {
                background-color: #232629;
                border-radius: 8px;
            }
            QListWidget {
                background-color: #232629;
                border: none;
                color: #eff0f1;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 12px;
                border-radius: 4px;
            }
            QListWidget::item:selected {
                background-color: #3daee9;
            }
            QListWidget::item:hover {
                background-color: #31363b;
            }
            QGroupBox {
                background-color: #232629;
                border: 1px solid #3f4447;
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 12px;
                color: #eff0f1;
                font-weight: bold;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 8px;
                padding: 0 4px;
            }
            QProgressBar {
                border: 1px solid #3f4447;
                border-radius: 4px;
                text-align: center;
                color: #eff0f1;
                background-color: #232629;
            }
            QProgressBar::chunk {
                background-color: #3daee9;
                border-radius: 3px;
            }
        """)
        
        self.init_ui()
        self.start_monitoring()
        
    def init_ui(self):
        """Initialize the UI"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Sidebar
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)
        
        # Content area
        self.content_stack = QStackedWidget()
        main_layout.addWidget(self.content_stack, 1)
        
        # Add views
        self.content_stack.addWidget(self.create_dashboard_view())
        self.content_stack.addWidget(self.create_gaming_view())
        self.content_stack.addWidget(self.create_developer_view())
        self.content_stack.addWidget(self.create_blockchain_view())
        self.content_stack.addWidget(self.create_security_view())
        
    def create_sidebar(self):
        """Create navigation sidebar"""
        sidebar = QFrame()
        sidebar.setFixedWidth(280)
        sidebar.setStyleSheet("background-color: #232629; border-radius: 0px;")
        
        layout = QVBoxLayout()
        sidebar.setLayout(layout)
        
        # Logo/Brand
        brand_layout = QVBoxLayout()
        logo = QLabel("🦘")
        logo.setStyleSheet("font-size: 48px;")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        brand_layout.addWidget(logo)
        
        title = QLabel("Dingo OS")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #3daee9;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        brand_layout.addWidget(title)
        
        subtitle = QLabel("Control Center")
        subtitle.setStyleSheet("font-size: 14px; color: #7f8c8d;")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        brand_layout.addWidget(subtitle)
        
        layout.addLayout(brand_layout)
        layout.addSpacing(20)
        
        # Navigation list
        self.nav_list = QListWidget()
        nav_items = [
            ("🏠  Dashboard", 0),
            ("🎮  Gaming", 1),
            ("🛠️  Developer", 2),
            ("⛓️  Blockchain", 3),
            ("🔒  Security", 4),
        ]
        
        for text, index in nav_items:
            item = QListWidgetItem(text)
            item.setData(Qt.ItemDataRole.UserRole, index)
            self.nav_list.addItem(item)
        
        self.nav_list.setCurrentRow(0)
        self.nav_list.currentItemChanged.connect(self.on_nav_changed)
        
        layout.addWidget(self.nav_list)
        layout.addStretch()
        
        # Status
        self.status_label = QLabel("System: ✓ Healthy")
        self.status_label.setStyleSheet("color: #27ae60; padding: 12px;")
        layout.addWidget(self.status_label)
        
        author_label = QLabel("Made By: Muhammad Ali\nGithub: Baymax005")
        author_label.setStyleSheet("color: #7f8c8d; font-size: 11px; padding: 12px;")
        author_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(author_label)
        
        return sidebar
    
    def create_dashboard_view(self):
        """Create dashboard view"""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        # Welcome section
        welcome = QLabel("Welcome to Dingo OS 🦘")
        welcome.setStyleSheet("font-size: 32px; font-weight: bold; color: #3daee9;")
        layout.addWidget(welcome)
        
        subtitle = QLabel("Your all-in-one development, gaming, and productivity system")
        subtitle.setStyleSheet("font-size: 14px; color: #7f8c8d; margin-bottom: 20px;")
        layout.addWidget(subtitle)
        
        # Stats grid
        stats_layout = QGridLayout()
        
        # CPU Card
        cpu_group = QGroupBox("CPU Usage")
        cpu_layout = QVBoxLayout()
        self.cpu_label = QLabel("0%")
        self.cpu_label.setStyleSheet("font-size: 36px; font-weight: bold; color: #3daee9;")
        cpu_layout.addWidget(self.cpu_label)
        self.cpu_bar = QProgressBar()
        cpu_layout.addWidget(self.cpu_bar)
        cpu_group.setLayout(cpu_layout)
        stats_layout.addWidget(cpu_group, 0, 0)
        
        # Memory Card
        mem_group = QGroupBox("Memory Usage")
        mem_layout = QVBoxLayout()
        self.mem_label = QLabel("0%")
        self.mem_label.setStyleSheet("font-size: 36px; font-weight: bold; color: #3daee9;")
        mem_layout.addWidget(self.mem_label)
        self.mem_bar = QProgressBar()
        mem_layout.addWidget(self.mem_bar)
        mem_group.setLayout(mem_layout)
        stats_layout.addWidget(mem_group, 0, 1)
        
        # Disk Card
        disk_group = QGroupBox("Disk Usage")
        disk_layout = QVBoxLayout()
        self.disk_label = QLabel("0%")
        self.disk_label.setStyleSheet("font-size: 36px; font-weight: bold; color: #3daee9;")
        disk_layout.addWidget(self.disk_label)
        self.disk_bar = QProgressBar()
        disk_layout.addWidget(self.disk_bar)
        disk_group.setLayout(disk_layout)
        stats_layout.addWidget(disk_group, 0, 2)
        
        layout.addLayout(stats_layout)
        
        # System info
        info_group = QGroupBox("System Information")
        info_layout = QVBoxLayout()
        self.kernel_label = QLabel(f"Kernel: {self.get_kernel_version()}")
        self.kernel_label.setStyleSheet("color: #eff0f1; padding: 4px;")
        info_layout.addWidget(self.kernel_label)
        
        self.uptime_label = QLabel("Uptime: Calculating...")
        self.uptime_label.setStyleSheet("color: #eff0f1; padding: 4px;")
        info_layout.addWidget(self.uptime_label)
        
        info_group.setLayout(info_layout)
        layout.addWidget(info_group)
        
        # Quick actions
        actions_layout = QHBoxLayout()
        
        terminal_btn = QPushButton("🖥️  Open Terminal")
        terminal_btn.clicked.connect(lambda: subprocess.Popen(['konsole']))
        actions_layout.addWidget(terminal_btn)
        
        settings_btn = QPushButton("⚙️  System Settings")
        settings_btn.clicked.connect(lambda: subprocess.Popen(['systemsettings']))
        actions_layout.addWidget(settings_btn)
        
        update_btn = QPushButton("⬇️  Update System")
        update_btn.clicked.connect(self.update_system)
        actions_layout.addWidget(update_btn)
        
        layout.addLayout(actions_layout)
        layout.addStretch()
        
        return widget
    
    def create_gaming_view(self):
        """Create gaming view"""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        title = QLabel("🎮 Gaming Mode")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #3daee9;")
        layout.addWidget(title)
        
        # Gaming mode button
        game_mode_btn = QPushButton("Enable Gaming Mode")
        game_mode_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                font-size: 16px;
                padding: 16px;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
        """)
        game_mode_btn.clicked.connect(self.toggle_gaming_mode)
        layout.addWidget(game_mode_btn)
        
        # GPU info
        gpu_group = QGroupBox("GPU Information")
        gpu_layout = QVBoxLayout()
        
        gpu_name = QLabel(f"GPU: {self.get_gpu_name()}")
        gpu_name.setStyleSheet("font-size: 16px; padding: 8px;")
        gpu_layout.addWidget(gpu_name)
        
        driver_info = QLabel(f"Driver: {self.get_driver_info()}")
        driver_info.setStyleSheet("padding: 8px;")
        gpu_layout.addWidget(driver_info)
        
        gpu_group.setLayout(gpu_layout)
        layout.addWidget(gpu_group)
        
        # Game platforms
        platforms_group = QGroupBox("Game Platforms")
        platforms_layout = QVBoxLayout()
        
        steam_btn = QPushButton("🎮  Launch Steam")
        steam_btn.clicked.connect(lambda: subprocess.Popen(['steam']))
        platforms_layout.addWidget(steam_btn)
        
        lutris_btn = QPushButton("🕹️  Launch Lutris")
        lutris_btn.clicked.connect(lambda: subprocess.Popen(['lutris']))
        platforms_layout.addWidget(lutris_btn)
        
        platforms_group.setLayout(platforms_layout)
        layout.addWidget(platforms_group)
        
        layout.addStretch()
        return widget
    
    def create_developer_view(self):
        """Create developer view"""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        title = QLabel("🛠️ Developer Tools")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #3daee9;")
        layout.addWidget(title)
        
        # Dev tools
        tools_layout = QGridLayout()
        
        vscode_btn = QPushButton("📝  VS Code")
        vscode_btn.clicked.connect(lambda: subprocess.Popen(['code']))
        tools_layout.addWidget(vscode_btn, 0, 0)
        
        docker_btn = QPushButton("🐳  Docker Desktop")
        docker_btn.clicked.connect(lambda: subprocess.Popen(['systemctl', 'start', 'docker']))
        tools_layout.addWidget(docker_btn, 0, 1)
        
        git_btn = QPushButton("🌿  Git GUI")
        git_btn.clicked.connect(lambda: subprocess.Popen(['git', 'gui']))
        tools_layout.addWidget(git_btn, 1, 0)
        
        term_btn = QPushButton("💻  Terminal")
        term_btn.clicked.connect(lambda: subprocess.Popen(['konsole']))
        tools_layout.addWidget(term_btn, 1, 1)
        
        layout.addLayout(tools_layout)
        layout.addStretch()
        return widget
    
    def create_blockchain_view(self):
        """Create blockchain view"""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        title = QLabel("⛓️ Blockchain & Mining")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #3daee9;")
        layout.addWidget(title)
        
        # Mining controls
        mining_group = QGroupBox("XMRig Mining")
        mining_layout = QVBoxLayout()
        
        start_mining_btn = QPushButton("▶️  Start Mining")
        start_mining_btn.clicked.connect(self.start_mining)
        mining_layout.addWidget(start_mining_btn)
        
        stop_mining_btn = QPushButton("⏹️  Stop Mining")
        stop_mining_btn.clicked.connect(self.stop_mining)
        mining_layout.addWidget(stop_mining_btn)
        
        mining_group.setLayout(mining_layout)
        layout.addWidget(mining_group)
        
        # Wallet
        wallet_group = QGroupBox("Crypto Wallet")
        wallet_layout = QVBoxLayout()
        
        electrum_btn = QPushButton("💰  Open Electrum Wallet")
        electrum_btn.clicked.connect(lambda: subprocess.Popen(['electrum']))
        wallet_layout.addWidget(electrum_btn)
        
        wallet_group.setLayout(wallet_layout)
        layout.addWidget(wallet_group)
        
        layout.addStretch()
        return widget
    
    def create_security_view(self):
        """Create security view"""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        title = QLabel("🔒 Security Settings")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #3daee9;")
        layout.addWidget(title)
        
        # Firewall
        firewall_group = QGroupBox("Firewall")
        firewall_layout = QVBoxLayout()
        
        ufw_status = QLabel("Status: Checking...")
        firewall_layout.addWidget(ufw_status)
        
        enable_fw_btn = QPushButton("Enable Firewall")
        enable_fw_btn.clicked.connect(lambda: subprocess.Popen(['pkexec', 'ufw', 'enable']))
        firewall_layout.addWidget(enable_fw_btn)
        
        firewall_group.setLayout(firewall_layout)
        layout.addWidget(firewall_group)
        
        layout.addStretch()
        return widget
    
    def on_nav_changed(self, current, previous):
        """Handle navigation change"""
        if current:
            index = current.data(Qt.ItemDataRole.UserRole)
            self.content_stack.setCurrentIndex(index)
    
    def start_monitoring(self):
        """Start system monitoring"""
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(2000)  # Update every 2 seconds
        self.update_stats()
    
    def update_stats(self):
        """Update system stats"""
        # CPU
        cpu_percent = psutil.cpu_percent(interval=0.1)
        self.cpu_label.setText(f"{cpu_percent:.1f}%")
        self.cpu_bar.setValue(int(cpu_percent))
        
        # Memory
        mem = psutil.virtual_memory()
        self.mem_label.setText(f"{mem.percent:.1f}%")
        self.mem_bar.setValue(int(mem.percent))
        
        # Disk
        disk = psutil.disk_usage('/')
        self.disk_label.setText(f"{disk.percent:.1f}%")
        self.disk_bar.setValue(int(disk.percent))
        
        # Uptime
        uptime = subprocess.run(['uptime', '-p'], capture_output=True, text=True)
        self.uptime_label.setText(f"Uptime: {uptime.stdout.strip()}")
    
    def get_kernel_version(self):
        """Get kernel version"""
        try:
            result = subprocess.run(['uname', '-r'], capture_output=True, text=True)
            return result.stdout.strip()
        except:
            return "Unknown"
    
    def get_gpu_name(self):
        """Get GPU name"""
        try:
            result = subprocess.run(['lspci'], capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if 'VGA' in line or '3D' in line:
                    return line.split(': ')[1] if ': ' in line else "Unknown GPU"
            return "GPU not detected"
        except:
            return "Unknown GPU"
    
    def get_driver_info(self):
        """Get driver info"""
        try:
            if subprocess.run(['which', 'nvidia-smi'], capture_output=True).returncode == 0:
                result = subprocess.run(['nvidia-smi', '--query-gpu=driver_version', '--format=csv,noheader'],
                                      capture_output=True, text=True)
                return f"NVIDIA {result.stdout.strip()}"
            return "Open Source Driver"
        except:
            return "Unknown"
    
    def toggle_gaming_mode(self):
        """Toggle gaming mode"""
        try:
            subprocess.run(['dingo-game'], check=True)
        except:
            subprocess.run(['notify-send', 'Gaming Mode', 'Failed to toggle gaming mode'])
    
    def update_system(self):
        """Update system"""
        subprocess.Popen(['konsole', '-e', 'sudo', 'apt', 'update', '&&', 'sudo', 'apt', 'upgrade', '-y'])
    
    def start_mining(self):
        """Start mining"""
        subprocess.Popen(['konsole', '-e', 'xmrig'])
    
    def stop_mining(self):
        """Stop mining"""
        subprocess.run(['pkill', 'xmrig'])


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Dingo Control Center")
    
    window = DingoControlCenter()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
