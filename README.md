# 📰 Elite News Scraper

A **dynamic, live news scraping tool** that fetches headlines from any website with RSS feeds and displays them in a **beautiful terminal dashboard**. Perfect for staying updated on multiple sources in real-time.

---

## Features ✨

- **Dynamic RSS Detection**: Enter any website URL, and the program automatically detects RSS feeds.  
- **Predefined Sources**: BBC, Reuters, CNN, NYTimes, The Guardian, Al Jazeera, TechCrunch, and more.  
- **Live Terminal Dashboard**: Displays news with progress bars, network status, and auto-refresh.  
- **Keyword Highlighting**: Highlight important words in headlines for quick scanning.  
- **Category Filtering**: Fetch news by category (World, Business, Tech, Sports, etc.) per source.  
- **Fallback Headlines**: Silently handles feeds with no entries — no error spam.  
- **Customizable Refresh & Headlines**: Set number of headlines per source and refresh interval.  

---

## Installation ⚙️

1. Clone the repository:

```bash
git clone https://github.com/MrV3nomous/news-scraper.git
cd news-scraper
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Requirements:
feedparser
requests
beautifulsoup4
rich


---

## Usage 🏃
Run the program:
Bash
Copy code
python news_scraper.py
Follow the prompts to:
Enter custom websites (optional).
Select news sources.
Choose categories per source.
Set the number of headlines per source.
Set refresh interval in seconds.
Optionally, provide keywords to highlight.
Press Ctrl+C to stop live scraping.

---

## Why This Project? 💡
Demonstrates web scraping, RSS feed handling, and real-time terminal dashboards.
Useful for monitoring multiple news sources in one place.
Great portfolio project for Python, network programming, and CLI tools.

---

## License 📜
This project is licensed under the MIT License.
