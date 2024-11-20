from sqlalchemy import String, Text, VARCHAR, Integer
from sqlalchemy.orm import Mapped, mapped_column
from api.database import Base


class VPNData(Base):
    __tablename__ = 'vpn_data'

    id: Mapped[int] = mapped_column(primary_key=True)
    template_id: Mapped[int] = mapped_column(nullable=False, default=1)
    domain: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    bot_name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    header_title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Скорость и свобода в одном VPN"
    )
    header_description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="Оцените нашу мощь с бесплатной пробной подпиской!"
    )
    header_image_url: Mapped[str | None] = mapped_column(VARCHAR(2048), nullable=True)
    opportunity_block_title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Быстрый, безопасный и доступный VPN для всех ваших нужд."
    )
    opportunity_1_title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Молниеносная скорость"
    )
    opportunity_1_short_description: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Минимальная задержка и высокая скорость."
    )
    opportunity_2_title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Выгодная цена"
    )
    opportunity_2_short_description: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Максимальная защита по выгодной стоимости."
    )
    opportunity_3_title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Надежная защита"
    )
    opportunity_3_short_description: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Используем передовые методы шифрования."
    )
    opportunity_4_title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="До 3-x устройств"
    )
    opportunity_4_short_description: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Подключи все свои устройства."
    )
    opportunity_5_title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Никакой рекламы"
    )
    opportunity_5_short_description: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Наш VPN блокирует до 95% реклам на YouTube и по всему интернету."
    )
    opportunity_6_title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Легкость"
    )
    opportunity_6_short_description: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Управляйте через Telegram"
    )
    global_coverage_main_title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Глобальное покрытие"
    )
    global_coverage_title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Свобода интернета по всему миру"
    )
    global_coverage_description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="""С нашим VPN вы получаете доступ к сети из более чем 100 стран,
            обеспечивая непрерывное соединение и доступ 
            к контенту без географических ограничений, где бы вы ни находились."""
    )
    global_coverage_image_url: Mapped[str | None] = mapped_column(VARCHAR(2048), nullable=True)

    setup_security_title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Все устройства под защитой"
    )
    setup_security_description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="Наш VPN совместим с любой операционной системой – Windows,"
                " macOS, iOS, Android и Linux. Оставайтесь в безопасности, "
                "независимо от того, какое устройство вы используете."
    )
    setup_security_image_url: Mapped[str | None] = mapped_column(VARCHAR(2048), nullable=True)
    start_bot_image_url: Mapped[str | None] = mapped_column(VARCHAR(2048), nullable=True)
    start_bot_image_url_2: Mapped[str | None] = mapped_column(VARCHAR(2048), nullable=True)
    start_bot_button_url: Mapped[str] = mapped_column(
        VARCHAR(2048),
        nullable=False,
        default="tm.ru"
    )
    challenge_title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Испытайте VPN бесплатно"
    )
    challenge_short_description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="Начните с бесплатного пробного периода на 30 дней и оцените все преимущества нашего сервиса!"
    )
    challenge_background_image: Mapped[str | None] = mapped_column(VARCHAR(2048), nullable=True)
    license_description: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="© 2024 FlyVpn. Все права защищены"
    )
