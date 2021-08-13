import asyncio
import requests


async def get_status(res):
    response = await res
    if response.status_code == 200:
        with open(f'Cats/{response.url[-7:]}', 'wb') as img:
            img.write(response.content)
            print(f'Done - {response.url[-7:]}')
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
