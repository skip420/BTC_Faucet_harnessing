#install pytesseract
# install pillow
# install selenium
# install chrome browser and chrome driver
# install python-requests
# install python-pyquery
# install opencv

# This code will harness free btc every 5 minutes and auto grabs captcha text from image using OCR 98% success rate, all captcha grab auto inputs image into the same directory and fills the font work into the terminal,(Chrome browser will automatically open) sit back and relax :)
# there is also an added bonus here in the code which will also automatically show balance from any wallet or current wallet you use.

#Donation all are welcome,We too LOVE COFFEE ,Lavazza is much regarded as our soul thinker
# 16VVng4HpSvtFjxmTiRnms2iWhgZt3wx5W 







from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pytesseract
import time
import cv2
import requests
from pyquery import PyQuery

BTCwalletAddress = ['112vq8eT295ekWeuNzyeKbGYbvAsAZYZGu']

def GetBalance():
    for x in range(len(BTCwalletAddress)):
          Url = 'http://5minutebitcoin.com/check-balance/?the99btcbfaddress=' + BTCwalletAddress[x]
          r = requests.get(Url, timeout=60)
          responseData = r.content

          # Parse out Proxy IP addresses and ports
          html = responseData
          pq = PyQuery(html)
          tag = pq('div')
          Links = tag.text()
          tmp = Links.split(' ')
          print tmp[40]

GetBalance()


def haveTimer():
    # Check to see if there is an active 5 minute timer
    try:
        timerText = driver.find_elements_by_class('timer')
     
        return True
    except:
           return False
    #<div class="timer" data-seconds="300" data-sound="http://5minutebitcoin.com/wp-content/plugins/99bitcoins-btc-faucet/assets/beep.wav">4:32</div>

def SolveCaptcha(filename):
    image_obj = cv2.imread(filename)
    gray = cv2.cvtColor(image_obj, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(filename, gray)

    CaptchaText = pytesseract.image_to_string(Image.open(filename), lang="eng", config='--psm 6 --oem 1')

    # Sometimes the captcha words are split on two lines remove the newline or return characters
    CaptchaText = CaptchaText.replace("\n", " ")
    CaptchaText = CaptchaText.replace("\r", "")

    # Sometimes the screen capture wasn't quite perfect and we got some of the SolveMedia icon texts
    CaptchaText = CaptchaText.replace("Your Answer SOLVE media", "")

    # Get rid of any white space to the left or right of the captcha words
    CaptchaText.rstrip()
    CaptchaText.lstrip()


    # Commonly miss-detected characters are not letters - so let's translate
    CaptchaText = CaptchaText.replace("|", "i")

    print "Captcha Solution: " + CaptchaText
    return CaptchaText

def ExtractImage():
    element = driver.find_element_by_id("adcopy-puzzle-image-image")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    img_file = 'captcha-' + BotID + '.png'
    driver.save_screenshot(img_file)

    img = Image.open(img_file)
    area = (95, 18, 392, 148)
    cropped_img = img.crop(area)
    cropped_img.save(img_file)

    return img_file

#Kay@wechat_BTC_ADDRESS
EthAddress  = ''
BtcAddress  = '1AKABouYu88Kx179Z33KweaXJ6ddS2rEWK'
ClaimsCount = 0
BotID       = '001'


options = webdriver.ChromeOptions()
#options.add_argument('--user-data-dir=~/Desktop/webdriver-test')
#options.add_argument('Android 5.1')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-web-security')
options.binary_location = '/usr/bin/chromium-browser'
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(300,265)
driver.set_window_position(0, 0)

#driver.get('http://affi.cryptoplanets.org/ethcollector/index.php')
driver.get('http://5minutebitcoin.com/')

print haveTimer()
if(haveTimer == True):
   time.sleep(5)
else:
    CaptchaSolution = SolveCaptcha(ExtractImage())

    btcAddressText = driver.find_elements_by_name('address')
    SolveMediaText = driver.find_elements_by_name('adcopy_response')
    btcAddressText[0].send_keys(BtcAddress)
    SolveMediaText[0].send_keys(CaptchaSolution)
    driver.find_element_by_name('claim_coins').click()

def main():
    while(x):
         # Check to see if there is currently an active timer
         if(haveTimer() == True):
            # Make sure the BTC Address is filled out
            btcAddressText[0].send_keys(BtcAddress)

            # Extract the Captcha Image
            ExtractImage()

            Result = SolveCaptcha(img)

            SolveMediaText[0].send_keys(Result)

            # Click Claim
            driver.find_element_by_name('claim_coins').click()

         else:
              # Set a wait timer for the remaining time of the faucet
              time.wait(RemainingTime)
