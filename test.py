import asyncio
from pprint import pprint

import aiofiles
import aiohttp


async def update_vpn_data(
        subdomain: str,
        token: str,
        update_data: dict,
        files: dict
):
    """
    Отправляет запрос на обновление данных VPN через API.

    :param subdomain: Поддомен для обновления данных.
    :param token: Токен авторизации.
    :param update_data: Данные формы для обновления (словари ключ-значение).
    :param files: Файлы для отправки (словари ключ-файл).
    """
    url = f"http://localhost/vpn_data/{subdomain}"
    headers = {"telegram-api-x-token": token}

    # Формируем данные для отправки
    form_data = aiohttp.FormData()

    # Добавляем данные формы
    for key, value in update_data.items():
        if value is not None:
            form_data.add_field(key, str(value))

    # Добавляем файлы
    for key, file_path in files.items():
        if file_path == 'NaN':
            form_data.add_field(key, 'NaN', filename=file_path.split("/")[-1])
            continue
        if file_path:
            async with aiofiles.open(file_path, "rb") as file:
                form_data.add_field(key, await file.read(), filename=file_path.split("/")[-1])

    # Выполняем запрос
    async with aiohttp.ClientSession() as session:
        async with session.patch(url, headers=headers, data=form_data) as response:
            if response.status == 200:
                result = await response.json()
                pprint(result)
                return result
            else:
                print(f"Error {response.status}: {await response.text()}")
                return None

# Пример использования
update_data = {
    "domain": 'data'
}

files = {
    # 'challenge_background_image': "tests/files/img.png"
}


asyncio.run(update_vpn_data("user", "test", update_data, files))
