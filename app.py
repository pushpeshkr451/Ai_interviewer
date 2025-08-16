from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import PyPDF2
import io

app = Flask(__name__)

# --- Global Objects ---
# These are initialized to None and will be set after the user provides a valid API key.
model = None
chat = None

@app.route('/configure_key', methods=['POST'])
def configure_key():
    """
    Receives an API key from the browser, verifies it by making a test call,
    and initializes the global 'model' object for the server session.
    """
    global model
    api_key = request.json.get('apiKey')
    if not api_key:
        return jsonify({'error': 'No API key provided'}), 400
    
    try:
        # Configure the genai library with the user-provided key.
        genai.configure(api_key=api_key)
        
        # Create a model instance for a quick, cheap test call to validate the key.
        temp_model = genai.GenerativeModel('gemini-1.5-flash-latest')
        temp_model.generate_content("test")
        
        # If the test call succeeds, assign the validated model to the global variable.
        model = temp_model
        print("Gemini API key configured successfully.")
        return jsonify({'success': True})
    except Exception as e:
        print(f"Failed to configure Gemini API: {e}")
        return jsonify({'error': f'Invalid API key or configuration error: {e}'}), 400

@app.route('/')
def index():
    """Renders the main single-page application."""
    return render_template('index.html')

@app.route('/start_interview', methods=['POST'])
def start_interview():
    """
    Initializes a new interview chat session based on the uploaded resume and job role.
    This endpoint relies on the global 'model' object being configured first.
    """
    global chat, model

    if not model:
        return jsonify({'error': 'API key not configured. Please set the key first.'}), 500

    if 'resume' not in request.files:
        return jsonify({'error': 'No resume file provided'}), 400
    
    resume_file = request.files['resume']
    job_role = request.form.get('job_role', 'Not provided')
    
    resume_text = extract_text_from_pdf(resume_file)
    if resume_text is None:
        return jsonify({'error': 'Could not read text from PDF.'}), 500

    # This initial prompt provides the context for the entire interview.
    initial_prompt = f"""
    You are an expert AI interviewer. Your task is to conduct an interview for the job role of '{job_role}'.
    You have been given the candidate's resume below.
    ---
    RESUME: {resume_text}
    ---
    Analyze the resume against the job role. Start the interview by greeting the candidate and asking your first insightful question.
    Keep your responses concise and conversational. Just ask the first question.
    """
    
    # Start a new chat session, wiping any previous history.
    chat = model.start_chat(history=[])
    response = chat.send_message(initial_prompt)
    
    return jsonify({'reply': response.text})

@app.route('/send_message', methods=['POST'])
def send_message():
    """Handles a single conversational turn in an ongoing interview."""
    global chat
    if not chat:
        return jsonify({'error': 'Interview not started'}), 400

    user_message = request.json['message']
    
    try:
        response = chat.send_message(user_message)
        ai_message = response.text
    except Exception as e:
        ai_message = f"An error occurred: {e}"

    return jsonify({'reply': ai_message})

def extract_text_from_pdf(pdf_file):
    """A helper function to extract all text from an uploaded PDF file."""
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.read()))
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None