from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains

#browser = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(10)
browser.maximize_window()#最大化窗口
url = "https://degree.qingshuxuetang.com/hfgydx/Student/Home"
browser.get(url)
time.sleep(3)
browser.find_element_by_id('uname').send_keys('*******')
browser.find_element_by_id('pwd').send_keys('********')
browser.find_element_by_xpath('//*[@id="loginByPwdBtn"]').click()
time.sleep(3)#3是推迟执行的秒数

def multiwindowing():
    pass

def find(i,j):
    if i == 0 or i == 5:
        #j = j + 1
        id1 = 'kcjs_' + str(j)
        return id1
    elif i == 1 or i == 4:
        #j = j + 1
        return str(j)
    # elif i == 2:
    #     liss = [40317, 40318, 40319, 40320, 40321, 40325, 40326, 40327, 40328, 40329,
    #            40330, 40334, 40335, 40336, 40337, 40338, 40339, 40340, 40341, 40342,
    #            40343, 40344, 40348, 40349, 40350, 40351, 40352, 40353, 40354, 40355,
    #            40359, 40360, 40361, 40362, 40363, 40364, 40365, 40366, 40367, 40368,
    #            40369, 40370, 40371, 40372, 40373, 40374, 40375, 40376, 40380, 40381,
    #            40382, 40383, 40384, 40385, 40389, 40390, 40394, 40398, 40399]
    #     for id1 in liss:
    #         return id1
    # elif i == 3:
    #     if j != 1:
    #         browser.find_element_by_xpath('//*[@id="list"]/ul/li/a').click()#j=1时lis函数点击打开课程之后无需再点击当j=2时没有运行函数lis所以要进行点击打开课程目录
    #         time.sleep(1)
    #     #j = j + 1
    #     # if j == 1:
    #     #     pass
    #     # elif j == 2:
    #     #     pass
    #     id1 = browser.find_element_by_xpath('//*[@id="list"]/ul/li/ul/li/ul[1]/li/a[' + str(j) + ']').get_attribute('id')
    #     return id1


def lis1(i):
    if i == 0 or i == 5:
        lis = browser.find_elements_by_xpath('//*[@id="list"]/ul/li/ul[2]/li/a')
        return lis
    elif i == 1 or i == 4:
        lis = browser.find_elements_by_xpath('//*[@id="list"]/ul/li/ul/li/a')
        return lis
    elif i == 2:
        # browser.find_element_by_xpath('//*[@id="list"]/ul/li/a[2]').click()
        # time.sleep(1)
        #lis = [40315,40316,40317,40318,40319,40320,40321,40323,40324,40325,40326,40327,40328,40329,4033]
        # for w in range(1,10):
        #     lis = browser.find_elements_by_xpath('//*[@id="list"]/ul/li/ul[2]/li/ul[' + str(w) + ']/li')
        #     print("12345")
        lis = [40317, 40318, 40319, 40320, 40321, 40325, 40326, 40327, 40328, 40329,
         40330, 40334, 40335, 40336, 40337, 40338, 40339, 40340, 40341, 40342,
         40343, 40344, 40348, 40349, 40350, 40351, 40352, 40353, 40354, 40355,
         40359, 40360, 40361, 40362, 40363, 40364, 40365, 40366, 40367, 40368,
         40369, 40370, 40371, 40372, 40373, 40374, 40375, 40376, 40380, 40381,
         40382, 40383, 40384, 40385, 40389, 40390, 40394, 40398, 40399]
        return lis
    elif i == 3:#kcjs_1_1,
        lis = ['kcjs_1_2','kcjs_1_3','kcjs_1_4','kcjs_1_5','kcjs_1_6','kcjs_1_7',
               'kcjs_2_1','kcjs_2_2','kcjs_2_3','kcjs_2_4','kcjs_2_5','kcjs_2_6','kcjs_3_1',
               'kcjs_3_2','kcjs_3_3','kcjs_3_4','kcjs_3_5','kcjs_3_6','kcjs_3_7','kcjs_3_8',
               'kcjs_4_1','kcjs_4_2','kcjs_4_3','kcjs_4_4','kcjs_4_5','kcjs_4_6','kcjs_4_7',
               'kcjs_4_8','kcjs_4_9','kcjs_4_10','kcjs_4_11','kcjs_4_12','kcjs_4_13','kcjs_4_14',
               'kcjs_4_15','kcjs_4_16','kcjs_4_17','kcjs_4_18','kcjs_4_19','kcjs_4_20','kcjs_4_21',
               'kcjs_4_22','kcjs_5_1','kcjs_5_2','kcjs_5_3','kcjs_5_4','kcjs_5_5','kcjs_5_6','kcjs_5_7',
               'kcjs_5_8','kcjs_5_9','kcjs_5_10','kcjs_5_11','kcjs_5_12','kcjs_6_1','kcjs_6_2','kcjs_6_3',
               'kcjs_6_4','kcjs_6_5','kcjs_6_6','kcjs_6_7','kcjs_6_8','kcjs_6_9','kcjs_6_10','kcjs_6_11',
               'kcjs_6_12','kcjs_6_13','kcjs_6_14','kcjs_6_15','kcjs_6_16','kcjs_6_17','kcjs_6_18',
               'kcjs_6_19','kcjs_6_20','kcjs_6_21','kcjs_6_22','kcjs_6_23','kcjs_7_1','kcjs_7_2','kcjs_7_3',
               'kcjs_7_4','kcjs_7_5','kcjs_7_6','kcjs_7_7','kcjs_7_8','kcjs_7_9','kcjs_7_10','kcjs_7_11','kcjs_7_12',
               'kcjs_7_13','kcjs_7_14','kcjs_7_15','kcjs_8_1','kcjs_8_2','kcjs_8_3','kcjs_8_4']
    #     browser.find_element_by_xpath('//*[@id="list"]/ul/li/a').click()
    #     time.sleep(1)
    #     for w in range(1,9):
    #         lis = browser.find_elements_by_xpath('//*[@id="list"]/ul/li/ul/li/ul[' + str(w) + ']/li')
        return lis

def look(i,lis):
  for j in range(62,len(lis)):#第三课17讲
    #lit = browser.find_elements_by_xpath('//*[@id="list"]/ul/li/ul[2]/li/a/span[1]')[j].text
    print("准备播放《《《《《第" + str(i+1) + "课》》》》》")
    if i == 2:
        browser.find_element_by_xpath('//*[@id="list"]/ul/li/a[2]').click()
        time.sleep(1)
        id1 = str(lis[j])
    elif i == 3:
        browser.find_element_by_xpath('//*[@id="list"]/ul/li/a').click()
        time.sleep(1)
        id1 = lis[j]
    else:
        j = j + 1
        id1 = find(i, j)

    browser.find_element_by_id(id1).click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="playerContainer"]/div/div[10]/canvas').click()
    time1 = browser.find_element_by_xpath('//*[@id="playerContainer"]/div/div[2]/div[8]').get_attribute("innerText")#由于文本内容是隐藏的，所以用.text就会返回一个类型为str的空字符
    if time1[10] == ':':
      print("所需时间为：" + time1[8:10] + "分钟" + time1[11:] + "秒")
      time_s = int(time1[8:10])*60 + int(time1[11:]) + int(10)
    elif time1[11] == ':':
      print("所需时间为：" + time1[8:11] + "分钟" + time1[12:] + "秒")
      time_s = int(time1[8:11]) * 60 + int(time1[12:]) + int(10)
    print("当前时间为：" + time.ctime())
    print("》》》》》正在观看第" + str(j) + "讲中》》》》》共" + str(time_s) + "秒》》》》》" )
    time.sleep(time_s)
    print("《《《《《第" + str(j) + "讲》》》》》播放完成，准备进入下一讲》》》》》共" + str(len(lis)) + "讲》》》》》")
    browser.find_element_by_class_name('glyphicon-menu-left').click()
    time.sleep(3)
    continue

def a():
    for i in range(6):
        time.sleep(3)
        browser.find_elements_by_class_name('btn-lg')[i].click()  # 此处报列表超出索引范围是因为页面没有完全获取到需要休息几秒
        time.sleep(3)
        lis = lis1(i)
        look(i, lis)
        #还要点击首页回去
        print("《《《《《第" + str(i + 1) + "课》》》》》播放完成，准备进入下一课》》》》》")

def main():
    a()


if __name__ == '__main__':
    main()
