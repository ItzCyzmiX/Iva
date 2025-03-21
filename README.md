# 🤖 Iva - AI-Powered Copilot

Iva is an intelligent code assistant that helps you generate file structures and boilerplate code based on natural language descriptions.

## ✨ Features

-   Natural language processing for code generation
-   Interactive command-line interface with rich formatting
-   Progress indicators and visual feedback
-   Flexible output directory selection
-   Cross-platform compatibility

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/iva.git
cd iva
```

### 2. Setup the env variables

Iva uses [groq](https://groq.com), so you will need an api key.
To get you api key head over to [groq's console](https://console.groq.com/key) and create a new key, one the key is created paste into the GROQ_API_KEY (between the double quotes) ```example.env```file
and rename that file to ```.env```

PS: DONT CHANGE THE NAME OF THE ENV VARIABLE (GROQ_API_KEY)!

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 💻 Usage

### Run the main script:

```bash
python main.py
```

### Then follow the interactive prompts:

1. Enter your request in natural language
2. Specify the output directory (or press Enter for current directory)
3. Wait for the generation process to complete

## 📝 Example

```bash
What would you like me to do? Create a basic Flask API with authentication
Output directory: ./my_project
✅ Files generated successfully!
```
