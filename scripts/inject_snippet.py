import sys
from pathlib import Path

SNIPPET_FILE = Path(__file__).resolve().parent.parent / "embed.html"

USAGE = """Usage: python inject_snippet.py <path/to/index.html> [snippet.html]\n"""

def load_snippet(path: Path) -> str:
    try:
        return path.read_text()
    except Exception as e:
        raise SystemExit(f"Failed to read snippet {path}: {e}")

def inject(target: Path, snippet: str) -> None:
    try:
        text = target.read_text()
    except Exception as e:
        raise SystemExit(f"Failed to read {target}: {e}")

    if snippet.strip() in text:
        print("Snippet already present")
        return

    close_tag = "</body>"
    idx = text.lower().rfind(close_tag)
    if idx == -1:
        raise SystemExit(f"No closing </body> tag found in {target}")

    new_text = text[:idx] + snippet + "\n" + text[idx:]
    target.write_text(new_text)
    print(f"Injected snippet into {target}")


def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv:
        print(USAGE)
        return

    html_path = Path(argv[0])
    snippet_path = Path(argv[1]) if len(argv) > 1 else SNIPPET_FILE
    snippet = load_snippet(snippet_path)
    inject(html_path, snippet)


if __name__ == "__main__":
    main()
