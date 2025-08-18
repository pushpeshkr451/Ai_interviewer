# AI Voice Interviewer 🎙️

[![Status](https://img.shields.io/badge/status-live-success.svg)](https://personal-ai-interviewer.onrender.com/) [![Live Demo](https://img.shields.io/badge/live_demo-online-brightgreen)](https://personal-ai-interviewer.onrender.com/)

An interactive web application that acts as an AI-powered mock interviewer. This tool analyzes your resume against a specific job role to conduct a realistic, voice-to-voice interview, helping you practice and improve your skills.

## 🚀 Live Demo

You can try the live application here:
**[https://personal-ai-interviewer.onrender.com/](https://personal-ai-interviewer.onrender.com/)**



***
## 📋 Features

-   **Personalized Question Generation**: The AI generates questions tailored to your resume and the target job role.
-   **Voice-to-Voice Interaction**: Conducts the entire interview through your microphone and speakers using the browser's Web Speech API.
-   **Resume Analysis**: Extracts text from your uploaded PDF resume to understand your skills and experience.
-   **Multi-User Safe**: Uses server-side sessions to manage separate conversations for each user.
-   **Easy Deployment**: Configured for straightforward deployment on cloud platforms like Render.

***
## 🛠️ Technology Stack

-   **Backend**: Python, Flask
-   **AI Engine**: Google Gemini API (`google-generativeai`)
-   **PDF Parsing**: PyPDF2
-   **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
-   **Web Server**: Gunicorn (for production)

***
## ⚙️ Setup and Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/pushpeshkr451/Ai_interviewer.git](https://github.com/pushpeshkr451/Ai_interviewer.git)
cd Ai_interviewer
