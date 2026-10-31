"""
چت ساده با IranRouter

اجرا:
  export IRANROUTER_API_KEY=ir-...
  python examples/01_chat.py
"""

import _bootstrap  # noqa: F401

from iranrouter import IranRouter

client = IranRouter()

response = client.chat.completions.create(
    model="deepseek/deepseek-flash",
    messages=[
        {"role": "user", "content": "سلام! خودت را در یک جمله معرفی کن."},
    ],
)

print(response.choices[0].message.content)
