from sql_declarative import Person, Base, Student, Lecturer, Lecture, Course, StudentCourse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my_year.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
s = DBSession()

# Print all student
print "###### STUDENTS ######"
q = s.query(Person).join(Student).all()
for r in q:
    print r.first_name + " " + r.last_name

# Print all papers
print "###### PAPERS ######"
q = s.query(Course).all()
for r in q:
    print r.title, r.desc

# Get OOSD paper, print some stuff, print students.
print "#### OOSD, STUDENTS #####"
q = s.query(Course).filter(Course.id == "in710001").one()
print q.title, q.desc
for r in q.students:
    print r.first_name + " " + r.last_name

# Select a student (me) print schedule for semester
print "##### STUDENT SCHEDULE #####"
q = s.query(Student).filter(Student.student_id == 11005725).one()
courses = q.courses
for r in courses:
    print r.title
    for i in r.lectures:
        print i.day + " " + i.time

