from typing import Optional

import aiohttp


class ClientSession:
    def __init__(
            self,
            headers: Optional[dict] = None,
            auth: Optional[dict] = None
    ) -> None:
        self.headers = headers
        self.auth = auth

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers=self.headers, auth=self.auth)
        return self.session

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()


async def fetch_data_get(client_session: aiohttp.ClientSession, url: str) -> Optional[dict]:
    async with client_session as session:
        async with session.get(url) as r:
            if r and r.status == 200:
                json_body = await r.json()
            else:
                raise Exception(r)
        return json_body


async def fetch_data_post(client_session: aiohttp.ClientSession, url: str, json: Optional[dict] = None) -> Optional[dict]:
    async with client_session as session:
        async with session.post(url, json=json) as r:
            if r and r.status in [200, 201]:
                json_body = await r.json()
            else:
                raise Exception(r)
        return json_body
