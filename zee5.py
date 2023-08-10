import time

from seleniumwire import webdriver
from selenium_stealth import stealth

def driver_options():    
    brave_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    options = webdriver.ChromeOptions()
    options.binary_location = brave_path

    options.add_argument("--headless");
    options.add_argument("--ignore-certificate-errors");
    options.add_argument("--no-sandbox");

    return options

def get_chrome_capabilities():
    caps = webdriver.DesiredCapabilities.CHROME
    caps['acceptSslCerts'] = True
    caps['acceptInsecureCerts'] = True
    opts = webdriver.ChromeOptions()
    caps.update(opts.to_capabilities())
    return caps

def zee5_scrapper(url, timeout=30):   
        
    driver = webdriver.Chrome(options=driver_options())

    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    stealth(
        driver=driver,
        user_agent = agent,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    TARGET_URL = "https://www.zee5.com/global/tv-shows/details/jodha-akbar/0-6-1516/jodha-akbar-episode-266/0-1-manual_158oht2ql3g0"

    proto = "https://"
    host= "zee5vodnd.akamaized.net"

    driver.get(url)

    time.sleep(int(timeout))

    zee5_media_urls = []
    print("=====> HTTP <=====")
    print("Response  :")
    getted_media = 0
    for req in driver.requests: 
        if getted_media >= 5:
            break

        if req.host == host:
            zee5_media_urls.append(req.url)
            print(req.url)
            getted_media = getted_media + 1
            
    print("<================>")

    driver.quit()

    return zee5_media_urls

