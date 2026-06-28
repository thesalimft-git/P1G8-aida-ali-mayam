import requests
from bs4 import BeautifulSoup

course_title = [] 
course_teacher = [] 

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
        print(span_time.text)




    print(course_title)
    print(course_teacher)



