"""Screenshot script: capture all pages of the ad-video-product app."""
import asyncio
import os

async def main():
    from playwright.async_api import async_playwright

    HTML_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app', 'index.html'))
    HTML_URI = 'file://' + HTML_PATH
    OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs', 'images')
    os.makedirs(OUT_DIR, exist_ok=True)

    # Pages to capture: (pageId, filename, description, js_before_screenshot)
    pages = [
        ('login', 'login.png', 'Login page', ''),
        ('dashboard', 'dashboard.png', 'Dashboard page', ''),
        # Enter project first, then navigate
        ('brief', 'brief.png', 'Brief page', ''),
        ('style', 'style.png', 'Style page', ''),
        ('script', 'script.png', 'Script page', ''),
        ('storyboard', 'storyboard.png', 'Storyboard page', ''),
        ('export', 'export.png', 'Export page', ''),
        ('export-rendering', 'export-rendering.png', 'Export rendering state',
         'window.renderState = "rendering";'
         'var btn = document.getElementById("exportMainBtn");'
         'btn.classList.remove("btn-blue","btn-red");'
         'btn.classList.add("btn-loading");'
         'btn.innerHTML = \'<div class="spinner" style="width:1rem;height:1rem;border-color:oklch(1 0 0 / 30%);border-top-color:#fff;"></div> 渲染中... 67%\';'
         'document.getElementById("rqTikTokProgressWrap").style.display = "";'
         'document.getElementById("complianceCard").style.display = "none";'
         'document.getElementById("rqTikTokProgress").style.width = "67%";'
         'document.getElementById("rqTikTokDesc").textContent = "渲染中... 67%";'),
        ('export-done', 'export-done.png', 'Export done state',
         'window.renderState = "done";'
         'var btn = document.getElementById("exportMainBtn");'
         'btn.classList.remove("btn-loading","btn-red");'
         'btn.classList.add("btn-blue");'
         'btn.innerHTML = \'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:1rem;height:1rem;"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> 下载视频\';'
         'document.getElementById("rqTikTokProgressWrap").style.display = "";'
         'document.getElementById("complianceCard").style.display = "";'
         'document.getElementById("rqTikTokStatus").textContent = "✓";'
         'document.getElementById("rqTikTokStatus").style.background = "oklch(0.55 0.15 160 / 12%)";'
         'document.getElementById("rqTikTokStatus").style.color = "oklch(0.65 0.12 160)";'
         'document.getElementById("rqTikTokDesc").textContent = "已完成 · 8.7 MB";'
         'document.getElementById("rqTikTokProgress").style.width = "100%";'),
        ('export-error', 'export-error.png', 'Export error state',
         'window.renderState = "error";'
         'var btn = document.getElementById("exportMainBtn");'
         'btn.classList.remove("btn-loading","btn-blue");'
         'btn.classList.add("btn-red");'
         'btn.innerHTML = \'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:1rem;height:1rem;"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg> 重试\';'
         'document.getElementById("rqTikTokStatus").textContent = "✕";'
         'document.getElementById("rqTikTokDesc").textContent = "渲染失败，请重试";'),
    ]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        await page.goto(HTML_URI, wait_until='networkidle')
        await asyncio.sleep(0.5)

        for i, (page_id, filename, desc, js_before) in enumerate(pages):
            print(f'[{i+1}/{len(pages)}] Capturing {desc} ({page_id})...')

            if page_id == 'login':
                await page.evaluate('sessionStorage.removeItem("adcrafLoggedIn"); location.reload();')
                await page.wait_for_load_state('networkidle')
                await asyncio.sleep(0.5)
            elif page_id == 'dashboard':
                await page.evaluate('sessionStorage.setItem("adcrafLoggedIn", "1"); document.getElementById("loginPage").classList.add("hidden"); document.querySelector(".app-shell").style.display = ""; document.body.classList.add("dashboard-mode"); switchPage("dashboard");')
                await asyncio.sleep(0.3)
            elif page_id.startswith('export-'):
                # Navigate to export first, then apply state
                await page.evaluate('sessionStorage.setItem("adcrafLoggedIn", "1"); document.getElementById("loginPage").classList.add("hidden"); document.querySelector(".app-shell").style.display = ""; enterProject("Test Project", "export")')
                await asyncio.sleep(0.3)
                if js_before:
                    await page.evaluate(js_before)
                    await asyncio.sleep(0.2)
            else:
                # Enter project and navigate
                await page.evaluate(f'sessionStorage.setItem("adcrafLoggedIn", "1"); document.getElementById("loginPage").classList.add("hidden"); document.querySelector(".app-shell").style.display = ""; enterProject("Test Project", "{page_id}")')
                await asyncio.sleep(0.3)

            out_path = os.path.join(OUT_DIR, filename)
            await page.screenshot(path=out_path, full_page=False)
            print(f'  ✓ Saved: {out_path}')

        await browser.close()
        print(f'\nDone! {len(pages)} screenshots saved to {OUT_DIR}')

if __name__ == '__main__':
    asyncio.run(main())
