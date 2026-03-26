# Polish Case Visualizer 🇵🇱 <-> 🇬🇧

An AI-powered web application designed to help learners visualize Polish grammatical cases. Using Gemini 2.5 Flash, the tool color-codes text to identify inflections and provides detailed grammatical explanations on hover.

## Features
- **Real-time Analysis**: Color-codes all 7 Polish cases (Nominative, Genitive, Dative, Accusative, Instrumental, Locative, and Vocative).
- **Grammar Insights**: Provides the base nominative form and a brief explanation of the inflection (e.g., consonant shifts).
- **Persistence**: A sidebar tracks your last 10 analyzed sentences using browser local storage.
- **PDF Export**: Generate a clean PDF of your analyzed text for study notes.
- **Linux Optimized**: Includes specific networking overrides to prevent gRPC/IPv6 timeout hangs on Fedora and similar distributions.

## Tech Stack
- **Backend**: Python, Flask, Google GenAI SDK.
- **Frontend**: Vanilla JS, HTML5, CSS3.
- **AI Model**: Gemini 2.5 Flash.

## Project Structure
- **app.py**: Flask backend with Gemini AI integration and IPv4 network fixes.
- **index.html**: Single-page frontend with sidebar history and PDF generation.
- **uv.lock & pyproject.toml**: Deterministic dependency tracking.
- **requirements.txt**: Universal dependency list for pip compatibility.

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/github9000/polish-case-visualizer
   cd polish-case-visualizer

2. **Configure Environment Variables**:
   Create a .env file in the root directory and add your API key:
   ```bash
   GEMINI_API_KEY=your_api_key_here   

3. **Install dependencies**:

   Option A: Using uv (Recommended)
   If you have uv installed, this will sync your environment exactly with the uv.lock file:
   ```bash
   uv sync

   Option B: Using standard pip
   If you prefer standard Python tools, use the generated requirements file:
   ```bash
   pip install -r requirements.txt


4. **Run the application**:
   ```bash
   # If using uv
   uv run python app.py

   # If using standard python
   python app.py

Access the app at http://127.0.0.1:5000


