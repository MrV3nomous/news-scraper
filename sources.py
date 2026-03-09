# sources.py
"""
This file contains all the news sources and their RSS feeds.
You can add new sources easily here without touching the main program.
"""

NEWS_SOURCES = {
    "BBC": {"rss": "http://feeds.bbci.co.uk/news/rss.xml", "categories": ["World", "Business", "Tech", "Science"]},
    "Reuters": {"rss": "http://feeds.reuters.com/Reuters/worldNews", "categories": ["World", "Business", "Technology", "Sports"]},
    "CNN": {"rss": "http://rss.cnn.com/rss/edition.rss", "categories": ["World", "US", "Tech", "Entertainment"]},
    "NYTimes": {"rss": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", "categories": ["World", "Business", "Technology", "Science"]},
    "The Guardian": {"rss": "https://www.theguardian.com/world/rss", "categories": ["World", "US", "Tech", "Culture"]},
    "Al Jazeera": {"rss": "https://www.aljazeera.com/xml/rss/all.xml", "categories": ["World", "Middle East", "Africa"]},
    "TechCrunch": {"rss": "http://feeds.feedburner.com/TechCrunch/", "categories": ["Startups", "Apps", "Gadgets"]},
}

# Fallback headlines if a feed fails
FALLBACK_HEADLINES = [
    "Breaking: Example headline 1",
    "Update: Example headline 2",
    "Top story: Example headline 3"
]
