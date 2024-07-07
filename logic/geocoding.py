from typing import Iterable
import asyncio

from aiohttp import ClientSession

from logic.translate import translate
from misc.data_models import Polygon
from misc.config import GEOAPIFY_KEY


async def get_district_name(session: ClientSession, latitude: float, longitude: float) -> str:
    async with session.get(
        f"https://api.geoapify.com/v1/geocode/reverse?lat={latitude}&lon={longitude}&format=json&apiKey={GEOAPIFY_KEY}"
    ) as response:
        json = await response.json()

        result = json["results"][0]
        district_name = ", ".join(
            filter(
                lambda field: field is not None,
                (result.get("city"), result.get("district"), result.get("suburb"), result.get("street"))
            )
        )

        return district_name


async def resolve_polygon_titles(session: ClientSession, polygons: Iterable[Polygon]) -> None:
    district_name_tasks = [
        get_district_name(
            session=session,
            latitude=polygon.center.latitude,
            longitude=polygon.center.longitude
        )
        for polygon in polygons
    ]

    district_names = await asyncio.gather(*district_name_tasks)
    # district_names_translated = await translate(district_names)

    # for (polygon, title) in zip(polygons, district_names_translated):
    for (polygon, title) in zip(polygons, district_names):
        polygon.title = title
