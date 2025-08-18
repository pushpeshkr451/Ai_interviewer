# AI Interviewer

### 🔴 [Try the Live Demo Here!](https://personal-ai-interviewer.onrender.com/) 🔴

An interactive, voice-powered interview simulator that leverages Google's Gemini API to conduct realistic job interviews based on a user's resume.

## Description

This web application provides a platform for users to practice their interview skills in a simulated environment. A user uploads their resume, specifies the job role they are applying for, and the AI, powered by the Gemini 1.5 Flash model, initiates and conducts a voice-based interview. The AI's questions are tailored to the candidate's resume and the specified job role, providing a highly relevant and personalized experience. The application uses the Web Speech API for voice recognition and text-to-speech, allowing for a hands-free, conversational interview flow.

***

## 🚀 Features

* **AI-Powered Interviews**: Utilizes Google's Gemini API to generate insightful and relevant interview questions.
* **Resume Analysis**: The AI analyzes the user's uploaded PDF resume to tailor the interview questions.
* **Job Role Specific**: The interview is customized for the specific job role entered by the user.
* **Voice-to-Text**: Captures the user's spoken answers and converts them to text using the browser's SpeechRecognition API.
* **Text-to-Speech**: The AI's responses are spoken back to the user, creating a natural conversational flow.
* **Secure API Key Handling**: API keys are stored in the browser's local storage and are not exposed on the client-side after initial configuration.

***

## 🛠️ Installation and Setup

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/ai-interviewer.git](https://github.com/your-username/ai-interviewer.git)
    cd ai-interviewer
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    Create a `requirements.txt` file with the following content:
    ```
    Flask
    google-generativeai
    PyPDF2
    ```
    Then, run the installation command:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Get your Gemini API Key:**
    * Visit the [Google AI for Developers](https://ai.google.dev/) website.
    * Create an API key in the Google AI Studio.

5.  **Run the Flask application:**
    ```bash
    flask run
    ```

6.  **Open the application in your browser:**
    * Navigate to `http://127.0.0.1:5000`

***

## 📋 How to Use

1.  **Enter your API Key**: The first time you open the application, you will be prompted to enter your Gemini API key. This key is stored in your browser's local storage for future use.
2.  **Setup the Interview**:
    * Enter the job role you are interviewing for in the "Job Role" text area.
    * Upload your resume in PDF format.
    * Click the "Start Interview" button.
3.  **The Interview**:
    * The AI will greet you and ask the first question.
    * Click the **🎤 Start Recording** button to begin answering. The button will turn red, indicating that it is recording.
    * Speak your answer clearly.
    * Click the **🛑 Stop Recording** button when you have finished your answer.
    * Your answer will appear in the chat, followed by the AI's next question.

***

## 💻 Technologies Used

* **Backend**:
    * [Flask](https://flask.palletsprojects.com/): A lightweight WSGI web application framework in Python.
    * [Google Generative AI (Gemini)](https://ai.google.dev/): The core AI model used for generating interview questions and responses.
    * [PyPDF2](https://pypdf2.readthedocs.io/): A library for reading and extracting text from PDF files.

* **Frontend**:
    * **HTML5**
    * **CSS3**
    * **JavaScript**
    * [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API): For speech-to-text and text-to-speech functionality.
