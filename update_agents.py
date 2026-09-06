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
# Edge এবং Opera ক্রোমিয়াম ভিত্তিক, তাই এদের মেজর ভার্সন ক্রোমের সাথে মিল থাকে
major_ver = chrome_ver.split('.')[0]
now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

data = {
    "last_updated": now_str,
    "agents": [
        # --- Google Chrome ---
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
            "browser": "Google Chrome (Linux)",
            "platform": "Desktop",
            "ua": f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36"
        },
        {
            "browser": "Google Chrome (Android)",
            "platform": "Mobile",
            "ua": f"Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36"
        },

        # --- Mozilla Firefox ---
        {
            "browser": "Mozilla Firefox (Windows)",
            "platform": "Desktop",
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"
        },
        {
            "browser": "Mozilla Firefox (Mac)",
            "platform": "Desktop",
            "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:132.0) Gecko/20100101 Firefox/132.0"
        },
        {
            "browser": "Mozilla Firefox (Android)",
            "platform": "Mobile",
            "ua": "Mozilla/5.0 (Android 14; Mobile; rv:132.0) Gecko/132.0 Firefox/132.0"
        },

        # --- Microsoft Edge ---
        {
            "browser": "Microsoft Edge (Windows)",
            "platform": "Desktop",
            "ua": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36 Edg/{chrome_ver}"
        },
        {
            "browser": "Microsoft Edge (Mac)",
            "platform": "Desktop",
            "ua": f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36 Edg/{chrome_ver}"
        },

        # --- Apple Safari ---
        {
            "browser": "Apple Safari (Mac Desktop)",
            "platform": "Desktop",
            "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15"
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
        },

        # --- Opera ---
        {
            "browser": "Opera (Windows)",
            "platform": "Desktop",
            "ua": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36 OPR/114.0.0.0"
        }
    ]
}

with open("agents.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("agents.json updated with all major browsers successfully!")
