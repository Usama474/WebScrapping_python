import requests
import html5lib
import time
from bs4 import BeautifulSoup
import csv
coins=[]
url1= "https://www.amazon.com/3dRose-118876_4-Geeky-School-Pixels/dp/B013KTBWN6/ref=sr_1_2?keywords=data+scientist+shirts&qid=1639935227&sr=8-2"
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-61bf73d2-0a0d4bac5b7a441c64038c62"}
htlm_file= requests.get(url1, headers=headers );
content=htlm_file.content;

soap= BeautifulSoup(content, "html.parser")

i=0;
while (i<10):
    time.sleep(5)
    Title = soap.find(id= "productTitle").get_text()
    Price= soap.find( class_="a-offscreen").get_text()
    current= time.asctime(time.localtime());
    Column_title= ["Product Introduction", "Product Price", "Time of Recording"]
    Column_values= [Title, Price, current]
    with open("webscapped.csv", "a") as f:
        writer= csv.writer(f);
        writer.writerow(Column_title)
        writer.writerow(Column_values)
    i+=1;







