import asyncio

from aiohttp import ClientSession
from sqlalchemy.testing.plugin.plugin_base import logging

from api.schemas import VPNDataCreate


class TestVpnAPI:
    def __init__(self, vpn_data: dict):
        self.vpn_data = vpn_data
        self.host = 'localhost:8000'


    async def test_create_vpn_data(self):
        async with ClientSession() as client:
            headers = {
                "Host": "https://test.domain.ru",
                "Telegram-API-X-Token": "test"
            }
            response =  await client.post(
                url="http://localhost:8000/vpn_data/",
                headers=headers,
                json={
                    'template_id':1,
                    'vpn_title': 'test'
                }
            )
            assert response.status == 200

    async def test_get_vpn_data(self):
        async with ClientSession() as client:
            headers = {
                "Host": "test.domain.ru",
                "Telegram-API-X-Token": "test"
            }
            response = await client.get(
                url="http://localhost:8000/",
                headers=headers,

            )
            assert await response.text() == ''

