
import requests
from bs4 import BeautifulSoup

def find_rss_feed(url):
    """
    Try to detect RSS feeds from a website URL.
    Returns a list of RSS feed URLs (could be empty if none found).
    """
    feeds = []
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.content, "html.parser")
        for link in soup.find_all("link", type="application/rss+xml"):
            href = link.get("href")
            if href:
                if href.startswith("http"):
                    feeds.append(href)
                else:
                    # Handle relative URLs
                    if url.endswith("/"):
                        feeds.append(url + href)
                    else:
                        feeds.append(url + "/" + href)
    except Exception:
        pass  # silently ignore errors
    return feeds
