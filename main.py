from contextlib import asynccontextmanager
from random import random

from fastapi import FastAPI, UploadFile, Body
from fastapi.middleware.cors import CORSMiddleware

from aiohttp import ClientSession

from advertising_locations import best_strategy_async

from logic.geocoding import resolve_polygon_titles
from misc.data_models import AudienceReach, TargetAudience, Polygon, Coordinates, Part1Response, GeneticsMode
from misc.config import age_categories


app = FastAPI()

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)


session = ClientSession()


@asynccontextmanager
async def lifespan():
    yield

    await session.close()


@app.get("/")
async def index():
    return {"message": "I <3 Scarlett"}


@app.post("/polygons")
async def polygons(
        target_audience: TargetAudience = Body(embed=True),
        count: int = Body(embed=True),
        mode: GeneticsMode = Body(embed=True)
) -> list[Polygon]:
    raw_result = await best_strategy_async(
        num_banners=count,
        num_polygons=40 ** 2,
        target_audience=target_audience.TA,
        iterations=(20 if mode == GeneticsMode.QUICK else 50)
    )

    with open("temp.txt", "w") as f:
        f.write(str(raw_result))

    result = [
        Polygon(
            top_left=Coordinates(
                latitude=raw_polygon.lat_top,
                longitude=raw_polygon.lon_left
            ),
            bottom_right=Coordinates(
                latitude=raw_polygon.lat_bottom,
                longitude=raw_polygon.lon_right
            ),
            count=raw_polygon.count
        )
        for raw_polygon in raw_result
    ]

    await resolve_polygon_titles(session, result)

    return result


@app.post("/audience_reach")
async def audience_reach(file: UploadFile) -> Part1Response:
    return Part1Response(
        value=30,
        reach=[
            AudienceReach(
                age_from=category[0],
                age_to=category[1],
                percentage=random() * 100
            )
            for category in age_categories
        ]
    )
