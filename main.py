import os
import json
import time
import keyboard
import threading
import tkinter as tk
from vosk import Model, KaldiRecognizer
import pyaudio
import openai
import PyPDF2
import requests

# Set your API Keys for respective models
openai.api_key = "your_openai_api_key_here"
anthropic_api_key = "your_anthropic_api_key_here"
gemini_api_key = "your_gemini_api_key_here"
llama_endpoint = "http://your_llama_api_endpoint_here"  # Replace with LLaMA API endpoint
ollama_endpoint = "http://localhost:11434/v1/chat/completions"  # Default Ollama endpoint

# Vosk model setup (update the path to your downloaded model)
vosk_model_path = "path_to_vosk_model_directory"

# Initialize Vosk Speech Recognition model
if not os.path.exists(vosk_model_path):
    print(f"Please download the model from https://alphacephei.com/vosk/models and unpack as '{vosk_model_path}'")
    exit(1)

model = Model(vosk_model_path)
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Function to stop and clear the recording
def stop_and_clear_recording():
    global stream
    if stream.is_active():
        stream.stop_stream()
        stream.close()

# Teleprompter: Floating window class
class Teleprompter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Advanced Interview Responder with AI")
        self.root.geometry("1100x600")
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.6)  # Slight transparency
        self.root.resizable(True, True)

        # Dropdown menu for selecting the model
        self.model_var = tk.StringVar(self.root)
        self.model_var.set("OpenAI GPT-4")  # Default model
        self.models = ["OpenAI GPT-4", "Google Gemini", "Meta LLaMA", "Anthropic Claude", "Ollama"]
        self.model_menu = tk.OptionMenu(self.root, self.model_var, *self.models)
        self.model_menu.pack(pady=10)

        # Text widget for displaying responses
        self.text_widget = tk.Text(self.root, wrap='word', font=("Arial", 20), bg="black", fg="white", padx=10, pady=10)
        self.text_widget.configure(state="disabled")
        self.text_widget.pack(expand=True, fill='both')
        self.root.update()

    def update_text(self, response_text):
        self.text_widget.configure(state="normal")
        self.text_widget.delete(1.0, tk.END)  # Clear previous text
        self.text_widget.insert(tk.END, response_text)  # Insert new text
        self.text_widget.configure(state="disabled")
        self.root.update()

    def get_selected_model(self):
        return self.model_var.get()

# Resume Parsing Function
def extract_resume_data(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        resume_text = ""
        for page in reader.pages:
            resume_text += page.extract_text()
    return resume_text

# Get response from different AI models
def get_response(prompt, resume_context, selected_model):
    model_mapping = {
        "OpenAI GPT-4": get_response_from_openai,
        "Google Gemini": get_response_from_google,
        "Meta LLaMA": get_response_from_meta,
        "Anthropic Claude": get_response_from_anthropic,
        "Ollama": get_response_from_ollama
    }
    response_function = model_mapping.get(selected_model, lambda *_: "Selected model is not available.")
    return response_function(prompt, resume_context)

# API call functions for each model
def get_response_from_openai(prompt, resume_context):
    full_prompt = f"Respond as if you were me. The question is:\n{prompt}\n\nMy Resume information: {resume_context}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": full_prompt}],
            max_tokens=60,
            n=1,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error with OpenAI GPT-3.5-turbo: {e}"

def get_response_from_google(prompt, resume_context):
    full_prompt = f"Respond as if you were me. The question is:\n{prompt}\n\nMy Resume information: {resume_context}"
    try:
        headers = {"Authorization": f"Bearer {gemini_api_key}"}
        data = {"prompt": full_prompt}
        response = requests.post("https://gemini-api.google.com/v1/generate", headers=headers, json=data)
        response.raise_for_status()
        return response.json().get("text", "Sorry, I couldn't process that.")
    except Exception as e:
        return f"Gemini API Error: {e}"

def get_response_from_meta(prompt, resume_context):
    full_prompt = f"Respond as if you were me. The question is:\n{prompt}\n\nMy Resume information: {resume_context}"
    try:
        headers = {"Content-Type": "application/json"}
        data = {"prompt": full_prompt}
        response = requests.post(llama_endpoint, headers=headers, json=data)
        response.raise_for_status()
        return response.json().get("generated_text", "Sorry, I couldn't process that.")
    except Exception as e:
        return f"LLaMA API Error: {e}"

def get_response_from_anthropic(prompt, resume_context):
    full_prompt = f"Respond as if you were me. The question is:\n{prompt}\n\nMy Resume information: {resume_context}"
    try:
        headers = {"x-api-key": anthropic_api_key}
        data = {"prompt": full_prompt, "max_tokens_to_sample": 150}
        response = requests.post("https://api.anthropic.com/v1/complete", headers=headers, json=data)
        response.raise_for_status()
        return response.json().get("completion", "Sorry, I couldn't process that.")
    except Exception as e:
        return f"Anthropic API Error: {e}"

def get_response_from_ollama(prompt, resume_context):
    full_prompt = f"Respond as if you were me. The question is:\n{prompt}\n\nMy Resume information: {resume_context}"
    try:
        headers = {"Content-Type": "application/json"}
        data = {
            "model": "llama-7b",  # Specify the model name as configured in Ollama
            "prompt": full_prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        response = requests.post(ollama_endpoint, headers=headers, json=data)
        response.raise_for_status()
        return response.json().get("choices", [{}])[0].get("text", "Sorry, I couldn't process that.")
    except Exception as e:
        return f"Ollama API Error: {e}"

# Speech Recognition with Vosk
def transcribe_audio():
    print("Listening for questions...")
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result).get("text", "")
            if text:
                print(f"Transcribed text: {text}")
                return text

# Pause and resume mechanism
pause_event = threading.Event()

def toggle_pause_resume():
    if pause_event.is_set():
        print("Resuming bot...")
        pause_event.clear()
    else:
        print("Pausing bot...")
        pause_event.set()

def listen_for_keyboard():
    keyboard.on_press(lambda _: toggle_pause_resume(), lambda _: stop_and_clear_recording())
    keyboard.wait()  # Keep the listener active

# Main interview process
def start_interview():
    resume_path = "path_to_resume.pdf"  # Update with your resume path
    resume_data = extract_resume_data(resume_path)
    teleprompter = Teleprompter()
    
    while True:
        question = transcribe_audio()
        if question:
            selected_model = teleprompter.get_selected_model()
            response = get_response(question, resume_data, selected_model)
            print(f"Generated response: {response}")
            teleprompter.update_text(response)
        time.sleep(1)

if __name__ == "__main__":
    # Start the keyboard listener in a separate thread
    keyboard_thread = threading.Thread(target=listen_for_keyboard)
    keyboard_thread.daemon = True
    keyboard_thread.start()

    # Start the interview process
    start_interview()