import asyncio
from playwright.sync_api import sync_playwright, expect

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        import os
        # Get the absolute path to the HTML file
        file_path = os.path.abspath('index.html')
        # Use a file:// URL to open the local HTML file
        page.goto(f'file://{file_path}')

        print(f"Initial scrollY: {page.evaluate('window.scrollY')}")

        # Click the "UI Designer" button
        page.click('#ui_button')

        # Wait for the scroll animation to finish
        page.wait_for_timeout(1000) # 800ms duration + 200ms buffer

        print(f"ScrollY after clicking UI button: {page.evaluate('window.scrollY')}")

        # Take a screenshot
        page.screenshot(path="jules-scratch/verification/screenshot_ui.png")

        # Click the "Music Producer" button
        page.click('#music_button')

        # Wait for the scroll animation to finish
        page.wait_for_timeout(1000) # 800ms duration + 200ms buffer

        print(f"ScrollY after clicking Music button: {page.evaluate('window.scrollY')}")

        # Take a screenshot
        page.screenshot(path="jules-scratch/verification/screenshot_music.png")

        browser.close()

if __name__ == "__main__":
    main()
