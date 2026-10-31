"""
فهرست مدل‌های در دسترس

اجرا:
  python examples/03_models.py
"""

import _bootstrap  # noqa: F401

from iranrouter import IranRouter

client = IranRouter()

models = client.models.list()

for model in models.data[:20]:
    print(model.id)

print(f"\n… مجموع در این صفحه: {len(models.data)}")
