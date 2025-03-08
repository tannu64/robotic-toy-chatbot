# Robotic Toy Chatbot

## Overview
This project is a **voice-enabled chatbot** designed for a **robotic toy**, integrating:
- **Speech Recognition** (Google/STT)
- **Text-to-Speech (TTS)** (pyttsx3/AWS Polly)
- **Face Recognition** (OpenCV & dlib)
- **Translation** (Google Translate/AWS Translate)
- **Chatbot Logic** (Delphi-based rules system)
- **AWS Cloud Logging** (S3/CloudWatch)

## Features
- **Real-time speech recognition** from microphone input.
- **AI-driven chatbot responses** powered by a Delphi-based logic system.
- **Face detection and recognition** for personalized interactions.
- **Multilingual support** via translation services.
- **AWS logging** to store interactions for analysis.

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/tannu64/robotic-toy-chatbot.git
cd robotic-toy-chatbot
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## Configuration
### Edit `config/dev_config.yaml` (for development) or `config/prod_config.yaml` (for production)
```yaml
speech_recognition:
  engine: "google"
  language_code: "en-US"

tts:
  engine: "pyttsx3"
  voice: "default"

face_recognition:
  enable: true
  known_faces_path: "./data/known_faces"
  camera_index: 0

translation:
  engine: "google"
  default_language: "en"

log_level: "DEBUG"
```

## Running the Chatbot
### 1. Start the Chatbot
```sh
python src/main.py
```
### 2. Run with a Specific Config File
```sh
python src/main.py config/prod_config.yaml
```

## Running Tests
```sh
pytest tests/
```

## File Structure
```
robotic-toy-chatbot/
├── README.md
├── requirements.txt
├── setup.py
├── config/
│   ├── dev_config.yaml
│   ├── prod_config.yaml
│   └── logging.conf
├── src/
│   ├── main.py
│   ├── chatbot/
│   ├── speech/
│   ├── vision/
│   ├── translation/
│   ├── aws_integration/
│   ├── delphi_integration/
│   └── utils/
├── tests/
└── Dockerfile (optional)
```

## Deployment
### Using Docker (Optional)
```sh
docker build -t robotic-chatbot .
docker run --rm -it robotic-chatbot
```

## Future Enhancements
- **NLP-powered chatbot** using Rasa or GPT-based AI.
- **Emotion detection** via facial expression analysis.
- **Integration with IoT** for robot movement & actions.

## License
This project is licensed under the **MIT License**.

## Contact
For any inquiries, contact **agapaitanveermou@gmail.com**.
