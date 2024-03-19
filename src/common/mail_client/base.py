from typing import Optional
from abc import ABC
from abc import abstractmethod

from src.database.schemas import AccountSchema


class AbstractClient(ABC):
    @abstractmethod
    async def fetch_data_post(self, url: str, headers: Optional[dict], json: Optional[dict]):
        pass

    @abstractmethod
    async def fetch_data_get(self, url: str, headers: Optional[dict]):
        pass

    @abstractmethod
    def _domain_verification(self, data: dict):
        pass

    @abstractmethod
    async def _get_domain(self):
        pass

    @abstractmethod
    async def _create_user_data(self):
        pass

    @abstractmethod
    async def create_account(self):
        pass

    @abstractmethod
    async def create_token(self, data: AccountSchema):
        pass

    @abstractmethod
    async def get_messages_all(self):
        pass

    @abstractmethod
    async def get_message_id(self, message_id: int):
        pass
