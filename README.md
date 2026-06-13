# 🗞️ AI News Aggregator & Bias Detector

A lightweight, enterprise-grade automated data pipeline that pulls live streaming articles from multiple news outlets, passes them to a remote GPU node running **Qwen 2.5**, and delivers a deduplicated, clustered, and bias-analyzed daily briefing.

By shifting text organization and cognitive synthesis completely to a remote **Ollama** infrastructure, this architecture requires zero heavy local machine learning dependencies (like PyTorch or Hugging Face transformers) on the client machine.

---

## 🏗️ System Architecture

1. **Ingest (RSS Engine):** Periodically streams real-time headlines and snippets from technical and business RSS feeds.
2. **Transport (JSON Payload Vector):** Bundles structural text articles into a localized matrix context.
3. **Remote Synthesis (Ollama API):** Dispatches context payloads to a dedicated GPU cluster running Qwen 2.5 Coder to handle topic clustering, deduplication, and media angle analysis.
4. **Presentation (Executive Display):** Formats raw data into an organized, scannable corporate briefing layout directly in your console.

---

## 📂 Project Directory Structure

```text
ai_news_aggregator/
│
├── .env                # Infrastructure network endpoints & model definitions
├── main.py             # Optimized asynchronous pipeline logic
├── requirements.txt    # Lean package configuration
└── README.md           # Documentation
🛠️ Installation & Setup
1. Prerequisites
Ensure you have Python 3.12+ installed on your host system.

2. Configure Environment Variables
Create a file named .env in the root directory to define your remote infrastructure mapping:

Plaintext
OLLAMA_BASE_URL="[http://10.22.39.192:11434](http://10.22.39.192:11434)"
OLLAMA_MODEL_NAME="qwen2.5-coder:latest"
⚠️ Note: Ensure your remote Ollama host is launched with environment bindings configured to accept external network traffic (OLLAMA_HOST=0.0.0.0).

3. Install Lean Dependencies
Install the lightweight network parsing packages using pip:

PowerShell
pip install -r requirements.txt
🚀 Execution
To stream live data feeds, run the main controller script from your terminal:

PowerShell
python main.py
📊 Sample Executive Layout Output
When executing successfully, the console will render clean Markdown elements generated from your remote AI agent:

Plaintext
==================================================
      🗞️  LIGHTWEIGHT AI NEWS AGGREGATOR ENGINE   
==================================================

📰 Fetching live streaming data articles from RSS networks...
📊 Successfully loaded 12 total news items.
🧠 Sending raw news stream to remote GPU Qwen for clustering and bias synthesis...

==================================================
          YOUR PERSONALIZED DAILY BRIEFING        
==================================================

### 📌 TOPIC: Global Semiconductor Supply Chain Adjustments
**Connected Sources:** TechCrunch, ArsTechnica
**Executive Brief:** TechCrunch reports massive financial backing changes for domestic manufacturing, while ArsTechnica provides specialized breakdowns of architecture limitations. The data shows unified movement toward specific foundry alternatives.
**Media Bias & Angle Analysis:** TechCrunch emphasizes corporate and market valuation shifts. Conversely, ArsTechnica focuses heavily on engineering bottlenecks, completely bypassing the macroeconomic implications.
--------------------------------------------------
