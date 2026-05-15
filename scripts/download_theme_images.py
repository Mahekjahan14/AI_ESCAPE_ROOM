"""Download all theme images to assets/images/ for offline-reliable loading."""

import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from data.themes import _PEXELS, _pexels_url  # noqa: E402

ASSETS = Path(__file__).resolve().parent.parent / "assets" / "images"
ASSETS.mkdir(parents=True, exist_ok=True)

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}


def download_one(key: str, photo_id: int) -> bool:
    dest = ASSETS / f"{key}.jpg"
    url = _pexels_url(photo_id)
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        if len(data) < 5000:
            print(f"  SKIP {key}: too small ({len(data)} bytes)")
            return False
        dest.write_bytes(data)
        print(f"  OK   {key} ({len(data) // 1024} KB)")
        return True
    except Exception as exc:
        print(f"  FAIL {key}: {exc}")
        return False


def main():
    ok, fail = 0, 0
    for key, photo_id in sorted(_PEXELS.items()):
        if download_one(key, photo_id):
            ok += 1
        else:
            fail += 1
        time.sleep(0.5)
    print(f"\nDone: {ok} saved, {fail} failed -> {ASSETS}")


if __name__ == "__main__":
    main()
