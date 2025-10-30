import json
import requests
import bs4
import re

department_course_catalogs = {}

with open('department_course_catalogs.json', 'r') as file:
    department_course_catalogs = json.loads(file.read())


courses = {}
for department_link in department_course_catalogs.values():
    course_blocks = bs4.BeautifulSoup(requests.get(department_link).text, 'html.parser').find_all('div', {'class': 'courseblock'})
    for course in course_blocks:
        try:
            course_block_title = course.find('h2', {'class': 'courseblocktitle'}).get_text()
            course_id, course_title = re.search('([A-Z]{4} [0-9]{3,4}) (.*)', course_block_title).groups()
            course_id = course_id.replace(' ', ' ')
            course_description = course.find('p', {'class': 'courseblockdesc'}).text

            courses[course_id] = {'title': course_title,
                                  'description': course_description}
        except Exception as e:
            print(course)
            print(e)


with open('courses.json', 'w') as file:
    file.write(json.dumps(courses))