from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import asyncio
from buttplug import Client, WebsocketConnector
import logging

# ToDo: Is this real, am I real?




async def vibrate_all(client, time):
    print("Sending vibration...")
    for device_id, device in client.devices.items():
        for i in range(len(device.actuators)):
            await device.actuators[i].command(0.5)
            await asyncio.sleep(time)
            await device.actuators[i].command(0)


async def start(client):
    connector = WebsocketConnector("ws://127.0.0.1:12345", logger=client.logger)

    try:
        await client.connect(connector)
    except Exception as e:
        logging.error(f"Could not connect to server, exiting: {e}")

    await client.start_scanning()
    print("Scanning devices...")
    await asyncio.sleep(10)
    await client.stop_scanning()

    client.logger.info(f"Devices: {client.devices}")

    await vibrate_all(client, 1)


async def get_karma_from_html(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    text = soup.text
    text = text[0:text.find("total karma") - 1]
    text = text[text.rfind(" ") + 1:]
    text = text[text.rfind("a") + 1:]
    if text.find("menu") == -1:
        print("Karma not found.")
        return text
    else:
        return -1


async def wait_and_print_seconds(seconds):
    print("Sleeping...", end="")
    for i in range(seconds):
        print(" " + str(i + 1), end="")
        await asyncio.sleep(1)
    print()


async def login(page):
    await page.goto('https://web.yikyak.pro/login')
    print("Loading Page...")
    await page.is_visible("div.mt-5")
    print("Page Loaded.")
    phone_num = input("Please enter your phone number (for account verification):")
    await page.fill('input#phone', str(phone_num))
    await page.click('button[type=submit]')
    await page.is_visible('div.justify-center')
    code = input("Enter the Verification Code:")
    await page.fill('input#code', str(code))
    await page.click('button[type=submit]')
    print("Logging in...")
    await wait_and_print_seconds(5)
    await page.is_visible('div.bg-[#000000] p-1 rounded-full flex items-center')
    print("Logged in.")
    await page.goto('https://web.yikyak.pro/profile')
    print("Going to profile...")
    await page.is_visible('div.C')
    await wait_and_print_seconds(10)


async def get_karma(page):
    html = await page.inner_html('div')
    soup = BeautifulSoup(html, 'lxml')
    text = soup.text
    text = text[0:text.find("total karma") - 1]
    text = text[text.rfind(" ") + 1:]
    text = text[text.rfind("a") + 1:]
    if text.find("menu") != -1:
        return -1

    return int(text)


async def main():
    client = Client("YikYak Vibrator")
    await start(client)
    async with async_playwright() as p:
        web_browser = await p.chromium.launch()
        page = await web_browser.new_page()
        await login(page)

        last_karma = 0
        while True:
            karma = await get_karma(page)
            if karma == -1:
                karma = last_karma
            elif karma > last_karma:
                print("Karma Increased: ", end="")
                await vibrate_all(client, 1)
                last_karma = karma
            print(f"Karma: {str(karma)}")
            await page.reload()
            await wait_and_print_seconds(10)


asyncio.run(main(), debug=True)

