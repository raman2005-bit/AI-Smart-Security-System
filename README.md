AI-Powered Smart Security System 🛡️🤖
​A real-time security surveillance system built with Python, YOLOv8, and Telegram API. The system detects human intrusion, sends instant photo alerts to the owner, and enters a 'Locked' state until a remote reset command is received.
​🚀 Key Features
​Human Detection: Uses YOLOv8 (State-of-the-art Object Detection) to identify persons with high confidence.
​Instant Telegram Alerts: Sends a real-time notification and the captured intruder image directly to your Telegram bot.
​Remote Control: The system stays in a "Locked" state after an alert. It only resumes monitoring once the owner sends an "ok" command via Telegram.
​Optimized Performance: Implemented state management and request throttling to ensure a smooth 30+ FPS camera feed without network lag.
​Secure Configuration: Uses environment variables to protect sensitive API keys and tokens.
​🛠️ Tech Stack
​Language: Python 3.x
​Computer Vision: OpenCV, Ultralytics (YOLOv8)
​Communication: Telegram Bot API, Requests
​OS: Ubuntu / Linux (Optimized for embedded/edge devices)
​📁 Project Structure
.
├── main.py       # Main loop for detection and logic
├── telegram_handler.py    # Telegram API integration (Send/Receive)
├── config_manager.py      # File I/O for system state (Locked/Open)
├── status.txt             # Stores the current system state
└── .env        # (Hidden) Environment variables for API keys

Setup & Installation
Clone the repository:
git clone https://github.com/raman2005-bit/AI-Smart-Security-System.git
cd AI-Smart-Security-System

Install Dependencies:
pip install ultralytics opencv-python requests python-dotenv

Configure Environment Variables:
Create a .env file in the root directory and add your credentials:
TELEGRAM_TOKEN=your_bot_token_here
CHAT_ID=your_chat_id_here
IMGBB_API_KEY=your_imgbb_key_here

Run the System:
python3 main.py

How it Works
​The system continuously monitors the camera feed.
​If a person is detected, it captures a frame, sends it to Telegram, and writes "locked" to status.txt.
​In the locked state, the system stops detection to save CPU and waits for the user to reply with "ok" on Telegram.
​Once "ok" is received, the system resets to "open" and resumes monitoring.
