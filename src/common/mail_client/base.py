from typing import Optional
from abc import ABC
from abc import abstractmethod

from src.database.schemas import AccountSchema


class AbstractClient(ABC):
    def __init__(self):
        self.base_url: str
        self.user_token: Optional[str]

    @abstractmethod
    async def fetch_data_post(self, url: str):
        pass

    @abstractmethod
    async def fetch_data_get(self, url: str):
        pass

    @abstractmethod
    def _domain_verification(self, data: dict):
        pass

    @abstractmethod
    async def get_domain(self):
        pass

    @abstractmethod
    def _create_user_data(self, data: AccountSchema):
        pass

    @abstractmethod
    async def create_account(self, data: AccountSchema):
        pass

    @abstractmethod
    async def get_token(self, data: AccountSchema):
        pass

    @abstractmethod
    async def get_messages_all(self):
        pass

    @abstractmethod
    async def get_message_id(self, message_id: int):
        pass
