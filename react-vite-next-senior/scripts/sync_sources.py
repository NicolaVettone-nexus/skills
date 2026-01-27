import hashlib
import os
import sys
from datetime import datetime
from urllib.request import urlopen, Request

SOURCES = [
  ("react_blog", "https://react.dev/blog"),
  ("react_versions", "https://react.dev/versions"),
  ("react_19", "https://react.dev/blog/2024/12/05/react-19"),
  ("react_19_2", "https://react.dev/blog/2025/10/01/react-19-2"),
  ("react_compiler_1", "https://react.dev/blog/2025/10/07/react-compiler-1"),
  ("next_blog", "https://nextjs.org/blog"),
  ("next_15", "https://nextjs.org/blog/next-15"),
  ("next_cache_components", "https://nextjs.org/docs/app/getting-started/cache-components"),
  ("vite_releases", "https://vite.dev/releases"),
  ("vite_6", "https://vite.dev/blog/announcing-vite6"),
  ("vite_migration", "https://vite.dev/guide/migration"),
]

OUT_DIR = "references/.sync"
os.makedirs(OUT_DIR, exist_ok=True)

def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "skill-sync/1.0"})
    with urlopen(req, timeout=30) as r:
        return r.read()

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main():
    changed = []
    for key, url in SOURCES:
        data = fetch(url)
        h = sha256(data)

        hash_path = os.path.join(OUT_DIR, f"{key}.sha256")
        prev = open(hash_path, "r", encoding="utf-8").read().strip() if os.path.exists(hash_path) else None

        if prev != h:
            changed.append((key, url, prev, h))
            with open(os.path.join(OUT_DIR, f"{key}.html"), "wb") as f:
                f.write(data)
            with open(hash_path, "w", encoding="utf-8") as f:
                f.write(h)

    report_path = os.path.join(OUT_DIR, "REPORT.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# Sync report\n\nGenerated: {datetime.utcnow().isoformat()}Z\n\n")
        if not changed:
            f.write("No changes detected.\n")
        else:
            f.write("## Changes detected\n\n")
            for key, url, prev, h in changed:
                f.write(f"- **{key}** changed: {url}\n")

    # Exit 0 always; PR tool will pick up file diffs.
    print(f"Done. Changes: {len(changed)}. Report: {report_path}")

if __name__ == "__main__":
    main()
