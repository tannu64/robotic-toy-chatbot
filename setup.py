from setuptools import setup, find_packages

setup(
    name="robotic-toy-chatbot",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A voice-enabled chatbot for a robotic toy with speech recognition, text-to-speech, and face recognition.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/robotic-toy-chatbot",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "SpeechRecognition==3.8.1",
        "PyAudio==0.2.11",
        "pyttsx3==2.90",
        "face_recognition==1.3.0",
        "opencv-python==4.5.5.64",
        "googletrans==4.0.0-rc1",
        "boto3==1.24.0",
        "PyYAML==6.0",
        "playsound==1.2.2",
        "pydub==0.25.1",
        "pytest==7.1.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "robotic-chatbot=src.main:main",
        ],
    },
)