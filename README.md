<img src="./images/interview.png">

<!-- At first glance, the branding and messaging clearly conveys what to expect -->
<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rahulv91/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:vadisettyrahul@gmail.com)
</div>
<br />

# 🚀Quantum_Interview_AI

The **Quantum Interview AI** This innovative tool harnesses the power of artificial intelligence to support users during interviews by generating contextually accurate responses tailored to their resume and the interview questions. With a real-time teleprompter interface, users can seamlessly deliver their answers while maintaining eye contact with the interviewer, ensuring a confident and polished performance.

## ✨ Features

- **🤖 Multiple AI Model Integration**: Supports OpenAI GPT-4, Google Gemini, Meta LLaMA, Anthropic Claude, and Ollama create tailored responses based on the user's resume and interview questions. 
- **🎤 Speech Recognition**: Uses the Vosk speech recognition model to transcribe audio questions in real-time for seamless interaction.
- **📺 Teleprompter Interface**: A user-friendly GUI displays AI-generated responses clearly, helping users deliver answers confidently.
- **📄 Resume Parsing**: Extracts relevant information from the user's PDF resume to provide context for the AI's responses.
- **⌨️ Keyboard Control**: Enables users to pause and resume the application using keyboard shortcuts for greater control during practice sessions or live interviews.
- **🔩 User-Friendly Interface**: Simple command-line interface for selecting AI models and initiating the interview process.
## 🛠️ How It Works

1. **📑 Resume Data Extraction**: The application reads the user's resume and extracts key information to inform the response generation process.
2. **🗣️ Real-Time Question Transcription**: As the interviewer asks questions, the application listens and transcribes them using speech recognition technology.
3. **🧠 Contextual Response Generation**: The AI processes the transcribed question along with the resume data to generate a relevant response.
4. **📢 Display on Teleprompter**: The generated response is displayed on the teleprompter interface, enabling the user to read the answer while engaging with the interviewer.

## 🧩 Installation
### 📋 Prerequisites

- [Python 3.12.4 AND ABOVE](https://www.python.org/downloads/) installed on your system
- An [OpenAI API key](https://platform.openai.com/account/api-keys) (replace `"your_openai_api_key_here"` in the code with your actual API key)
### 🔐 Set Up AI Model APIs

#### **OpenAI GPT-4**

1. Sign up at [OpenAI](https://openai.com/) and obtain your API key.
2. Replace `"your_openai_api_key_here"` in the script with your actual API key.

#### **Google Gemini**

1. **Note:** As of my knowledge cutoff in September 2021, Google’s Gemini model details might be updated. Ensure you have access and obtain the necessary API keys or endpoints from [Google Cloud](https://cloud.google.com/).
2. Replace `"your_gemini_api_key_here"` and `"https://gemini-api.google.com/v1/generate"` with the actual API key and endpoint.

#### **Meta LLaMA**

1. Obtain access to **Meta's LLaMA** and set up the API endpoint as per [Meta's documentation](https://ai.facebook.com/blog/large-language-models-llama-meta-ai/).
2. Replace `"http://your_llama_api_endpoint_here"` with your actual LLaMA API endpoint.

#### **Anthropic Claude**

1. Sign up at [Anthropic](https://www.anthropic.com/) and obtain your API key.
2. Replace `"your_anthropic_api_key_here"` and `"https://api.anthropic.com/v1/complete"` with your actual API key and endpoint.

#### **Ollama**

1. Install **Ollama** by following the [Ollama Installation Guide](https://ollama.com/docs/installation).
2. Start the Ollama server to access the API. By default, Ollama runs on `http://localhost:11434`.
3. Replace `"http://localhost:11434/v1/chat/completions"` with your Ollama API endpoint if different.
- Vosk speech recognition model (download from [Vosk Models](https://alphacephei.com/vosk/models)
- Here’s a list of Vosk English speech recognition models and their system requirements:

### 1. **Lightweight English Models**
   - **Model size**: ~50 MB
   - **System requirements**:
     - **RAM**: Minimum 1 GB
     - **CPU**: Mid-range CPU (equivalent to Raspberry Pi or Android devices)
     - **Performance**: Suitable for real-time offline speech recognition on constrained devices【7†source】【8†source】.

### 2. **Large English Models for Quality listening**
   - **Model size**: 1.4 GB to 4.4 GB
   - **System requirements**:
     - **RAM**: 4 GB or more recommended
     - **CPU**: Multi-core processors
     - **Performance**: Designed for server environments with better accuracy but higher resource consumption【8†source】【9†source】.


## 🔧 Configuration

1. Open the `main.py` script in your preferred code editor.
2. Update the API keys and endpoints for each AI model as outlined in the [Installation](#installation) section.
3. Ensure the `vosk_model_path` is correctly set to the location of your downloaded Vosk model.
4. Place your resume in PDF format and update the `resume_path` variable in the `main.py` script to point to your resume file.
5. 
### 📦 Libraries

The application requires the following libraries:

- **Vosk**: For speech recognition
- **PyAudio**: For audio input and processing
- **OpenAI**: For interacting with the OpenAI API
- **PyPDF2**: For reading PDF files
- **Requests**: HTTP requests for API interactions
- **Tkinter**: For creating the GUI (included with Python)
- **Keyboard**: For detecting keyboard events

### 📄 Requirements File

The required libraries and their versions are listed in the `requirements.txt` file. You can install them using the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:

```
vosk==0.3.45
pyaudio==0.2.14
openai==1.37.1
PyPDF2==3.0.1
keyboard==0.13.5
```

### ▶️ Running the Application

You can run the application using one of the following methods:

#### 🔧 Method 1: Using a Virtual Environment

Creating a virtual environment is recommended to manage dependencies separately from your global Python installation.

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/{username}/Quantum_Interview_AI.git
   cd Quantum_Interview_AI
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:

   - **On Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS and Linux**:

     ```bash
     source venv/bin/activate
     ```

4. **Install the Required Libraries**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Download and Specify the Path for the Vosk Model**.

6. **Run the Application**:

   ```bash
   python main.py
   ```

7. **Deactivate the Virtual Environment** (after you're done):

   ```bash
   deactivate
   ```

#### ⚙️ Method 2: Normal Setup (Without Virtual Environment)

If you prefer to install the dependencies globally without using a virtual environment, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/{username}/Quantum_Interview_AI.git
   cd Quantum_Interview_AI
   ```

2. **Install the Required Libraries**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download and Specify the Path for the Vosk Model**.

4. **Run the Application**:

   ```bash
   python main.py
   ```
## 🤝 Contributing

Contributions are welcome! Whether it's improving documentation, suggesting new features, or fixing bugs, your input is valuable.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## 💼 Applications

The Quantum_Interview_AI can be utilized in various scenarios, including:

- **💼 Job Interviews**: Candidates can practice with the AI to prepare for real interviews, receiving tailored answers based on their resumes.
- **💻 Virtual Meetings**: During online meetings or webinars, users can ask questions and get immediate AI-generated responses to enhance their presentations.
- **🎤 Public Speaking**: Individuals can practice speeches and receive feedback on their delivery by reading AI-generated content.
- **🏢 Corporate Training**: New employees can use the tool for onboarding, helping them prepare for real-world interactions and interviews.

## 📝 Conclusion

The Quantum_Interview_AI with AI is a valuable tool for anyone looking to enhance their interview skills and communication abilities. By combining AI-generated responses with a teleprompter interface, it provides users with a unique and effective way to prepare for and navigate interviews confidently.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
