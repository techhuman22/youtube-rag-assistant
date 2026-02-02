# YouTube RAG Assistant

A Chrome Extension and FastAPI backend that allows you to chat with YouTube videos using RAG (Retrieval-Augmented Generation). It fetches the transcript of a video, indexes it, and lets you ask questions about the content, powered by Llama 3 via Groq.

## Features

-   **Video Summarization & Q&A**: Ask any question about a YouTube video.
-   **RAG Architecture**: Uses FAISS for vector storage and retrieval to find relevant transcript sections.
-   **Fast Inference**: Powered by Groq's LPU inference engine with `llama-3.3-70b-versatile`.
-   **Chrome Extension**: Simple popup interface to use directly on YouTube video pages.

## Tech Stack

-   **Backend**: Python, FastAPI, Uvicorn
-   **AI/LLM**: LangChain, Groq (Llama 3), HuggingFace Embeddings (`all-mpnet-base-v2`)
-   **Vector Database**: FAISS (Facebook AI Similarity Search)
-   **Frontend**: HTML, CSS, JavaScript (Chrome Extension)

## Prerequisites

-   Python 3.10+
-   A [Groq API Key](https://console.groq.com/keys)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/techhuman22/youtube-rag-assistant.git
cd youtube-rag-assistant
```

### 2. Backend Setup
1.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    # Mac/Linux
    source .venv/bin/activate
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Configuration**:
    Create a `.env` file in the root directory and add your Groq API key:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

4.  **Run the Server**:
    ```bash
    python app.py
    ```
    The backend will start at `http://127.0.0.1:8000`.

### 3. Chrome Extension Setup
1.  Open Chrome and navigate to `chrome://extensions/`.
2.  Enable **Developer mode** (toggle in the top right).
3.  Click **Load unpacked**.
4.  Select the `extension` folder from this repository.

## Usage

1.  Ensure the backend server is running (`python app.py`).
2.  Go to any YouTube video.
3.  Click the **YT RAG Assistant** extension icon in your browser toolbar.
4.  Type your question (e.g., "Summarize this video" or "What does he say about X?").
5.  Wait a moment for the AI to process the transcript and generate an answer.

## Troubleshooting

-   **Server Error / Connection Refused**: Ensure the backend is running on port 8000. If port 8000 is occupied, you may need to kill the process or change the port in `app.py` and `popup.js`.
-   **No Captions Available**: The tool relies on YouTube transcripts. If a video has no captions/transcripts, it cannot answer questions.
-   **LangChain Warnings**: You might see warnings about deprecated classes; these usually do not affect functionality but can be fixed by upgrading packages as suggested in the warning logs.

## Project Structure

```
├── app.py              # FastAPI application entry point
├── config.py           # Configuration and LLM setup
├── rag_pipeline.py     # LangChain RAG pipeline definition
├── transcript.py       # Helper to fetch YouTube transcripts
├── vectorstore.py      # Vector store creation (FAISS)
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed)
└── extension/          # Chrome Extension files
    ├── manifest.json
    ├── popup.html
    ├── popup.js
    └── styles.css
```
