"""
تولید تصویر

اجرا:
  python examples/06_images.py
"""

import _bootstrap  # noqa: F401

from iranrouter import IranRouter

client = IranRouter()

response = client.images.generate(
    model="openai/gpt-image-2.5-sunburst",
    prompt="a teal fox in the desert at dusk",
    size="1024x1024",
)

item = response.data[0]
print(item.url or (item.b64_json[:80] + "…" if item.b64_json else item))
