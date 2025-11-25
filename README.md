# Tavily vs Traditional Search - RAG Quality Comparison Tool

A side-by-side comparison tool that demonstrates why Tavily's Search API is better for AI agents and RAG (Retrieval-Augmented Generation) applications than traditional search APIs.

### Technical Capabilities
- Real-time search comparison
- Token counting and metrics analysis
- RAG quality scoring
- Visual comparison of results

## Quick Start

### Prerequisites
- Python 3.8+
- Tavily API key

### Installation

1. **Clone or navigate to the project directory**
```bash
cd tavily
```

2. **Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
The `.env` file should already be configured with:
```
TAVILY_API_KEY=your_api_key_here
FLASK_ENV=development
FLASK_DEBUG=True
```

5. **Run the application**
```bash
python app.py
```

6. **Open in browser**
Navigate to: http://localhost:8080

## How to Use

1. Enter a search query (e.g., "Latest developments in transformer architectures")
2. Click "Compare Search Results"
3. View the side-by-side comparison:
   - **Left**: Tavily's extracted, RAG-ready content
   - **Right**: Traditional search snippets (and what you'd need to do)
4. Review the metrics and insights

