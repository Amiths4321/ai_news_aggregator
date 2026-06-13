import os
import json
import feedparser
import requests
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# 1. LIVE DATA INGESTION ENGINE (RSS)
# ==========================================
class NewsIngestionEngine:
    def __init__(self):
        self.sources = {
            "TechCrunch": "https://techcrunch.com/feed/",
            "VentureBeat": "https://venturebeat.com/feed/",
            "ArsTechnica": "https://feeds.arstechnica.com/arstechnica/index"
        }

    def fetch_latest_articles(self, limit_per_source=4):
        print("📰 Fetching live streaming data articles from RSS networks...")
        collected_articles = []
        
        for source_name, url in self.sources.items():
            try:
                feed = feedparser.parse(url)
                entries = feed.entries[:limit_per_source]
                for entry in entries:
                    collected_articles.append({
                        "source": source_name,
                        "title": entry.title,
                        "summary": entry.get("summary", entry.title)[:300]  # Keep snippets compact
                    })
            except Exception as e:
                print(f"⚠️ Failed fetching from {source_name}: {e}")
                
        print(f"📊 Successfully loaded {len(collected_articles)} total news items.")
        return collected_articles

# ==========================================
# 2. REMOTE GPU PIPELINE CONTROLLER
# ==========================================
class QwenAggregatorAnalyst:
    def __init__(self):
        self.base_url = os.getenv("OLLAMA_BASE_URL", "http://10.22.39.192:11434")
        self.model_name = os.getenv("OLLAMA_MODEL_NAME", "qwen2.5-coder:14b")

    def process_newspaper(self, articles):
        # Convert all articles into a structured text context block
        articles_context = ""
        for i, art in enumerate(articles):
            articles_context += f"ID: {i+1} | Source: {art['source']}\nTitle: {art['title']}\nSnippet: {art['summary']}\n\n"

        system_prompt = (
            "You are an elite AI News Aggregator engine.\n"
            "Your task is to take a raw list of incoming articles, automatically group/cluster them by underlying story topic, "
            "deduplicate repeating stories, and synthesize them into a clean daily newspaper briefing.\n\n"
            "For each distinct topic/story group you discover, output using this EXACT markdown layout:\n\n"
            "### 📌 TOPIC: [Name of the story/theme group]\n"
            "**Connected Sources:** [List the media outlets covering this story]\n"
            "**Executive Brief:** [Tight 3-sentence summary synthesizing facts from all sources without repetition]\n"
            "**Media Bias & Angle Analysis:** [Examine how different sources framed the story. Did one focus on business, another on technical details, or another on controversy? Calling out specific outlets.]\n"
            "--------------------------------------------------"
        )

        try:
            print("🧠 Sending raw news stream to remote GPU Qwen for clustering and bias synthesis...")
            response = requests.post(
                f"{self.base_url}/api/chat",  # 🟢 Changed from /api/generate to /api/chat
                json={
                    "model": self.model_name,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Analyze, cluster, and deduplicate these articles:\n\n{articles_context}"}
                    ],
                    "stream": False,
                    "options": {"temperature": 0.3}
                },
                timeout=90
            )
            if response.status_code == 200:
                # Chat endpoint returns data inside ['message']['content']
                return response.json().get("message", {}).get("content", "No brief generated.")
            return f"Error from Ollama node: Status {response.status_code}"
        except Exception as e:
            return f"Failed connecting to remote GPU server: {e}"

# ==========================================
# 3. RUNTIME EXECUTION
# ==========================================
if __name__ == "__main__":
    print("==================================================")
    print("      🗞️  LIGHTWEIGHT AI NEWS AGGREGATOR ENGINE   ")
    print("==================================================\n")

    scraper = NewsIngestionEngine()
    raw_news = scraper.fetch_latest_articles(limit_per_source=4)

    if raw_news:
        analyst = QwenAggregatorAnalyst()
        briefing = analyst.process_newspaper(raw_news)
        
        print("\n==================================================")
        print("          YOUR PERSONALIZED DAILY BRIEFING        ")
        print("==================================================\n")
        print(briefing)
    else:
        print("❌ No articles fetched.")