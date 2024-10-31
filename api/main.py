import os
from typing import Annotated

from fastapi import FastAPI, Depends, Body
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.exceptions import HTTPException
from starlette.responses import Response, RedirectResponse, HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN
from starlette.templating import Jinja2Templates

from api.database import get_db
from api.models import VPNData
from api.schemas import VPNDataUpdate, VPNDataCreate
from api.services import CustomRequest, get_custom_request
from api.utils import get_subdomain

app = FastAPI()
app.mount("/static", StaticFiles(directory="static/"), name="static")

templates = Jinja2Templates(directory="templates/")



@app.middleware('http')
async def split_subdomain(request:Annotated[CustomRequest, Depends(get_custom_request)]  , call_next) -> Response:
    """Получение поддомена"""
    full_url = request.headers.get('host')
    request.subdomain = await get_subdomain(full_url)
    response = await call_next(request)
    return response

@app.middleware('http')
async def check_auth(request: CustomRequest, call_next) -> Response:
    """Проверка токена авторизации"""
    if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
        auth_token = request.headers.get('Telegram-API-X-Token')
        if not auth_token:
            return Response(
                status_code=HTTP_401_UNAUTHORIZED,
                content="Вы не авторизованы"
            )
        if auth_token != os.getenv('SECRET_TELEGRAM_TOKEN', 'test'):
            return Response(
                status_code=HTTP_403_FORBIDDEN,
                content="Неверный токен!"
            )
    response = await call_next(request)
    return response

@app.get('/')
async def get_page_vpn(
        request: Annotated[get_custom_request, Depends()],
        db: Annotated[get_db, Depends()]
        ):
    query = await db.execute(select(VPNData).where(VPNData.vpn_title == request.subdomain))
    vpn_data = query.scalar_one_or_none()
    if not vpn_data:
        return HTMLResponse(status_code=404, content="<h1>404</h1>")

    return templates.TemplateResponse(
        request=request, name="landing_1.html", context={"subdomain": request.subdomain}
    )

@app.post("/vpn_data/")
async def create_vpn_data(
        vpn_data: Annotated[VPNDataCreate, Body()],
        db: Annotated[AsyncSession , Depends(get_db)]
):
    new_vpn_data = VPNData(**vpn_data.dict())
    db.add(new_vpn_data)
    await db.commit()
    return vpn_data


@app.patch("/vpn_data/{id}")
async def update_vpn_data(
        id: int,
        vpn_data: VPNDataUpdate,
        db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(VPNData).filter(VPNData.id == id))
    db_vpn_data = result.scalar_one_or_none()

    if db_vpn_data is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="VPN data not found")

    for key, value in vpn_data.dict(exclude_unset=True).items():
        setattr(db_vpn_data, key, value)

    db.add(db_vpn_data)
    await db.commit()
    return {"message": "VPN data updated successfully"}

@app.delete("/vpn_data/{id}")
async def delete_vpn_data(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(VPNData).filter(VPNData.id == id))
    db_vpn_data = result.scalar_one_or_none()

    if db_vpn_data is None:
        raise HTTPException(status_code=404, detail="VPN data not found")

    await db.delete(db_vpn_data)
    await db.commit()
    return {"message": "VPN data deleted successfully"}