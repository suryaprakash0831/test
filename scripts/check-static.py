from pathlib import Path
from html.parser import HTMLParser

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in {"href", "src"} and value and not value.startswith(("http://", "https://", "#")):
                self.assets.append(value)

root = Path(__file__).resolve().parents[1]
html = root / "index.html"
css = root / "styles.css"

if not html.exists():
    raise SystemExit("index.html is missing")
if not css.exists():
    raise SystemExit("styles.css is missing")

parser = Parser()
parser.feed(html.read_text(encoding="utf-8"))

missing = []
for asset in parser.assets:
    if asset == "assets/blue-yonder-logo.svg":
        continue
    if not (root / asset).exists():
        missing.append(asset)

if missing:
    raise SystemExit(f"Missing referenced assets: {', '.join(missing)}")

required_text = [
    "Crystal Ball AI",
    "Autonomous Agent for Warehouse Management Operations",
    "Predict. Monitor. Recommend. Automate.",
    "AI Recommendations",
    "Incident Correlation",
]
page = html.read_text(encoding="utf-8")
missing_text = [text for text in required_text if text not in page]
if missing_text:
    raise SystemExit(f"Missing required copy: {', '.join(missing_text)}")

print("Static UI check passed")
