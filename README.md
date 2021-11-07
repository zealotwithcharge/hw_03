# hw_03

ebay-dl.py scrapes ebay pages when given a search term and provides a list of the items on the page.\
Each entry in the list contains the name, price, status, shipping price, whether they provide free returns, and the number of units sold of the item.\
After scraping, the program creates a json file "SEARCH_TERM.json" that contains this list.\
\
\
The command should look as such:
```
  ebay-dl.py [-h] [--page1 PAGE1] [--page2 PAGE2] [--csv] search_term
```
Page1 is the starting page and page2 is the ending page.\
Page1 is set to 1 at default and page2 is set to 5 at default.\
csv lets you choose whether you want to save the data as a .csv file or a .json file.\
simply having the csv argument will set it so that the data is saved as a .csv file.\
\
The three .json files in this repository were generated with the following commands:
```
  ebay-dl.py game
  ebay-dl.py paper
  ebay-dl.py "stuffed animal"
```
On my local computer the exact commands is as follows:
```
  python.exe ebay-dl.py game
  python.exe ebay-dl.py paper
  python.exe ebay-dl.py "stuffed animal"
```
The three .csv files in this repository were generated with the following commands:
```
  ebay-dl.py game --csv
  ebay-dl.py paper --csv
  ebay-dl.py "stuffed animal" --csv
```
On my local computer the exact commands is as follows:
```
  python.exe ebay-dl.py game --csv
  python.exe ebay-dl.py paper --csv
  python.exe ebay-dl.py "stuffed animal" --csv
```


https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03
