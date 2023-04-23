from selenium import webdriver


def run_chrome_webdriver(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False})
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option('detach', True)  #不自动关闭浏览器
    options.add_argument('--start-maximized')  #浏览器窗口最大化
    wd = webdriver.Chrome(options=options)
    wd.get(url)
    return wd
