import json
import requests
import bs4
import re
import os

department_course_catalogs = {}

with open('department_course_catalogs.json', 'r') as file:
    department_course_catalogs = json.loads(file.read())

count = 0

courses = {}
for department_link in department_course_catalogs.values():
    course_blocks = bs4.BeautifulSoup(requests.get(department_link).text, 'html.parser').find_all('div', {'class': 'courseblock'})
    for course in course_blocks:
        course_block_title = course.find('h2', {'class': 'courseblocktitle'}).get_text()
        course_id, course_title = re.search('([A-Z]{4} [0-9]{3,4}) (.*)', course_block_title).groups()
        course_id = course_id.replace(' ', ' ')
        course_description = course.find('p', {'class': 'courseblockdesc'}).text


        subj_code, course_num = course_id.split(" ")

        requirements = None

        try:
            requirements = requests.post("https://howdy.tamu.edu/main/api/degree/get-updated-course-prerequisites",
                                         headers={
                                             "Cookie": os.getenv('HOWDY_COOKIE')
                                         },
                                         json={
                                             "p_term_in": "202611",
                                             "p_subj_code_in": subj_code,
                                             "p_crse_numb_in": course_num
                                         }).json()["rows"][0]['RESULT']
        except Exception as e:
            print(e)

        print(course_id, requirements)

        courses[course_id] = {'title': course_title,
                              'description': course_description,
                              'requirements': requirements}


print(courses)

with open('courses.json', 'w') as file:
    file.write(json.dumps(courses, indent=4))