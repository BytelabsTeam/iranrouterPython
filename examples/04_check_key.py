"""
بررسی کلید، اعتبار و سطح رایگان

GET /api/v1/key

اجرا:
  python examples/04_check_key.py
"""

import _bootstrap  # noqa: F401
import json
import os

import httpx

from iranrouter import DEFAULT_BASE_URL

api_key = os.environ["IRANROUTER_API_KEY"]
base_url = os.getenv("IRANROUTER_BASE_URL", DEFAULT_BASE_URL).rstrip("/")

with httpx.Client(timeout=30.0) as http:
    r = http.get(
        f"{base_url}/key",
        headers={"Authorization": f"Bearer {api_key}"},
    )
    r.raise_for_status()
    print(json.dumps(r.json(), ensure_ascii=False, indent=2))
