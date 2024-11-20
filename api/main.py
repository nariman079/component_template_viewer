import os
import logging
from typing import Annotated, Callable, Awaitable

from fastapi import (FastAPI,
                     Depends,
                     Body,
                     File,
                     UploadFile,
                     Form,
                     HTTPException,
                     Request,
                     Response)

from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.status import HTTP_404_NOT_FOUND

from starlette.templating import Jinja2Templates

from api.bases.sqlalchemy_ext import session_context
from api.models import VPNData
from api.schemas import VPNDataCreate
from api.security import token_dependency, get_vpn_data
from api.settings import async_session
from api.utils import get_subdomain, save_file, is_exists_template

logging.basicConfig(level=logging.INFO)
logging.getLogger(__name__)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logging.getLogger('sqlalchemy.orm').setLevel(logging.INFO)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static/"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads/"), name="uploads")

templates = Jinja2Templates(directory="templates/")

@app.middleware("http")
async def database_session_middleware(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    """Установка сессии БД в контекст"""
    async with async_session.begin() as session:
        session_context.set(session)
        return await call_next(request)

@app.get('/')
async def get_page_vpn(
        request: Request
):
    full_url = request.headers.get('host')
    subdomain = await get_subdomain(full_url)
    vpn_data =  await VPNData.find_first_by_kwargs(domain=subdomain)

    if not vpn_data:
        return HTMLResponse(status_code=404, content="<h1>404</h1>")

    return templates.TemplateResponse(
        request=request, name=f"landing_{vpn_data.template_id}.html", context={"vpn": vpn_data}
    )


@app.post("/vpn_data/")
async def create_vpn_data(
        token: Annotated[token_dependency, Depends()],
        vpn_data: Annotated[VPNDataCreate, Body()],
):
    """Создание объекта VPNData
    Body:\n
    **template_id** - номер лендинга  \n
    **title** - Наименование вашего VPN, например FlyVPN \n
    **domain** - Поддоменное имя для вашего VPN, например flyvpn \n
    **bot_name** - имя бота с которого идет создание сайта ленгинга, например flyvpn_bot \n
    """
    if await VPNData.find_first_by_kwargs(domain=vpn_data.domain):
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Такой домен для VPN уже занят")
    if await VPNData.find_first_by_kwargs(bot_name=vpn_data.bot_name):
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Такое имя бота уже занята")
    if not is_exists_template(vpn_data.template_id):
        raise HTTPException(status_code=400, detail="Такого лендинга нет")

    new_vpn_data = await VPNData.create(**vpn_data.dict())
    return new_vpn_data


@app.patch("/vpn_data/{subdomain}")
async def update_vpn_data(
        vpn_data: Annotated[get_vpn_data, Depends()],
        token: Annotated[token_dependency, Depends()],
        header_image_url: UploadFile | None | str =  File(default=None),
        global_coverage_image_url: UploadFile | None =  File(default=None) ,
        setup_security_image_url: UploadFile | None =  File(default=None),
        start_bot_image_url:  UploadFile | None =  File(default=None) ,
        start_bot_image_url_2:  UploadFile | None = File(default=None),
        challenge_background_image:  UploadFile | None = File(default=None),
        title: str | None = Form(default=None),
        template_id: int | None = Form(default=None),
        domain: str | None = Form(default=None),
        header_title: str | None = Form(default=None),
        header_description: str | None = Form(default=None),
        opportunity_block_title: str | None = Form(default=None),
        opportunity_1_title: str | None = Form(default=None),
        opportunity_1_short_description: str | None = Form(default=None),
        opportunity_2_title: str | None = Form(default=None),
        opportunity_2_short_description: str | None = Form(default=None),
        opportunity_3_title: str | None = Form(default=None),
        opportunity_3_short_description: str | None = Form(default=None),
        opportunity_4_title: str | None = Form(default=None),
        opportunity_4_short_description: str | None = Form(default=None),
        opportunity_5_title: str | None = Form(default=None),
        opportunity_5_short_description: str | None = Form(default=None),
        opportunity_6_title: str | None = Form(default=None),
        opportunity_6_short_description: str | None = Form(default=None),
        global_coverage_main_title: str | None = Form(default=None),
        global_coverage_title: str | None = Form(default=None),
        global_coverage_description: str | None = Form(default=None),
        setup_security_title: str | None = Form(default=None),
        setup_security_description: str | None = Form(default=None),
        challenge_title: str | None = Form(default=None),
        challenge_short_description: str | None = Form(default=None),
        license_description: str | None = Form(default=None),
    ):
    """Изменение данных модели VPNData"""

    local_data = {
        k: v for k, v in locals().items() if k not in {"token", "vpn_data"}
    }
    updated_data = dict()

    for key, value in local_data.items():
        if 'image' in key and value:
            if value.filename == 'NaN':
                updated_data[key] = None
                continue
            updated_data[key] = await save_file(
                value,
                filename=f"{vpn_data.domain}_{key}.png"
            )
        else:
            if not value:
                continue
            updated_data[key] = value

    vpn_data.update(**updated_data)
    return updated_data


@app.delete("/vpn_data/{subdomain}")
async def delete_vpn_data(
        vpn_data: Annotated[get_vpn_data, Depends()],
        token: Annotated[token_dependency, Depends()],
):
    """Удаление модели VPNData"""
    await vpn_data.delete()
    return {"message": "VPN Успешно удален"}

