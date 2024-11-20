import re
import aiofiles
from starlette.datastructures import UploadFile



async def save_file(
        file: UploadFile,
        filename: str,
) -> str:
    """Сохраннение файла"""

    async with aiofiles.open(f'uploads/{filename}', 'wb') as new_file:
        content = await file.read()
        await new_file.write(content)
    return filename

async def get_subdomain(url: str) -> str | None:
    """Получение поддомена с url"""
    split_url = url.split('.')

    if len(split_url) == 3:
        return split_url[0].split('/')[-1]
    elif len(split_url) == 2 and 'localhost' in split_url[-1] :
        return split_url[0]
    return None

def validate_string(input_string) -> bool:
    """Валидация строки"""
    if len(input_string) < 32 and re.fullmatch(r'^[A-Za-z0-9_]+$', input_string):
        return True
    return False

def is_exists_template(template_id: int) -> bool:
    """Проверка на существование шаблона"""
    return template_id in [1, ]