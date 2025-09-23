# alferd-voice-assistant
A versatile, open-source voice assistant designed to simplify user interactions and boost productivity with hands-free computing.
Alferd is a modular, voice-controlled desktop assistant for Windows. It can automate apps, control system settings, fetch news, play music, take notes, and much more—all with your voice.

## Features

- Voice-controlled commands (using your microphone)
- Battery status reporting
- WiFi enable/disable (Windows only)
- Open standard Windows apps (Notepad, Calculator, Camera, etc.)
- Date and time reporting
- Web automation (Gmail, GitHub, Google, LinkedIn, YouTube, Instagram)
- Google and YouTube search by voice
- Brightness and volume control
- Spotify automation (play, pause, search)
- WhatsApp automation (send message, call)
- News headlines (via NewsAPI)
- Note-taking (take, read, clear notes)
- Fallback to OpenAI for smart responses

## Tech Stack

- **Python 3.8+**
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) (for GUI)
- [pyttsx3](https://pypi.org/project/pyttsx3/) (text-to-speech)
- [speech_recognition](https://pypi.org/project/SpeechRecognition/) (voice recognition)
- [psutil](https://pypi.org/project/psutil/) (battery status)
- [screen-brightness-control](https://pypi.org/project/screen-brightness-control/) (brightness control)
- [pycaw](https://pypi.org/project/pycaw/) (volume control)
- [openai](https://pypi.org/project/openai/) (OpenAI API)
- [requests](https://pypi.org/project/requests/) (API calls)
- [word2number](https://pypi.org/project/word2number/) (word to number conversion)
- [comtypes](https://pypi.org/project/comtypes/) (Windows COM interface)
- [Pillow](https://pypi.org/project/Pillow/) (image handling)
- [PyInstaller](https://pyinstaller.org/) (for packaging)
- Other custom modules: `spotify`, `whatsapp`, etc.


## Planned Features

- Weather updates
- Calendar integration
- More system controls (e.g., Bluetooth, airplane mode)
- More automation features


## Future Improvements

- Advanced Voice Recognition: Migrate the voice recognition engine to a more accurate, state-of-the-art solution like Vosk or a cloud-based API to improve command accuracy.

- Expanded Functionality: Add support for more applications, implement a to-do list, or enable calendar management.

- Standalone Application: Package the project into a standalone executable file so that users can run it without needing to install Python or other dependencies.

- Enhanced UI/UX: Introduce a more minimalistic, floating widget UI and add visual feedback to show when the assistant is actively listening.


---

## Acknowledgements

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [OpenAI](https://openai.com/)
- [NewsAPI](https://newsapi.org/)
- [PyCaw](https://github.com/AndreMiras/pycaw)
- [screen-brightness-control](https://github.com/CoffeePanda0/screen-brightness-control)
- And all open-source contributors!

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/alferd-voice-assistant.git
cd alferd-voice-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API keys

Create a file named `config.json` in the project folder:

```json
{
  "OPENAI_API_KEY": "your_openai_key_here",
  "NEWS_API_KEY": "your_newsapi_key_here"
}
```

- Get your [OpenAI API key](https://platform.openai.com/account/api-keys)
- Get your [NewsAPI key](https://newsapi.org/)

### 4. Run the assistant

```bash
python user.py
```

## Usage

- Say "Alfred" to activate the assistant.
- Speak your command (e.g., "open notepad", "tell date and time", "change brightness", "open spotify", "take note", etc.).
- For unrecognized commands, the assistant can use OpenAI to help (with your permission).

## Notes

- **Network required:** Recognition and some APIs require internet access.
- **Windows only:** Some features (WiFi, app opening, volume, brightness) are Windows-specific.
- **Microphone required:** Make sure your microphone is working.
- **Admin rights:** WiFi control may require running as administrator.
- **Notes:** Saved in `notes.txt` in the project folder.
- **API keys:** Never share your `config.json` publicly.

## Packaging

You can package the assistant as an executable using [PyInstaller](https://pyinstaller.org/):

```bash
pyinstaller --onefile user.py
```

Make sure to include `config.json` in the same directory as the executable.

## Contributing

Pull requests and suggestions are welcome!

## License

[MIT License](LICENSE)

---

**If you have any questions or issues, please open an issue on GitHub.**