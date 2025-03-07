# Instagram Story Video Creator & Upload Automatically

This project allows you to record your desktop screen using OBS Studio, process the video to fit Instagram Stories (1080x1920 resolution), and speed it up to create a 15-second high-quality video suitable for Instagram.

---

## **Features**
- Record your desktop screen using OBS Studio.
- Automatically resize the video to Instagram Stories resolution (1080x1920).
- Speed up the video to fit within 15 seconds.
- Ensure high video quality with Instagram-compliant settings (8 Mbps bitrate, H.264 codec).

---

## **Prerequisites**

Before running the script, ensure you have the following installed:

1. **OBS Studio**:
   - Download and install OBS Studio from [https://obsproject.com/download](https://obsproject.com/download).

2. **Python**:
   - Download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).

3. **OBS WebSocket Plugin**:
   - The OBS WebSocket plugin is required for communication between the script and OBS Studio. Follow the steps below to enable it.

---

## **Setup OBS Studio**

1. **Enable WebSocket**:
   - Open OBS Studio.
   - Go to `Tools` > `WebSocket Server Settings`.
   - Enable the WebSocket server and set a password (e.g., `123456789`).
   - Click `Apply` and `OK`.

2. **Add Window Capture**:
   - In the `Sources` window, click the `+` button and select `Window Capture`.
   - Choose the window or application you want to record.

3. **Set Video Resolution**:
   - Go to `File` > `Settings` > `Video`.
   - Set both `Base (Canvas) Resolution` and `Output (Scaled) Resolution` to `1080x1920` (Instagram Stories resolution).

4. **Start Recording**:
   - Ensure OBS Studio is running and ready to record.

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ebrahimkhodadadi/MtScreenRecorder.git
   cd MtScreenRecorder
   ```

2. **Install Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, install the libraries manually:
   ```bash
   pip install obs-websocket-py moviepy
   ```

---

## **Usage**

1. **Run the Script**:
   - Execute the script using Python:
     ```bash
     python main.py
     ```

2. **Set Script Settings**:
   - When prompted, enter the following settings:
     - **OBS WebSocket Host**: `localhost` (or the IP address of the machine running OBS).
     - **OBS WebSocket Port**: `4444` (default port).
     - **OBS WebSocket Password**: The password you set in OBS WebSocket settings.

3. **Start Recording**:
   - The script will connect to OBS Studio and start recording.
   - After recording, it will process the video to fit Instagram Stories and save it as `instagram_video.mp4`.

---

## **Script Workflow**

1. **Connect to OBS**:
   - The script connects to OBS Studio via WebSocket.

2. **Start Recording**:
   - The script sends a command to OBS to start recording.

3. **Stop Recording**:
   - After a predefined duration (e.g., 30 seconds), the script stops the recording.

4. **Process Video**:
   - The recorded video is resized to 1080x1920 (Instagram Stories resolution).
   - The video is sped up to fit within 15 seconds.
   - The video is encoded with high-quality settings (8 Mbps bitrate, H.264 codec).

5. **Save Output**:
   - The processed video is saved as `instagram_video.mp4` in the current directory.

---

## **Configuration**

You can customize the script by modifying the following variables in `main.py`:

- **OBS WebSocket Settings**:
  ```python
  host = "localhost"  # Replace with the IP address of the machine running OBS
  port = 4444         # Default WebSocket port
  password = "123456789"  # Password set in OBS WebSocket settings
  ```

- **Video Processing Settings**:
  ```python
  target_duration = 15  # Target duration for the Instagram Story video (in seconds)
  ```

---

## **Output**

The processed video will be saved as `instagram_video.mp4` in the current directory. The video will:
- Have a resolution of 1080x1920 (Instagram Stories).
- Be sped up to fit within 15 seconds.
- Comply with Instagram's maximum bitrate limit (8 Mbps).

---

## **Troubleshooting**

1. **Connection Issues**:
   - Ensure OBS Studio is running and the WebSocket server is enabled.
   - Verify the host, port, and password in the script match the OBS WebSocket settings.

2. **Low Video Quality**:
   - Ensure the source video recorded by OBS is high quality.
   - Check the resolution and bitrate settings in OBS.

3. **File Not Found**:
   - Ensure the recorded `.mkv` file is in the same directory as the script.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contributing**

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## **Acknowledgments**

- [OBS Studio](https://obsproject.com/) for providing a powerful open-source recording tool.
- [obs-websocket-py](https://github.com/Elektordi/obs-websocket-py) for the Python WebSocket client.
- [MoviePy](https://zulko.github.io/moviepy/) for video processing.

---

Let me know if you need further assistance!