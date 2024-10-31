from starlette.requests import Request

class CustomRequest(Request):
    def __init__(self, *args, **kwargs):
        self.subdomain = None
        super().__init__(*args, **kwargs)


async def get_custom_request(request: Request) -> CustomRequest:
    return CustomRequest(scope=request.scope, receive=request.receive)
