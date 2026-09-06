import json
from datetime import datetime
import urllib.request

def get_chrome_version():
    try:
        url = "https://versionhistory.googleapis.com/v1/chrome/platforms/win/channels/stable/versions"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return data['versions'][0]['version']
    except Exception:
        return "130.0.6723.92"

chrome_ver = get_chrome_version()
now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

data = {
    "last_updated": now_str,
    "agents": [
        {
            "browser": "Google Chrome (Windows)",
            "platform": "Desktop",
            "ua": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36"
        },
        {
            "browser": "Google Chrome (Mac)",
            "platform": "Desktop",
            "ua": f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36"
        },
        {
            "browser": "Google Chrome (Android)",
            "platform": "Mobile",
            "ua": f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36"
        },
        {
            "browser": "Apple Safari (iPhone / iOS)",
            "platform": "Mobile",
            "ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
        },
        {
            "browser": "Apple Safari (iPad / iPadOS)",
            "platform": "Tablet",
            "ua": "Mozilla/5.0 (iPad; CPU OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
        }
    ]
}

with open("agents.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("agents.json with iOS updated successfully!")
