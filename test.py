from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

##################################################################################
# 1. 계좌잔고 조회
##################################################################################
def account():
    # 농협비즈 사이트 접속
    driver.get("https://ibz.nonghyup.com/")

    # 링크 찾아서 클릭
    continue_link = driver.find_element(By.LINK_TEXT, '빠른조회')
    continue_link.click()

##################################################################################
# 2. 문자 발송
##################################################################################
def send_message():
    # 문자나라 사이트 접속
    driver.get("https://www.munjanara.co.kr/")

    # 로그인
    id = driver.find_element(By.id, 'userid')
    id.value
    
##################################################################################
# 3. 홈텍스 집계
##################################################################################    
def hometax():
    # 홈텍스 사이트 접속
    driver.get("https://www.hometax.go.kr/websquare/websquare.wq?w2xPath=/ui/pp/index_pp.xml&tmIdx=0&tm2lIdx=100907&tm3lIdx=")

    # 로그인
    # userid = driver.find_element(By.CLASS_NAME, 'w2textbox') # span class
    # try:
    # 상단 로그인 버튼 클릭
    userid = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.ID, 'textbox915')
                    )
                )
        # userid = driver.find_element(By.id, 'textbox915') # a link class
        # driver.find_element(By.id, 'textbox915').click()
    userid.click()
    
    # 로그인 페이지내 프레임 전환
    # iframe = driver.find_element(By.CSS_SELECTOR, '#txppIframe.w2iframe')
    iframe = driver.find_element(By.ID, 'txppIframe')
    driver.switch_to.frame(iframe)
    
    # 아이디 로그인 클릭
    # driver.find_element(By.ID, 'anchor15').click()
    id_login = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.ID, 'ckbBaseApp_input_0')
                    )
                )
    id_login.click()
    # <input type="checkbox" class="w2checkbox_input" name="ckbBaseApp_input" data-index="0" id="ckbBaseApp_input_0">
    
        # userid.send_keys(Keys.ENTER) # 여전히 에러
        # driver.execute_script("arguments[0].click();", userid)
     
    # except TimeoutException as e:
    # except:
    #     print("요소를 찾을 수 없거나 로딩에 시간이 너무 오래 걸립니다.")
        
    # finally:
        # 브라우저 종료
        # driver.quit()
        
    
        
if __name__ == "__main__" :
    hometax()
    while True:
        pass

# driver.quit()
