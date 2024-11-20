import asyncio
import sys
from os import getenv
from pathlib import Path

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine

current_directory: Path = Path.cwd()

if sys.platform == "win32":  # pragma: no cover
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


PRODUCTION_MODE: bool = getenv("PRODUCTION_MODE", False)

if PRODUCTION_MODE:
    DB_URL = getenv("DB_LINK")
else:
    DB_URL = "postgresql+asyncpg://test:test@localhost:5431/test"

engine = create_async_engine(
    DB_URL,
    pool_recycle=280,  # noqa: WPS432
    echo=not PRODUCTION_MODE,
)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


# Импорт событий
import api.events.vpn_data_events