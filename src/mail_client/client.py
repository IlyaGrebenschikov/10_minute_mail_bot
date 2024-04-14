import time
from typing import Optional
from string import ascii_lowercase
from string import ascii_letters
from string import digits
from random import choice

import asyncio

from src.mail_client.client_session import (
    ClientSession,
    fetch_data_get,
    fetch_data_post
)


class MailClient:
    """
    docs https://docs.mail.gw/
    """
    def __init__(self):
        self.base_url = 'https://api.mail.gw/'

    def __domain_verification(self, data: dict) -> str:
        for elems in data['hydra:member']:
            if elems.get('isActive'):
                return elems.get('domain')

    async def __get_domain(self) -> str:
        client = ClientSession()
        for page in range(1, 11):
            link = f'{self.base_url}domains?page={page}'
            data = await fetch_data_get(client, link)
            verification = self.__domain_verification(data)

            if verification:
                return verification

    async def __create_user_data(self) -> dict:
        random_kit_username = ascii_lowercase + digits
        random_kit_password = ascii_letters + digits
        username = ''.join(choice(random_kit_username) for _ in range(10))
        domain = await self.__get_domain()
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
        return data

    async def create_account(self) -> Optional[dict]:
        client = ClientSession()
        link = f'{self.base_url}accounts'
        data = await self.__create_user_data()
        await fetch_data_post(client, link, json=data)
        return data

    async def create_token(self, user_data: dict[str, str]) -> Optional[dict]:
        client = ClientSession()
        link = f'{self.base_url}token'
        request = await fetch_data_post(client, link, json=user_data)
        token = request.get('token')
        return {'Authorization': f'Bearer {token}'}

    async def get_messages_all(self, token: dict, page: int = 1) -> dict:
        client = ClientSession(token)
        link = f'{self.base_url}messages?page={page}'
        request = await fetch_data_get(client, link)
        return request

    async def get_message_id(self, token: dict, message_id: str) -> dict:
        client = ClientSession(token)
        link = f'{self.base_url}messages/{message_id}'
        request = await fetch_data_get(client, link)
        return request


async def main():
    client = MailClient()
    account = await client.create_account()
    print(account)
    token = await client.create_token(account)
    print(token)
    while True:
        message = await client.get_messages_all(token)
        print(message)
        time.sleep(30)
        continue


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.run(main())