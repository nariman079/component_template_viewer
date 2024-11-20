from fastapi import HTTPException
from pydantic import BaseModel, Field, field_validator
from starlette.status import HTTP_400_BAD_REQUEST

from api.utils import validate_string

class VPNDataCreate(BaseModel):
    template_id: int = Field(
        default=1, description="ID Шаблона",
    )
    title: str = Field(
        default="FlyVpn", description="Название для VPN лендига "
    )
    domain: str = Field(
        description="Domain для VPN, {domain}.vpn-bot.me"
    )
    bot_name: str = Field(
        default="creator_vpn_bot", description="botname от телегама"
    )

    @field_validator("domain")
    def validate_data(cls, value):
        domain = value
        if not validate_string(domain):
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Домен может содержать только английские буквы, цифры от 0 до 9 и "
                       "символ _. Общая длина не должна превышать 32 символа."
                       " Например: my_domain_12."
            )
        return value

    @field_validator("bot_name")
    def validate_bot_name(cls, value):
        bot_name = value
        if not validate_string(bot_name):
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Домен может содержать только английские буквы, цифры от 0 до 9 и "
                       "символ _. Общая длина не должна превышать 32 символа."
                       " Например: my_create_bot_12."
            )
        return value


class VPNDataUpdate(BaseModel):
    template_id: int | None = None
    title: str | None = None
    header_title: str | None = None
    header_description: str | None = None
    opportunity_block_title: str | None = None
    opportunity_1_title: str | None = None
    opportunity_1_short_description: str | None = None
    opportunity_2_title: str | None = None
    opportunity_2_short_description: str | None = None
    opportunity_3_title: str | None = None
    opportunity_3_short_description: str | None = None
    opportunity_4_title: str | None = None
    opportunity_4_short_description: str | None = None
    opportunity_5_title: str | None = None
    opportunity_5_short_description: str | None = None
    opportunity_6_title: str | None = None
    opportunity_6_short_description: str | None = None
    global_coverage_main_title: str | None = None
    global_coverage_title: str | None = None
    global_coverage_description: str | None = None

    setup_security_title: str | None = None
    setup_security_description: str | None = None

    challenge_title: str | None = None
    challenge_short_description: str | None = None
    license_description: str | None = None


