import json
import bs4
import requests

department_course_catalogs = {}

all_departments_catalogs = "https://catalog.tamu.edu/undergraduate/course-descriptions/"
all_department_links = bs4.BeautifulSoup(requests.get(all_departments_catalogs).text, 'html.parser').find(id='atozindex').find_all('li')
for department_link in all_department_links:
    department_course_catalogs[department_link.get_text()] = "https://catalog.tamu.edu" + department_link.find('a')['href']

with open('department_course_catalogs.json', 'w') as file:
    file.write(json.dumps(department_course_catalogs))