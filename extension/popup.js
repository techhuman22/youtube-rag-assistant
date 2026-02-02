document.addEventListener('DOMContentLoaded', function () {
    const askBtn = document.getElementById('askBtn');
    const questionInput = document.getElementById('questionInput');
    const chatContainer = document.getElementById('chat-container');
    const loader = document.getElementById('loader');

    // Function to append message to chat
    function appendMessage(text, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.classList.add('message');
        msgDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
        msgDiv.textContent = text;
        chatContainer.appendChild(msgDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    async function handleAsk() {
        const question = questionInput.value.trim();
        if (!question) return;

        appendMessage(question, 'user');
        questionInput.value = '';
        askBtn.disabled = true;
        loader.style.display = 'block';

        try {
            // Get current tab URL
            const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

            if (!tab || !tab.url.includes("youtube.com/watch")) {
                appendMessage("Please use this extension on a YouTube video page.", 'bot');
                loader.style.display = 'none';
                askBtn.disabled = false;
                return;
            }

            const urlParams = new URLSearchParams(new URL(tab.url).search);
            const videoId = urlParams.get('v');

            if (!videoId) {
                appendMessage("Could not find video ID.", 'bot');
                loader.style.display = 'none';
                askBtn.disabled = false;
                return;
            }

            // Call backend
            const response = await fetch('http://127.0.0.1:8000/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    video_id: videoId,
                    question: question
                })
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            const data = await response.json();
            appendMessage(data.answer, 'bot');

        } catch (error) {
            console.error(error);
            appendMessage("Error: Could not reach the backend locally. Make sure it's running on port 8000.", 'bot');
        } finally {
            loader.style.display = 'none';
            askBtn.disabled = false;
        }
    }

    askBtn.addEventListener('click', handleAsk);
    questionInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') handleAsk();
    });
});
