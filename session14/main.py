import requests
from bs4 import BeautifulSoup
from csv_manager import write_data
from services import normalize_time, normalize_price


course_title = [] 
course_teacher = [] 
course_time = []
course_price = []

for i in range(1, 3):
    url = f'https://toplearn.com/courses?pageId={i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for h2_tag in soup.find_all('h2'):
        a_tag = h2_tag.find('a')
        course_title.append(a_tag.text)

        
    for top_div in soup.find_all('div', class_="top"):
        link_tag = top_div.find('a')
        course_teacher.append(link_tag['title'])


    for span_time in soup.find_all('span', class_="time"):
        course_time.append(normalize_time(span_time.text))

 
    for span_price in soup.find_all('span', class_="price"):
        i_tag = span_price.find('i')
        pr = i_tag.text
        course_price.append(0 if pr == ' رایگانـ ' else normalize_price(pr))


write_data(
    course_title, 
    course_teacher, 
    course_price, 
    course_time
)
    
