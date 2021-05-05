import StockChecker
import time
import threading

def start(url,limitPrice):
    buyer = StockChecker.AutoBuy(url,limitPrice)
    buyer.logIn()
    buyer.infiniteCheck()
    buyer.tem()

purpleShampoo="https://www.amazon.com/Purple-Shampoo-Blonde-Hair-Toner/dp/B07W2W88MW/ref=sr_1_4?dchild=1&keywords=purple+shampoo+maple&qid=1613318203&sr=8-4"
gigRTX3080="https://www.amazon.com/gp/product/B08HJTH61J?smid=ATVPDKIKX0DER&psc=1&linkCode=sl1&tag=galaxy045-20&linkId=b0c3bb40e1581fb9ab86487a0b2d5e70&ref_=as_li_ss_tl"
asusRTX3080="https://www.amazon.com/dp/B08HH5WF97?&linkCode=sl1&tag=galaxy045-20&linkId=2161060510c80853601a9560aa08e1e3&ref_=as_li_ss_tl"
asus30701="https://www.amazon.com/dp/B08MT6B58K/ref=&tag=galaxy045-20&olp_aod_redir#aod"
asus30702="https://www.amazon.com/dp/B08L8LG4M3/ref=&tag=galaxy045-20&olp_aod_redir#aod"
gb3070="https://www.amazon.com/dp/B08M14Y3C7?&linkCode=sl1&tag=galaxy045-20&linkId=c9c0d7632b07cebe414471649341211a&ref_=as_li_ss_tl"
url3080List=[]
url3070List=[]
url3080List.append(gigRTX3080)
url3080List.append(asusRTX3080)
#url3070List.append(asus30701)
#url3070List.append(asus30702)
url3070List.append(gb3070)
threadList = []
try:
    for i in url3080List:
        t = threading.Thread(target=start, args=(i,900,))
        t.start()
        threadList.append(t)
    for i in url3070List:
        t = threading.Thread(target=start, args=(i,800,))
        t.start()
        threadList.append(t)
except:
    print("threads didnt start")