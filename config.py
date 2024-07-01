from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту

@dataclass
class PayToken:
    token: str
@dataclass
class PaysToken:
    token: PayToken
@dataclass
class Config:
    tg_bot: TgBot

# Создаем функцию, которая будет читать файл .env и возвращать экземпляр
# класса Config с заполненными полями token и admin_ids
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))

def load_pay_token(path: str | None = None) -> PaysToken:
    env = Env()
    env.read_env(path)
    return PaysToken(token=PayToken(token=env('PAYMENT_TOKEN')))