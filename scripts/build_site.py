"""Render shared navigation and page content into the GitHub Pages /docs source."""
from pathlib import Path
from html import escape
ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "index": ("Home", "Freedom through clarity. An open-source initiative for legal transparency and citizen participation."),
    "about": ("About", "Learn about the mission and development of Framers Linguistic Protocol."),
    "faq": ("FAQ", "Questions and answers about FLP, participation, AI, and the proposed FRA token."),
    "contact": ("Contact", "Send questions and feedback to Framers Linguistic Protocol using your email app."),
    "protocol": ("Protocol", "Explore the proposed FLP framework and download the draft overview."),
    "thanks": ("Email help", "Help with preparing and sending an email to FLP."),
}
def build():
    template = (ROOT / "site/template.html").read_text()
    header = (ROOT / "site/partials/header.html").read_text().rstrip("\n")
    footer = (ROOT / "site/partials/footer.html").read_text().rstrip("\n")
    for slug, (title, description) in PAGES.items():
        nav = "".join(f'<li><a href="{key}.html"' + (' aria-current="page"' if slug == key else '') + f'>{value[0]}</a></li>' for key, value in PAGES.items() if key != "thanks")
        content = (ROOT / f"site/content/{slug}.html").read_text().rstrip("\n")
        page = template
        for key, value in {"title":escape(title), "description":escape(description), "header":header.replace("{{navigation}}", nav), "content":content, "footer":footer}.items():
            page = page.replace("{{" + key + "}}", value)
        (ROOT / f"docs/{slug}.html").write_text(page)
    (ROOT / "docs/.nojekyll").touch()
if __name__ == "__main__":
    build()
