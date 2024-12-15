


from playwright.sync_api import sync_playwright

from selectolax.parser import HTMLParser


def getHtml(websiteUrl,showbrowser=True,screenshotName=''):

    with sync_playwright() as p:
        browser =p.chromium.launch(headless=not showbrowser)
        page = browser.new_page()
        page.goto(url=websiteUrl)

        page.wait_for_load_state('networkidle')
        page.wait_for_load_state('domcontentloaded')
        page.wait_for_timeout(1000)

        page.screenshot(full_page=True,path='./{screenshotName}.png')

        pageHtml = page.inner_html('body')

        pageData = HTMLParser(pageHtml)

        return pageData
        

