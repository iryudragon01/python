import requests,csv,concurrent.futures,time

httpslist=[]
with open('list.csv','r') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            text = row[0].replace('"','')+":"+row[7].replace('"','')
            httpslist.append(text)
    except:
        pass        


def th(pp):
    print(pp)
def extract(proxy):
    try:
        r= requests.get('https://youtube.com',proxies={'http':proxy,'https':proxy},timeout=5)
        print(r.json(),'  - working',proxy)
    except :
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract,httpslist)
    