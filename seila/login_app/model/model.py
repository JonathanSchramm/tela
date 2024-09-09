import pandas as pd
from playwright.sync_api import sync_playwright

class Model:
    def validate_login(self, username, password):
        login_url = 'https://auth.dio.me/realms/master/protocol/openid-connect/auth?client_id=spa-core-client&redirect_uri=https%3A%2F%2Fweb.dio.me%2F&state=b6181033-9f69-4928-ad85-63215781c625&response_mode=fragment&response_type=code&scope=openid&nonce=9706266a-6844-415d-ac52-d4b505234f05'
        username_selector = '#username'
        password_selector = '#password'
        submit_selector = '#kc-login'
        success_selector = '.sc-cWSHoV.gufarm'

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            page.goto(login_url)
            page.fill(username_selector, username)
            page.fill(password_selector, password)
            page.click(submit_selector)

            try:
                page.wait_for_selector(success_selector, timeout=30000)
                browser.close()
                return True
            except Exception as e:
                print(f"Erro ao verificar login: {e}")
                browser.close()
                return False

    def read_csv(self, file_path):
        try:
            df = pd.read_csv(file_path)
            return df
        except Exception as e:
            print(f"Erro ao ler o arquivo CSV: {e}")
            return None
