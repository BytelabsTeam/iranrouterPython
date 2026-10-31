from __future__ import annotations

import os
from typing import Optional

from openai import OpenAI

DEFAULT_BASE_URL = "https://iranrouter.net/api/v1"


def create_client(
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
) -> OpenAI:
    """
    کلاینت سازگار با OpenAI برای IranRouter بسازید.

    کلید را از متغیر محیطی `IRANROUTER_API_KEY` می‌خواند
    مگر اینکه خودتان `api_key` بدهید.
    """
    key = api_key or os.getenv("IRANROUTER_API_KEY")
    if not key:
        raise ValueError(
            "کلید API پیدا نشد. "
            "متغیر IRANROUTER_API_KEY را ست کنید یا api_key بدهید. "
            "کلید را از https://iranrouter.net/dashboard/keys بگیرید."
        )

    url = (base_url or os.getenv("IRANROUTER_BASE_URL") or DEFAULT_BASE_URL).rstrip(
        "/"
    )
    return OpenAI(api_key=key, base_url=url)


# نام کوتاه برای import راحت‌تر
IranRouter = create_client
