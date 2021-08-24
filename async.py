import asyncio
import requests


class ServerError(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'ServerError status code: {self.message}' if self.message else 'ServerError'


class ClientError(ServerError):
    def __str__(self):
        super(ClientError, self).__str__()
        return f'ClientError status code: {self.message}' if self.message else 'ClientError'


async def get_status(res):
    response = await res
    if response.status_code == 200:
        with open(f'Cats/{response.url[-7:]}', 'wb') as img:
            img.write(response.content)
            print(f'Done - {response.url[-7:]}')
    elif 400 <= response.status_code < 500:
        raise ClientError(f'{response.status_code}')
    elif 500 <= response.status_code < 527:
        raise ServerError(f'{response.status_code}')
    response.close()


async def main():
    tasks = []
    for i in range(10, 30):
        tasks.append(asyncio.ensure_future(
            get_status(
                loop.run_in_executor(None, requests.get, f'https://cdn2.thecatapi.com/images/d{i}.jpg')
            )))
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
