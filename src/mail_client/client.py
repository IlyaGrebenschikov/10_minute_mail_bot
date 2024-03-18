from typing import Optional
from pprint import pprint

import aiohttp
import asyncio

from src.common.mail_client import AbstractClient
from src.database.schemas import AccountSchema


class MailClient(AbstractClient):
    def __init__(self):
        self.base_url = 'https://api.mail.gw/'
        self.user_token = None

    async def fetch_data_post(self, url: str, headers: Optional[dict] = None, json: Optional[dict] = None):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(url, json=json) as r:
                if r and r.status == 201:
                    json_body = await r.json()
                else:
                    raise Exception(r)
            return json_body

    async def fetch_data_get(self, url: str, headers: Optional[dict] = None):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as r:
                if r and r.status == 200:
                    json_body = await r.json()
                else:
                    raise Exception(r)
            return json_body

    def _domain_verification(self, data: dict):
        pass

    async def get_domain(self):
        pass

    def _create_user_data(self, data: AccountSchema):
        pass

    async def create_account(self, data: AccountSchema):
        pass

    async def create_token(self, data: AccountSchema):
        pass

    async def get_messages_all(self):
        pass

    async def get_message_id(self, message_id: int):
        pass


if __name__ == '__main__':
    async def main():
        client = MailClient()
        get_q = await client.fetch_data_get(url='https://api.mail.gw/domains')
        post_q = ...
        pprint(get_q)

    asyncio.run(main())

