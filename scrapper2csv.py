import requests
from bs4 import BeautifulSoup
import re
from csv import writer

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page_request = requests.get("https://mumbrella.com.au/industry/branding-and-design-agencies", headers = headers )
page_content = BeautifulSoup(page_request.content,'html.parser')

directories = page_content.select('.directory-listing')


with open('entities.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    row_headers = ['Name','Email','Phone','Address']
    csv_writer.writerow(row_headers)

    for directory in directories:
        dir_address = directory.select('a')[0].get('href').strip()
        dir_request = requests.get(dir_address,headers = headers)
        dir_content = BeautifulSoup(dir_request.content,'html.parser')
        dir_name = dir_content.find('h1').get_text()

        dir_text = dir_content.get_text()
        email_span = re.search("Email:.*", dir_text)
        phone_span = re.search("Phone:.*", dir_text)
        address_span = re.search("Address", dir_text)
        end_span = re.search("Listing last updated", dir_text)
        
        dir_email = '' if email_span is None else re.sub("Email:","",dir_text[email_span.start():email_span.end()]).strip()
        dir_phone = '' if phone_span is None else re.sub("Phone:","", dir_text[phone_span.start():phone_span.end()]).strip()
        dir_address = '' if address_span is None else dir_text[address_span.end():end_span.start()].strip()
            
        csv_writer.writerow([dir_name,dir_email,dir_phone,dir_address])
 
