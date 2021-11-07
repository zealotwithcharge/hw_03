import argparse
import requests
import bs4
from os.path import exists
import json
import copy
import csv

parser = argparse.ArgumentParser(description='Ebay scrapper')
parser.add_argument('search_term',help='the search term')
parser.add_argument('--page1',default = 1, help='starting page')
parser.add_argument('--page2',default = 5, help='ending page')
parser.add_argument('--csv',action='store_true',help='Whether or not to create in csv format')
args = parser.parse_args()

base = {'name':'','price':0,'status':'','shipping':0,'free_returns':False,'items_sold':0}
all_items=[]


for i in range(int(args.page1)-1,int(args.page2)):
    print(i)
    
    if not exists(args.search_term+f'_{i}.html'):
        r = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw='+args.search_term+f'&_pgn={i}')
        text = r.text
        with open(args.search_term+f'_{i}.html', 'w', encoding='utf-8') as f:
            f.write(text)
    
    with open(args.search_term+f'_{i}.html',encoding='utf-8') as file:

        noStarchSoup = bs4.BeautifulSoup(file.read(), 'html.parser')
        items = noStarchSoup.select('li[class*= "s-item s-item__pl-on-bottom"]')
        
        print(len(items))
        for i,item in enumerate(items):
            name = item.select('h3[class*= "s-item__title"]')
            
            if len(name)!=0 and not name[0].getText()=='':
                #name
                base['name']= name[0].getText()
                #price
                price = item.select('span[class = "s-item__price"]')[0].getText()
                price = ''.join(filter(str.isdigit,price))
                if price != '':
                    base['price'] = int(price)
                else:
                    base['price'] = 0
                #status
                status = item.select('span[class = "SECONDARY_INFO"]')
                if len(status)!=0:
                    base['status'] = status[0].getText()
                #shipping
                shipping = item.select('span[class = "s-item__shipping s-item__logisticsCost"]')

                if len(shipping)!=0:
                    shipping = shipping[0].getText()
                    if shipping != 'Free shipping':
                        shipping = ''.join(filter(str.isdigit,shipping))
                        
                        base['shipping'] = int(shipping)
                    else:
                        base['shipping'] = 0 
                else:
                    base['shipping'] = 0
                #returns
                free_returns = item.select('span[class ="s-item__free-returns s-item__freeReturnsNoFee"]')
                if len(free_returns)!=0:
                    base['free_returns']= free_returns[0].getText() == 'Free returns'
                #items sold
                items_sold = item.select('span[class = "s-item__hotness s-item__itemHotness"]')
                if len(items_sold)!=0:
                    items_sold = str(items_sold[0])
                    items_sold = ''.join(filter(str.isdigit, items_sold))
                    if items_sold != '':
                        base['items_sold'] = int(items_sold)
                    else:
                        base['items_sold'] = None
                else:
                    base['items_sold'] = None
                base1= copy.deepcopy(base)
                all_items.append(base1)
        
if not args.csv:
    with open(args.search_term.upper()+'.json','w',encoding='utf-8') as f:
        json.dump(all_items,f)
else:
    # csv header
    fieldnames = ['name','price','status','shipping','free_returns','items_sold' ]

    with open(args.search_term.upper()+'.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_items)
