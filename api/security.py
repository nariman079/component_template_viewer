import os
from typing import Annotated

from fastapi import Header, HTTPException, UploadFile
from starlette.requests import Request
from starlette.status import HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN

from api.models import VPNData


async def token_dependency(
        telegram_api_x_token: Annotated[str, Header(
            description="Ключ авторизации для выполнения запросов, "
                  "без этого ключа ваш запрос будет отклонен"
        )],
        request: Request,
) -> str:
    """Проверка токена"""
    if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
        auth_token = request.headers.get('telegram-api-x-token')
        if not auth_token:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Вы не авторизованы"
            )
        if auth_token != os.getenv('SECRET_TELEGRAM_TOKEN', 'test'):
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN,
                detail={"detail":"Неверный токен авторизации"}
            )
    return telegram_api_x_token

async def get_vpn_data(
    subdomain: str
) -> VPNData:
    vpn_data_db = await VPNData.find_first_by_kwargs(domain=subdomain)
    if vpn_data_db is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="VPN data not found")

    return vpn_data_db

