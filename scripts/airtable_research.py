"""
Research script used to investigate the Airtable backend
behind Layoffs.fyi.

Achievements:
- Identified hidden Airtable endpoint
- Captured authenticated requests
- Automated browser access using Playwright
- Investigated MessagePack response format

Final project uses exported/public dataset instead of
direct Airtable extraction.
"""
from playwright.sync_api import sync_playwright

def handle_response(response):

    if "readSharedViewData" in response.url:

        print("\nFOUND DATA!")
        print("URL:", response.url)

        try:

            print("Trying to get body...")

            data = response.body()

            print("Body received!")

            with open("airtable_response.msgpack", "wb") as f:
                f.write(data)

            print("Saved!")
            print("Bytes:", len(data))

        except Exception as e:
            print("ERROR:", e)


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.on("response", handle_response)

    print("Opening Airtable...")

    page.goto(
        "https://airtable.com/embed/app1PaujS9zxVGUZ4/shroKsHx3SdYYOzeh?backgroundColor=green&viewControls=on"
    )


    browser.close()