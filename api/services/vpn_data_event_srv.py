import asyncio
import glob
import os
import logging

FIELDS_FOR_UPDATE = [
    'header_image_url',
    'global_coverage_image_url',
    'setup_security_image_url',
    'start_bot_image_url',
    'start_bot_image_url_2',
    'challenge_background_image'
]


async def delete_vpn_images_srv(domain: str) -> None:
    """Уделение изображений, связанных с объектам удаления"""
    vpn_images = glob.glob(os.path.join('uploads/', f'{domain}_*'))
    [os.remove(file_path) for file_path in vpn_images]
    logging.info(f"Изображения {domain} были удалены.")
    await asyncio.sleep(0.001)


async def edit_vpn_images_name_srv(target, value, oldvalue) -> None:
    """Изменение изображений и ссылок в БД"""
    if oldvalue:
        image_pattern = os.path.join('uploads/', f'{oldvalue}_*')
        images = glob.glob(image_pattern)

        for image in images:
            new_image = image.replace(f"{oldvalue}_", f"{value}_", 1)
            try:
                os.rename(image, new_image)
                logging.info(f"Переименование изображений: {value}")
            except OSError as e:
                logging.error(f"Ошибка при переименовании файла с {image} на {new_image}: {e}")

        for field in FIELDS_FOR_UPDATE:
            current_value = getattr(target, field)
            if current_value and oldvalue in current_value:
                setattr(target, field, current_value.replace(oldvalue, value))
        logging.info("Ссылки на изображения обновлены")
