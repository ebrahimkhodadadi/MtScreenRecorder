import os
import pickle
from instagrapi import Client

class InstagramBot:
    def __init__(self, username: str, password: str, session_file="session.pkl"):
        """Initialize the Instagram bot with username, password, and session file."""
        self.client = Client()
        self.username = username
        self.password = password
        self.session_file = session_file

    def save_session(self):
        """Saves the current session to a file."""
        with open(self.session_file, "wb") as f:
            pickle.dump(self.client.get_settings(), f)
        print("✅ Session saved.")

    def load_session(self):
        """Loads session from file if available."""
        if os.path.exists(self.session_file):
            try:
                with open(self.session_file, "rb") as f:
                    session_data = pickle.load(f)
                self.client.set_settings(session_data)
                self.client.login(self.username, self.password)
                print("✅ Session loaded successfully!")
                return True
            except Exception as e:
                print(f"⚠️ Failed to load session: {e}, logging in manually...")
                return False
        return False

    def login(self) -> bool:
        """Logs into Instagram (tries session first, then manual login)."""
        if self.load_session():
            return True
        
        try:
            self.client.login(self.username, self.password)
            self.save_session()  # Save session after logging in
            print("✅ Login successful!")
            return True
        except Exception as e:
            print(f"❌ Login failed: {e}")
            return False

    def upload_story(self, video_path: str):
        """Uploads an MP4 video as an Instagram story."""
        try:
            if not self.client.username:
                print("❌ Not logged in. Please log in first.")
                return False
            
            self.client.video_upload_to_story(video_path)
            print("✅ Video story uploaded successfully!")
            return True
        except Exception as e:
            print(f"❌ Failed to upload story: {e}")
            return False

# Example Usage
if __name__ == "__main__":
    username = "your_instagram_username"
    password = "your_instagram_password"
    
    insta_bot = InstagramBot(username, password)
    
    if insta_bot.login():
        insta_bot.upload_story("your_video.mp4")  # Replace with actual MP4 file path
