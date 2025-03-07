import json
import os
import questionary

CONFIG_FILE = "config.json"

class Configure:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self) -> dict:
        """Load config from file, return empty dict if not found."""
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        return {}

    def save_config(self):
        """Save the current configuration to a file."""
        with open(CONFIG_FILE, "w") as f:
            json.dump(self.config, f, indent=4)

    def ask_user_for_config(self):
        """Prompt user for configuration values interactively."""
        self.config = {
            "obs_host": questionary.text("Enter OBS WebSocket Host (default: 192.168.1.6):", default="192.168.1.6").ask(),
            "obs_port": questionary.text("Enter OBS WebSocket Port (default: 4455):", default="4455").ask(),
            "obs_password": questionary.password("Enter OBS WebSocket Password (default: 123456789):", default="123456789").ask(),
            
            "insta_username": questionary.text("Enter Instagram UserName:").ask(),
            "insta_password": questionary.password("Enter Instagram Password:").ask(),
            
            "mt_path": questionary.text("Enter MetaTrader path (default: C:\Program Files\MetaTrader 5\terminal64.exe):", default="C:\\Program Files\\MetaTrader 5\\terminal64.exe").ask(),
            "mt_server": questionary.text("Enter MetaTrader Server:").ask(),
            "mt_user": questionary.text("Enter MetaTrader User:").ask(),
            "mt_password": questionary.password("Enter MetaTrader Password:").ask(),
            
            "mt_symbol": questionary.password("Enter MetaTrader Symbol:").ask(),
            
            "video_quality": questionary.text("Enter Video quality: (defualt: 10000)", default=10000).ask(),
        }
        self.save_config()
        print("\nConfiguration saved successfully!\n")

    def configure(self):
        """Set up configuration."""
        self.ask_user_for_config()

    def get_config_value(self, key: str, default=None):
        """Get a specific config value, return default if not found."""
        return self.config.get(key, default)
