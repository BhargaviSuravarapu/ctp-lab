import asyncio
import aiohttp
import time


urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net"
]


async def fetch(session, url):
    for attempt in range(3):
        try:
            async with session.get(url, timeout=10) as response:
                text = await response.text()
                return url, response.status, len(text)

        except Exception as e:
            if attempt == 2:
                return url, "Failed", 0

            await asyncio.sleep(1)


async def crawler():
    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *(fetch(session, url) for url in urls)
        )

    end = time.perf_counter()

    for result in results:
        print(result)

    print("Async Time:", end - start)


asyncio.run(crawler())