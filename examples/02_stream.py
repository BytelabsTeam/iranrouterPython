"""
چت با استریم (SSE)

اجرا:
  python examples/02_stream.py
"""

import _bootstrap  # noqa: F401

from iranrouter import IranRouter

client = IranRouter()

stream = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {"role": "user", "content": "سه نکته کوتاه درباره پایتون بگو."},
    ],
    stream=True,
)

for chunk in stream:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)

print()
