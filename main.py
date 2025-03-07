import time
import os

import questionary
from config import Configure
from instagram import InstagramBot
from obs import Obs
from metatrader import MetaTrader
from utils import *
from video import *
from pyfiglet import Figlet

def monitor_trades(obs, insta_bot, mt, symbol, quality):
    """Monitor open trades in MetaTrader 5 and trigger recording."""
    obs.connect_to_obs()

    if insta_bot.login() == False:
        print("Failed to initialize Instagram.")
        return
    
    # Initialize MetaTrader 5
    if mt.Login() == False:
        print("Failed to initialize MetaTrader 5.")
        return
    
    try:
        print("Wait until find new positions")
        
        while True:
            positions = mt.get_open_positions(symbol=symbol)
            if positions is None or len(positions) == 0:
                time.sleep(1)
                continue
            ticket_id=positions[0].ticket

            # Start recording in OBS
            record_result = obs.start_recording()
            if record_result == False:
                continue
            
            while True:
                positions = mt.get_open_positions(ticket_id=ticket_id)
                if positions is None or len(positions) == 0:
                    break
                time.sleep(1)
                
            obs.stop_recording()
            
            # Capture screenshot
            # capture_screenshot()
            
            ## Resize recorded video
            # Find the recorded .mkv file
            time.sleep(3)
            input_video_path = find_mkv_file()
            output_video_path = os.path.join(os.getcwd(), str(ticket_id)+".mp4")
            if input_video_path:
                print(f"Found .mkv file: {input_video_path}")
                output_video_path = output_video_path  # Save in the current directory
                process_video(input_video_path, output_video_path, bitratev=quality)
            else:
                print("No .mkv file found in the current directory.")
                
            insta_bot.upload_story(output_video_path)
            
            time.sleep(2)
            delete_files_with_retry(input_video_path, output_video_path, output_video_path+".jpg")
            
    except KeyboardInterrupt:
        print("Stopping monitoring...")
    # finally:
    #     mt.shutdown()
    #     obs.disconnect()


def main():
    """Check if config exists; prompt user to edit or run the app."""
    config_manager = Configure()
    config = config_manager.get_config_value  # Function to fetch settings

    if not config_manager.config:
        print("No configuration found. Setting up for the first time...\n")
        config_manager.configure()

    choice = questionary.select(
        "What do you want to do?",
        choices=["Run the App", "Edit Configuration", "Exit"]
    ).ask()

    if choice == "Edit Configuration":
        config_manager.configure()
        main()
    elif choice == "Run the App":
        # Load OBS settings
        obs = Obs(
            host=config("obs_host"),
            port=int(config("obs_port")),
            password=config("obs_password")
        )

        insta_bot = InstagramBot(
            username=config("insta_username"),
            password=config("insta_password")
        )
        
        mt = MetaTrader(
            path=config("mt_path"),
            server=config("mt_server"),
            user=int(config("mt_user")),
            password=config("mt_password"),
        )
        symbol = config("mt_symbol")
        quality = config("video_quality")
        monitor_trades(obs, insta_bot, mt, symbol, quality)
    else:
        print("Exiting...")

if __name__ == "__main__":
    f = Figlet(font='slant')
    print(f.renderText('Mt Recorder'))
    
    main()