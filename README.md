# StackOverflow Helper Agent 🤖

An AI-powered assistant that searches StackOverflow and provides intelligent summaries of programming solutions using Google's Gemini AI.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Chainlit](https://img.shields.io/badge/Chainlit-Latest-green.svg)
![Google AI](https://img.shields.io/badge/Google_AI-Gemini-red.svg)

## 🌟 Features

- **🔍 Smart Search**: Searches StackOverflow using Google's Custom Search API
- **🤖 AI Summarization**: Uses Google Gemini AI to provide clear, concise explanations
- **💬 Interactive Chat**: Beautiful web interface powered by Chainlit
- **📚 Direct Links**: Provides links to original StackOverflow posts
- **⚡ Real-time**: Fast responses with live search results

## 🚀 Demo

Ask questions like:
- "How to reverse a string in Python?"
- "What's the difference between let and const in JavaScript?"
- "How to connect to MySQL database in Node.js?"
- "React useEffect cleanup function"

## 📋 Prerequisites

- Python 3.8 or higher
- Google Custom Search API key
- Google Gemini API key
- Google Custom Search Engine ID

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ahmed-KHI/stackoverflow-helper-agent.git
   cd stackoverflow-helper-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```

4. **Configure your API keys in `.env`**:
   - Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Get your Google Custom Search API key from [Google Cloud Console](https://console.cloud.google.com/)
   - Create a Custom Search Engine at [Google CSE](https://cse.google.com/)

## ⚙️ Configuration

### Google Custom Search Engine Setup

1. Go to [Google Custom Search Engine](https://cse.google.com/)
2. Click "Add" to create a new search engine
3. In "Sites to search", add: `stackoverflow.com`
4. Click "Create"
5. Copy your Search Engine ID
6. Add it to your `.env` file

### API Keys Setup

```env
# Your Google Gemini API key
GEMINI_API_KEY=your_gemini_api_key_here

# Your Google Custom Search API key
GOOGLE_SEARCH_API_KEY=your_google_search_api_key_here

# Your Custom Search Engine ID
GOOGLE_CSE_ID=your_custom_search_engine_id_here
```

## 🚀 Usage

1. **Start the application**
   ```bash
   chainlit run main.py
   ```

2. **Open your browser** to `http://localhost:8000`

3. **Start asking questions!** Type any programming question and get instant answers.

## 📁 Project Structure

```
stackoverflow-helper-agent/
├── main.py                 # Main Chainlit application
├── search_stackoverflow.py # Google Custom Search integration
├── gemini_helper.py       # Google Gemini AI integration
├── requirements.txt       # Python dependencies
├── chainlit.md           # Chainlit welcome screen
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🧩 How It Works

1. **User Input**: User types a programming question in the chat interface
2. **Search**: The app searches StackOverflow using Google Custom Search API
3. **Results**: Retrieves relevant StackOverflow posts with titles, snippets, and links
4. **AI Summary**: Google Gemini AI analyzes the results and provides a clear summary
5. **Response**: User receives both the original results and the AI-generated summary

## 🔧 Dependencies

- `chainlit` - Web interface framework
- `google-generativeai` - Google Gemini AI integration
- `requests` - HTTP requests for API calls
- `python-dotenv` - Environment variable management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Chainlit](https://chainlit.io/) for the amazing chat interface framework
- [Google AI](https://ai.google.dev/) for the Gemini AI model
- [StackOverflow](https://stackoverflow.com/) for being the best programming Q&A platform

## 📞 Support

If you have any questions or issues, please [open an issue](https://github.com/Ahmed-KHI/stackoverflow-helper-agent/issues) on GitHub.

---

Made with ❤️ by [Muhammad Ahmed]
