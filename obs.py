from obswebsocket import obsws, requests, exceptions

class Obs:
    def __init__(self, host: str, port: int, password: int):
        self.OBS_HOST = host
        self.OBS_PORT = port
        self.OBS_PASSWORD = password
        
        # Initialize OBS WebSocket client
        self.obs_client = obsws(self.OBS_HOST, self.OBS_PORT, self.OBS_PASSWORD)
        
    def connect_to_obs(self):
        """Connect to OBS WebSocket with retry logic."""
        try:
            print("Connecting to OBS WebSocket...")
            self.obs_client.connect()
            print("Connected to OBS WebSocket.")
        except Exception as e:
            print(f"Failed to connect to OBS WebSocket: {e}")
            exit(1)
            
    def disconnect(self):
        self.obs_client.disconnect()

    def start_recording(self) -> bool:
        """Start recording in OBS."""
        try:
            print("Attempting to start recording...")
            response = self.obs_client.call(requests.StartRecord())
            if response.status:
                print("Recording started successfully.")
                return True
            else:
                print("Failed to start recording.")
        except exceptions.ObswebsocketError as e:
            print(f"Failed to start recording: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return False
            
    def stop_recording(self):
        """Stop recording in OBS."""
        try:
            print("Attempting to stop recording...")
            response = self.obs_client.call(requests.StopRecord())
            if response.status:
                print("Recording stopped successfully.")
            else:
                print("Failed to stop recording.")
        except exceptions.ObswebsocketError as e:
            print(f"Failed to stop recording: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")