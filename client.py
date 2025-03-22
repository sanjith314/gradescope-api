from gradescopeapi.classes.connection import GSConnection

# create connection and login
connection = GSConnection()
connection.login("", "")

"""
Fetching all courses for user
"""
courses = connection.account.get_courses()
for course in courses["instructor"]:
    print(course)
for course in courses["student"]:
    print(course)

"""
Getting roster for a course
"""
course_id = 971386
# members = connection.account.get_course_users(course_id)
# for member in members:
#     print(member)

"""
Getting all assignments for course
"""
# assignments = connection.account.get_assignments(course_id)
# for assignment in assignments:
#     print(assignment)

submissions = connection.account.get_assignment_submissions(971386, 5723638)
for submission in submissions:
    print(submission)

    