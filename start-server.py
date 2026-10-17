#!/usr/bin/env python3
"""Lokaler Static-Server für Punktestand (Python-stdlib, kein pip)."""

from __future__ import annotations

import os
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PORT = 4173
ROOT = Path(__file__).resolve().parent


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args))


def main() -> None:
    os.chdir(ROOT)
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://localhost:{PORT}"
    print(f"Serving {ROOT}")
    print(f"Open: {url}")
    print("Beenden: Ctrl+C")
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nGestoppt.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
