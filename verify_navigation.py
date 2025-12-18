
import asyncio
from playwright.async_api import async_playwright

async def main():
    urls = [
        "http://localhost:8000/index.html",
        "http://localhost:8000/audit.html",
        "http://localhost:8000/partners.html",
        "http://localhost:8000/portal.html",
        "http://localhost:8000/home.html",
        "http://localhost:8000/landlord.html",
    ]
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for i, url in enumerate(urls):
            await page.goto(url)
            await page.screenshot(path=f"screenshot_{i}.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
