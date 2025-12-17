
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Navigate to the home page
        await page.goto("http://localhost:8000/home.html")
        await page.screenshot(path="/home/jules/verification/home_page.png")

        # Click the "Federal Audit" link
        await page.click('a[href="audit.html"]')
        await page.wait_for_url("http://localhost:8000/audit.html")
        await page.screenshot(path="/home/jules/verification/audit_from_home.png")

        await browser.close()

asyncio.run(main())
