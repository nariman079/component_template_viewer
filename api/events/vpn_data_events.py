import asyncio

from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.orm import Mapper
from random import randint

from api.bases.descriptions import seo_description_data
from api.models import VPNData
from api.services.vpn_data_event_srv import delete_vpn_images_srv, edit_vpn_images_name_srv


@event.listens_for(VPNData, 'before_insert')
def setup_vpn_date(
        mapper: Mapper,
        connection: AsyncConnection,
        target: VPNData
) -> None:
    """Изменение модели до ее создания"""
    target.license_description = f"© 2024 {target.title}. Все права защищены."
    target.start_bot_button_url = f"https://web.telegram.org/k/#@{target.bot_name}"
    target.seo_description = seo_description_data.get(randint(1,5))

@event.listens_for(VPNData, 'after_delete')
def delete_vpn_images(
        mapper: Mapper,
        connection: AsyncConnection,
        target: VPNData
) -> None:
    """Событие на удеаление объекта из БД"""
    asyncio.create_task(
        delete_vpn_images_srv(target.domain)
    )

@event.listens_for(VPNData.domain, 'set')
def edit_vpn_image(
        target: VPNData,
        value: str,
        oldvalue: str,
        initiator
) -> None:
    """Изменение названия изображений"""
    asyncio.create_task(
        edit_vpn_images_name_srv(target, value, oldvalue)
    )
