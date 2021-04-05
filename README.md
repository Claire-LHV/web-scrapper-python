# Web-Scrapper
An example of web scrapper for contact information of listed entities.
## Requirements
* **Python version 3 and higher**
* Libraries in used: [**BeautifulSoup**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [**requests**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [**re**](https://docs.python.org/3/library/re.html), and [**csv**](https://docs.python.org/3/library/csv.html).
## Output
The output will be a csv file with records of name of entities, their email address if found, their phone number if found, and there address if found. An empty string is used when any of them is not found.
## How it works
It opens and loops through every listing. Their contact information is then extracted and recorded in a csv file named *entities.csv*.



