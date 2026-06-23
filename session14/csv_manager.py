import csv

def write_data(
        course_title, 
        course_teacher, 
        course_price, 
        course_time
    ):
    with open('courses.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'teacher', 'price', 'time'])
        
        for index, item in enumerate(course_title):
            writer.writerow([
                course_title[index],
                course_teacher[index],
                course_price[index],
                course_time[index]
            ])