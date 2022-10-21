from re import M
from numpy import number
import requests
from bs4 import BeautifulSoup
import os.path
from urllib.parse import unquote

# Create top_items as empty list
all_links = []

to_save_all_links = []

mirrior_links = []

to_save_mirrior_links = []

driect_mirror_links = []

to_save_driect_mirror_links = []

local = []

to_save_local = []

download_links = []

specified_lines = []
  

# lines to print
for i in range(1, 100, 3):
    specified_lines.append(i)

animi_url = input("Enter the url: ")

dir_create = input("Enter the directory name: ")

os.mkdir(dir_create)

page = requests.get(animi_url)
soup = BeautifulSoup(page.content, 'html.parser')



links = soup.select('a', href = True ,attrs={'target':'_blank'})

f = open("url.txt", "w")
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''
    all_links.append(href)
    
    
for all_link in all_links:
    page = requests.get(all_link)
    soup = BeautifulSoup(page.content, 'html.parser')

    mirror = soup.findAll( 'a' , attrs={'class':'btn btn-outline-success'}) #soup.select('a', attrs={'data-mdb-ripple-color':'dark'}, href = True)
    for ahref in mirror:
        text = ahref.text
        text = text.strip() if text is not None else ''

        href = ahref.get('href')
        href = href.strip() if href is not None else ''
        # all_links.append(href)
        mirrior_links.append('https://anidrive.in' + href)

for direct in mirrior_links:
    page = requests.get(direct)
    soup = BeautifulSoup(page.content, 'html.parser')

    mirror = soup.findAll( 'a' , attrs={'class':'btn btn-success'}) #soup.select('a', attrs={'data-mdb-ripple-color':'dark'}, href = True)
    for ahref in mirror:
        text = ahref.text
        text = text.strip() if text is not None else ''

        href = ahref.get('href')
        href = href.strip() if href is not None else ''
        local.append(href)
for pos, l_num in enumerate(local):
# check if the line number is specified in the lines to read array
    if pos in specified_lines:
    # print the required line number
        driect_mirror_links.append(l_num)        

for download in driect_mirror_links:

    page = requests.get(download)
    soup = BeautifulSoup(page.content, 'html.parser')

    mirror = soup.findAll( 'a' , attrs={'class':'btn btn-success'}) #soup.select('a', attrs={'data-mdb-ripple-color':'dark'}, href = True)
    
    for ahref in mirror:
        text = ahref.text
        text = text.strip() if text is not None else ''

        href = ahref.get('onclick').split("'")[1]
        href = href.strip() if href is not None else ''
        download_links.append(href)
        f.write(href)
        f.write("\n")        
        print(href)


for link in download_links:
    link = link.strip()
    url_encode = link.rsplit('/', 1)[-1]
    name = unquote(url_encode)
    filename = os.path.join('E:\\New folder\\', dir_create , name)

    if not os.path.isfile(filename):
        print('Downloading: ' + filename)
        try:
            URL = link
            response = requests.get(URL)
            open(filename, "wb").write(response.content)
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing.')