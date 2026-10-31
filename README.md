# IranRouter Python

راهنمای ساده اتصال به [IranRouter](https://iranrouter.net) با پایتون.

IranRouter یک API سازگار با OpenAI است.
فقط `base_url` و کلید API را عوض کنید — بقیه مثل OpenAI SDK است.

## شروع سریع

### ۱) کلید بگیرید

از [ثبت‌نام](https://iranrouter.net/register) حساب بسازید.
بعد در [داشبورد ← کلیدها](https://iranrouter.net/dashboard/keys) یک کلید `ir-…` بگیرید.

### ۲) نصب

```bash
pip install openai python-dotenv
```

یا کل این ریپو:

```bash
git clone https://github.com/BytelabsTeam/iranrouterPython.git
cd iranrouterPython
pip install -r requirements.txt
```

### ۳) کلید را ست کنید

```bash
export IRANROUTER_API_KEY="ir-..."
```

یا فایل `.env` بسازید (از روی `.env.example`).

### ۴) اولین درخواست

```python
from openai import OpenAI

client = OpenAI(
    api_key="ir-...",  # یا از IRANROUTER_API_KEY بخوانید
    base_url="https://iranrouter.net/api/v1",
)

response = client.chat.completions.create(
    model="deepseek/deepseek-flash",
    messages=[{"role": "user", "content": "سلام"}],
)

print(response.choices[0].message.content)
```

با helper همین ریپو:

```python
from iranrouter import IranRouter

client = IranRouter()  # از IRANROUTER_API_KEY می‌خواند

response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
```

## اتصال در یک نگاه

| مورد | مقدار |
|------|--------|
| Base URL | `https://iranrouter.net/api/v1` |
| Auth | `Authorization: Bearer ir-…` |
| Env key | `IRANROUTER_API_KEY` |
| Docs | https://iranrouter.net/docs |
| مدل‌ها | https://iranrouter.net/models |

## نمونه‌ها

از ریشهٔ ریپو اجرا کنید:

```bash
cp .env.example .env   # کلید را داخلش بگذارید
python examples/01_chat.py
python examples/02_stream.py
python examples/03_models.py
python examples/04_check_key.py
python examples/05_embeddings.py
python examples/06_images.py
python examples/07_http_chat.py
```

| فایل | کار |
|------|-----|
| `examples/01_chat.py` | چت ساده |
| `examples/02_stream.py` | استریم |
| `examples/03_models.py` | فهرست مدل‌ها |
| `examples/04_check_key.py` | وضعیت کلید / اعتبار |
| `examples/05_embeddings.py` | embedding |
| `examples/06_images.py` | تولید تصویر |
| `examples/07_http_chat.py` | چت با HTTP خالص (بدون OpenAI SDK) |

## استریم

```python
from iranrouter import IranRouter

client = IranRouter()

stream = client.chat.completions.create(
    model="deepseek/deepseek-flash",
    messages=[{"role": "user", "content": "یک داستان کوتاه بگو"}],
    stream=True,
)

for chunk in stream:
    if not chunk.choices:
        continue
    text = chunk.choices[0].delta.content
    if text:
        print(text, end="", flush=True)
```

## HTTP بدون SDK

```python
import os
import httpx

api_key = os.environ["IRANROUTER_API_KEY"]

r = httpx.post(
    "https://iranrouter.net/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    json={
        "model": "deepseek/deepseek-flash",
        "messages": [{"role": "user", "content": "سلام"}],
    },
    timeout=60.0,
)
r.raise_for_status()
print(r.json()["choices"][0]["message"]["content"])
```

## مدل‌های رایج

شناسه را از [کاتالوگ](https://iranrouter.net/models) کپی کنید. چند نمونه:

- `deepseek/deepseek-flash` — مناسب شروع / سطح رایگان
- `openai/gpt-4o-mini` — چت سبک
- `openai/gpt-4o` — چت قوی‌تر
- `openai/gpt-image-2.5-sunburst` — تصویر

سطح رایگان روی بعضی مدل‌ها فعال است؛ جزئیات در [مستندات](https://iranrouter.net/docs#free-tier).

## endpointهای اصلی

| متد | مسیر |
|-----|------|
| `GET` | `/models` |
| `GET` | `/key` |
| `POST` | `/chat/completions` |
| `POST` | `/embeddings` |
| `POST` | `/images/generations` |
| `POST` | `/images/edits` |
| `POST` | `/videos/generations` |
| `GET` | `/generation/{id}` |

## نکات

- کلید را در کد commit نکنید؛ از env استفاده کنید.
- اگر قبلاً OpenAI / OpenRouter داشتید، فقط URL و کلید را عوض کنید.
- پاسخ chat موفق معمولاً هدر `X-Request-Id` دارد.
- خطای سهمیه رایگان تمام‌شده معمولاً HTTP `402` است.

## لینک‌ها

- سایت: https://iranrouter.net
- مستندات API: https://iranrouter.net/docs
- کلیدها: https://iranrouter.net/dashboard/keys
- شارژ اعتبار: https://iranrouter.net/dashboard/credits

MIT — [Bytelabs](https://github.com/BytelabsTeam)
