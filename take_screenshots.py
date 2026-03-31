from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8501/")
        print("Waiting for Streamlit to load...")
        time.sleep(5)  # wait for initial render

        print("Taking full page screenshot...")
        page.screenshot(path="screenshot_full.png", full_page=True)
        
        # Take a screenshot specifically of the tables section
        # We can just take a screenshot of the main section or the tables
        # Usually metrics and tables are visible near the top
        print("Taking tables screenshot...")
        # Since we just want the top part with metrics and maybe tables below it
        page.screenshot(path="screenshot_tables.png")

        print("Trying to capture PyVis graph area...")
        # Streamlit iframe containing PyVis
        iframe_element = page.locator("iframe").first
        if iframe_element.is_visible():
            iframe_element.screenshot(path="screenshot_pyvis.png")
        else:
            page.screenshot(path="screenshot_pyvis.png")

        # Now let's try to filter by "Эрон"
        print("Selecting Эрон...")
        try:
            # Streamlit sidebar is inside
            page.locator("text='Ҳама'").first.click()
            page.locator("text='Эрон'").nth(1).click() # It opens a listbox
            time.sleep(5)
            if iframe_element.is_visible():
                iframe_element.screenshot(path="screenshot_eron.png")
            else:
                page.screenshot(path="screenshot_eron.png")
        except Exception as e:
            print(f"Failed to select Эрон: {e}")

        # Now "Турон"
        print("Selecting Турон...")
        try:
            page.locator("text='Эрон'").first.click()
            page.locator("text='Турон'").first.click()
            time.sleep(5)
            if iframe_element.is_visible():
                iframe_element.screenshot(path="screenshot_turon.png")
            else:
                page.screenshot(path="screenshot_turon.png")
        except Exception as e:
            print(f"Failed to select Турон: {e}")
            
        browser.close()

if __name__ == "__main__":
    run()
