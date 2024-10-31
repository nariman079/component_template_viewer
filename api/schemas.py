from typing import Optional

from pydantic import BaseModel


class VPNDataCreate(BaseModel):
    template_id: int
    vpn_title: str

class VPNDataUpdate(BaseModel):
    template_id: Optional[int] = None
    vpn_title: Optional[str] = None
    header_title: Optional[str] = None
    header_description: Optional[str] = None
    header_image_url: Optional[str] = None
    opportunity_block_title: Optional[str] = None
    opportunity_1_title: Optional[str] = None
    opportunity_1_short_description: Optional[str] = None
    opportunity_2_title: Optional[str] = None
    opportunity_2_short_description: Optional[str] = None
    opportunity_3_title: Optional[str] = None
    opportunity_3_short_description: Optional[str] = None
    opportunity_4_title: Optional[str] = None
    opportunity_4_short_description: Optional[str] = None
    opportunity_5_title: Optional[str] = None
    opportunity_5_short_description: Optional[str] = None
    opportunity_6_title: Optional[str] = None
    opportunity_6_short_description: Optional[str] = None
    global_coverage_main_title: Optional[str] = None
    global_coverage_title: Optional[str] = None
    global_coverage_description: Optional[str] = None
    global_coverage_image_url: Optional[str] = None
    setup_security_title: Optional[str] = None
    setup_security_description: Optional[str] = None
    setup_security_image_url: Optional[str] = None
    start_bot_image_url: Optional[str] = None
    start_bot_button_url: Optional[str] = None
    challenge_title: Optional[str] = None
    challenge_short_description: Optional[str] = None
    challenge_background_image: Optional[str] = None
    license_description: Optional[str] = None