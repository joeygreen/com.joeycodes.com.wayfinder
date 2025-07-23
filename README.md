# --- README.md ---

# Product Scraper
A Python app that scrapes product availability from a target website.
This currently only works for disneystore.com

## 🛠️ Quick Start
Run the follwoing cmds from the project root

```bash
# Install dependencies
pip install -r requirements.txt

# Start the API
PYTHONPATH=src uvicorn src.api:app --reload

# Start the Streamlit GUI
streamlit run src/ui/monitor_dashboard.py
