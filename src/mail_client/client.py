import time
from typing import Optional
from string import ascii_lowercase
from string import ascii_letters
from string import digits
from random import choice
from pprint import pprint

import aiohttp
import asyncio

from src.common.mail_client import AbstractClient
from src.database.schemas import AccountSchema


class MailClient(AbstractClient):
    """
    docs https://docs.mail.gw/
    """
    def __init__(self):
        self.base_url = 'https://api.mail.gw/'
        self.user_token = Optional[dict]
        self.user_data = Optional[dict]

    async def fetch_data_post(
            self,
            url: str,
            headers: Optional[dict] = None,
            json: Optional[dict] = None,
            auth: Optional[dict] = None
    ) -> Optional[dict]:
        async with aiohttp.ClientSession(headers=headers, auth=auth) as session:
            async with session.post(url, json=json) as r:
                if r and r.status in [200, 201]:
                    json_body = await r.json()
                else:
                    raise Exception(r)
            return json_body

    async def fetch_data_get(self, url: str, headers: Optional[dict] = None) -> Optional[dict]:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as r:
                if r and r.status == 200:
                    json_body = await r.json()
                else:
                    raise Exception(r)
            return json_body

    def _domain_verification(self, data: dict) -> str:
        for elems in data['hydra:member']:
            if elems.get('isActive'):
                return elems.get('domain')

    async def _get_domain(self) -> str:
        for page in range(1, 11):
            link = f'{self.base_url}domains?page={page}'
            data = await self.fetch_data_get(link)
            verification = self._domain_verification(data)

            if verification:
                return verification

    async def _create_user_data(self) -> dict:
        random_kit_username = ascii_lowercase + digits
        random_kit_password = ascii_letters + digits
        username = ''.join(choice(random_kit_username) for _ in range(10))
        domain = await self._get_domain()
        adress = f'{username}@{domain}'
        while True:
            password = ''.join(choice(random_kit_password) for _ in range(20))
            if (sum(c.islower() for c in password) >= 4
                    and sum(c.isupper() for c in password) >= 4
                    and sum(c.isdigit() for c in password) >= 4):
                break
        data = {
            'address': adress,
            'password': password,
        }
        self.user_data = data
        return data

    async def create_account(self) -> Optional[dict]:
        link = f'{self.base_url}accounts'
        data = await self._create_user_data()
        request = await self.fetch_data_post(link, json=data)
        return request

    async def create_token(self) -> Optional[dict]:
        link = f'{self.base_url}token'
        data = self.user_data
        request = await self.fetch_data_post(link, json=data)
        self.user_token = {"Authorization": f'Bearer {request.get("token")}'}   # todo переписать под редис, в репозитории
        return request

    async def get_messages_all(self, token: dict, page: int = 1) -> dict:
        link = f'{self.base_url}messages?page={page}'
        request = await self.fetch_data_get(link, token)
        return request

    async def get_message_id(self, token: dict, message_id: str) -> dict:
        link = f'{self.base_url}messages/{message_id}'
        request = await self.fetch_data_get(link, token)
        return request


async def main():
    client = MailClient()
    user = await client.create_account()
    data = client.user_data
    token = await client.create_token()
    token_data = client.user_token
    messages = await client.get_messages_all(token_data)
    # pprint(user)
    pprint(data)
    print(token_data)
    # pprint(token)
    pprint(messages)


async def second():
    client = MailClient()
    token = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3MTE1MTMxMzUsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJ1c2VybmFtZSI6InF0aXBncm91eHFAbWF4YW1iYS5jb20iLCJpZCI6IjY2MDM5ZTJmMDkzNGUxMDJmMjE2MWFhNiIsIm1lcmN1cmUiOnsic3Vic2NyaWJlIjpbIi9hY2NvdW50cy82NjAzOWUyZjA5MzRlMTAyZjIxNjFhYTYiXX19.whdJSa5tZeJkZ7bEX2wuhJA_Uc4wdbriVu_Kv1Iw4swDR8KD4T2yerlJr4QotIfMgTEVCUGuBrQZgGix4mA4Kg'}
    messages = await client.get_messages_all(token)
    message_id = await client.get_message_id(token, '66039e515658baa442b4e27e')
    pprint(messages)
    pprint(message_id)

if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.run(second())