"""
چت بدون OpenAI SDK — فقط HTTP

اجرا:
  python examples/07_http_chat.py
"""

import _bootstrap  # noqa: F401
import os

import httpx

from iranrouter import DEFAULT_BASE_URL

api_key = os.environ["IRANROUTER_API_KEY"]
base_url = os.getenv("IRANROUTER_BASE_URL", DEFAULT_BASE_URL).rstrip("/")

payload = {
    "model": "deepseek/deepseek-flash",
    "messages": [{"role": "user", "content": "سلام"}],
}

with httpx.Client(timeout=60.0) as http:
    r = http.post(
        f"{base_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
    )
    r.raise_for_status()
    data = r.json()

print(data["choices"][0]["message"]["content"])
print("request_id:", r.headers.get("X-Request-Id"))
