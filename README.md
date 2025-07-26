#Voice Coding

A simple, student-friendly Python project that lets you convert your voice to text using your computer’s microphone—all in one file!
Perfect for beginners learning speech-to-text or Python audio programming.

🎤 Features
Record your voice: Press Enter and speak into your mic.

Speech-to-text: Your spoken words are transcribed using Google’s free speech recognition API.

Easy to use: No programming experience needed; just install a couple of packages and run.

Cross-platform: Works on Windows, Mac, and Linux. (For best results, run on your local laptop/PC with a microphone.)

🛠️ How to Set Up
1. Clone/download this repository
bash
git clone https://github.com/Govardhana23/voicecoding.git
cd voicecoding
2. Install dependencies
You'll need Python 3.x.
Install the required Python packages in your terminal:

bash
pip install speechrecognition pyaudio
Note:
If you get any errors installing PyAudio, see the Troubleshooting section at the bottom!

🚀 How to Use
Run the script:

bash
python voice_to_text_student.py
Follow the prompt:

Press Enter when ready, and then speak clearly into your microphone.

See the result:

The program prints what you said as text in the terminal.

If it didn’t understand you, try again or speak more clearly.

🌀 Troubleshooting
"No Default Input Device Available"

Your computer or environment does not have a microphone or cannot access it.

Make sure you are running this code on your own laptop or desktop (not Codespaces or cloud services).

Check that your mic is plugged in and recognized by your OS.

PyAudio install errors:

On Windows: Try installing with pip install pipwin then pipwin install pyaudio.

On Ubuntu/Debian Linux:

bash
sudo apt-get install portaudio19-dev python3-dev
pip install pyaudio
Google Speech API errors:

Make sure you are connected to the internet (SpeechRecognition uses Google’s free online service).
