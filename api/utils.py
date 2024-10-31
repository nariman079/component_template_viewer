async def get_subdomain(url: str) -> str | None:
    """Получение поддомена с url"""
    split_url = url.split('.')
    if len(split_url) == 3:
        return split_url[0].split('/')[-1]
    return None