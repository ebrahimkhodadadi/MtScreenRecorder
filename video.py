import moviepy.editor as mp

def process_video(input_path, output_path, target_duration=15, bitratev=8000):
    """
    Process the video to fit Instagram Stories:
    - Scale to 1080x1920 (9:16 aspect ratio).
    - Speed up the video to fit within 15 seconds.
    - Compress the video.
    """
    try:
        print("Processing video...")

        # Load the video
        clip = mp.VideoFileClip(input_path)

        # Scale the video to Instagram Stories resolution (1080x1920)
        clip_resized = clip.resize(height=1920)

        # Calculate the speed factor to fit the video into 15 seconds
        speed_factor = clip_resized.duration / target_duration
        clip_sped_up = clip_resized.fx(mp.vfx.speedx, speed_factor)

        # Compress the video (optional: adjust bitrate for compression)
        # clip_sped_up.write_videofile(output_path, codec="libx264", bitrate=str(bitratev)+"k")
        clip_sped_up.write_videofile(
            output_path,
            codec="libx264",  # Use H.264 codec
            bitrate=str(bitratev)+"k",   # Set bitrate to 8 Mbps (Instagram's max limit)
            preset="slow",     # Use a slower preset for better compression/quality
            ffmpeg_params=["-crf", "18"]  # Lower CRF for higher quality
        )

        print(f"Video processed and saved to {output_path}.")
    except Exception as e:
        print(f"An error occurred while processing the video: {e}")