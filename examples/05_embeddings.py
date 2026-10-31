"""
ساخت embedding

اجرا:
  python examples/05_embeddings.py
"""

import _bootstrap  # noqa: F401

from iranrouter import IranRouter

client = IranRouter()

response = client.embeddings.create(
    model="iranrouter/demo-embed",
    input="سلام دنیا",
)

vector = response.data[0].embedding
print(f"ابعاد: {len(vector)}")
print(f"نمونه: {vector[:5]} …")
