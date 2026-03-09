
import feedparser
import requests
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.text import Text
from rich.prompt import Prompt, IntPrompt
import time
from sources import NEWS_SOURCES, FALLBACK_HEADLINES
from rss_finder import find_rss_feed

console = Console()

# -----------------------------
# Check network
# -----------------------------
def is_network_online():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except:
        return False

# -----------------------------
# Fetch headlines from RSS feed
# -----------------------------
def fetch_headlines(source_name, max_headlines=5, keywords=None, category=None):
    source = NEWS_SOURCES[source_name]
    headlines = []
    keywords = keywords or []

    try:
        feed = feedparser.parse(source["rss"])
        entries = feed.entries
        # Filter by category if possible
        if category:
            entries = [e for e in feed.entries if category.lower() in getattr(e, 'tags', [{}])[0].get('term','').lower()]
        headlines = [entry.title for entry in entries[:max_headlines]]
        if not headlines:
            headlines = FALLBACK_HEADLINES[:max_headlines]
    except:
        headlines = FALLBACK_HEADLINES[:max_headlines]

    # Highlight keywords
    highlighted = []
    for h in headlines:
        text = Text(h)
        for kw in keywords:
            text.highlight_words([kw], style="bold red")
        highlighted.append(text)
    return highlighted

# -----------------------------
# Build live table
# -----------------------------
def build_table(headlines_dict, network_status):
    table = Table(title="Elite Live News Dashboard")
    table.add_column("No.", style="cyan", width=5)
    table.add_column("Source", style="magenta", width=12)
    table.add_column("Headline", style="white", no_wrap=False)
    table.add_column("Network", style="green", width=10)

    idx = 1
    for source, headlines in headlines_dict.items():
        for h in headlines:
            table.add_row(str(idx), source, h, network_status)
            idx += 1
    return table

# -----------------------------
# Main program
# -----------------------------
def main():
    console.print("[bold green]Elite Live News Scraper Dashboard[/bold green]\n")

    # Ask user for custom websites
    custom_sites_input = Prompt.ask(
        "Enter news websites (URLs) separated by comma or press Enter to skip", default=""
    )
    custom_sites = [s.strip() for s in custom_sites_input.split(",") if s.strip()]

    # Detect RSS feeds from custom sites
    for site in custom_sites:
        detected_feeds = find_rss_feed(site)
        for idx, feed in enumerate(detected_feeds, start=1):
            name = f"{site}_feed{idx}"
            NEWS_SOURCES[name] = {"rss": feed, "categories": []}

    # Dynamic source selection
    available_sources = ", ".join(NEWS_SOURCES.keys())
    selected_sources = Prompt.ask(
        f"Enter sources separated by comma (Available: {available_sources}) or press Enter for all",
        default=available_sources
    )
    selected_sources = [s.strip() for s in selected_sources.split(",") if s.strip() in NEWS_SOURCES]

    # Category selection per source
    source_categories = {}
    for s in selected_sources:
        categories = NEWS_SOURCES[s].get("categories", [])
        if categories:
            cat_choice = Prompt.ask(
                f"Select category for {s} (Available: {', '.join(categories)}) or press Enter for all",
                default=""
            )
            source_categories[s] = cat_choice if cat_choice in categories else None
        else:
            source_categories[s] = None

    max_headlines = IntPrompt.ask("Number of headlines per source?", default=5)
    refresh_interval = IntPrompt.ask("Refresh interval in seconds?", default=60)
    keywords_input = Prompt.ask("Highlight keywords (comma separated)?", default="")
    keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]

    console.print("[cyan]Fetching live news... Press Ctrl+C to stop[/cyan]\n")

    try:
        with Live(console=console, refresh_per_second=1) as live:
            while True:
                network_status = "[green]ONLINE[/green]" if is_network_online() else "[red]OFFLINE[/red]"
                headlines_dict = {}

                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    BarColumn(),
                    transient=True,
                ) as progress:
                    task = progress.add_task("Fetching headlines...", total=len(selected_sources))
                    for source in selected_sources:
                        headlines_dict[source] = fetch_headlines(
                            source,
                            max_headlines=max_headlines,
                            keywords=keywords,
                            category=source_categories.get(source)
                        )
                        progress.update(task, advance=1)

                table = build_table(headlines_dict, network_status)
                live.update(table)
                time.sleep(refresh_interval)

    except KeyboardInterrupt:
        console.print("\n[bold red]Stopped live scraping.[/bold red]")

if __name__ == "__main__":
    main()
