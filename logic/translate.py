from typing import Iterable
import asyncio

from gpytranslate import Translator


async def translate(texts: Iterable[str], sourcelang: str = "en", targetlang: str = "ru") -> list[str]:
    translator = Translator()

    translation_tasks = [
        translator.translate(
            text=text,
            sourcelang=sourcelang,
            targetlang=targetlang
        )
        for text in texts
    ]

    translations = await asyncio.gather(*translation_tasks)

    return [translation.text.removesuffix(".") for translation in translations]
