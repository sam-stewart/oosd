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

for p, st in s.query(Person, Student):
    print p.first_name, p.last_name, st.student_id

print "##### PAPERS + LECTURER #####"

for c, l, p in s.query(Course, Lecturer, Person).\
        filter(Course.lecturer_id == Lecturer.id).all():
    print c.title, c.desc, p.first_name, p.last_name

# Get OOSD paper, print some stuff, print students.
print "#### OOSD, STUDENTS #####"

q = s.query(Course).filter(Course.id == "in710001").one()
print q.title, q.desc
for r in q.students:
    print r.first_name, r.last_name

# Joins to assoc, joins to student, filters by semester and student_id.
print "##### STUDENT SCHEDULE #####"

q = s.query(Course).join(StudentCourse).\
        join(Student).\
        filter(Student.student_id == 11005725).\
        filter(Course.semester == 1).\
        all()

for c in q:
    print c.title
    for l in c.lectures:
        print l.day + " " + l.time + " " + l.class_room
