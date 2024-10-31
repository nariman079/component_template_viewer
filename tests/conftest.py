from typing import AsyncGenerator
import logging

import pytest

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from api.database import get_db
from api.models import Base
from api.main import app


logging.basicConfig(level=logging.DEBUG)


engine_test = create_async_engine('sqlite+aiosqlite:///./test.db', echo=True, future=True)

AsyncSessionTest= sessionmaker(
    autocommit=False, autoflush=False, bind=engine_test, class_=AsyncSession
)



@pytest.fixture(scope="function")
async def async_session():
    # Создаем таблицы перед каждым тестом
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


    yield

    # Удаляем таблицы после каждого теста
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)



async def get_test_db() -> AsyncGenerator[AsyncSession, None]:
    """Асинхронная фикстура для создания новой сессии перед каждым тестом"""
    async with AsyncSessionTest() as session:
        yield session


@pytest.fixture(autouse=True)
def override_get_db():
    app.dependency_overrides[get_db] = get_test_db

