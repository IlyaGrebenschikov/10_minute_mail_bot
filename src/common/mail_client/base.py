from typing import Optional
from abc import ABC
from abc import abstractmethod


class AbstractClient(ABC):
    @abstractmethod
    async def fetch_data_post(self, **kwargs):
        pass

    @abstractmethod
    async def fetch_data_get(self, **kwargs):
        pass

    @abstractmethod
    def _domain_verification(self, **kwargs):
        pass

    @abstractmethod
    async def _get_domain(self, **kwargs):
        pass

    @abstractmethod
    async def _create_user_data(self, **kwargs):
        pass

    @abstractmethod
    async def create_account(self, **kwargs):
        pass

    @abstractmethod
    async def create_token(self, **kwargs):
        pass

    @abstractmethod
    async def get_messages_all(self, **kwargs):
        pass

    @abstractmethod
    async def get_message_id(self, **kwargs):
        pass
