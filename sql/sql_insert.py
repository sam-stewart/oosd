from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_declarative import Base, Person, Student, Lecturer, Lecture, Course, StudentCourse

engine=create_engine('sqlite:///my_year.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
s = DBSession()

records=[
    Student(first_name='Samuel', last_name='Stewart', student_id=11005725),
    Lecturer(first_name='Tom', last_name='Clark'),
    Lecturer(first_name='Patricia', last_name='Hayden'),
    Lecturer(first_name='Sam', last_name='Mann'),
    Lecturer(first_name='David', last_name='Rozado'),
    Course(id="in700002", title="Project 2", desc="Fun times", lecturer_id=3),
    Course(id="in705001", title="Databases 3", desc="Machine learning", lecturer_id=4),
    Course(id="in711001",title="Algorithms and Data Structures", desc="Cool things", lecturer_id=1),
    Course(id="in700001", title="Project 1", desc="Sam Mann's holiday time", lecturer_id=3),
    Course(id="in710001", title="OOSD", desc="Gang of four", lecturer_id=1),
    Course(id="in719001", title="Systems Administration", desc="Puppet heaven", lecturer_id=1),
    Course(id="in721000", title="Mobile Development", desc="Design and dev", lecturer_id=2),
    Lecture(lecturer_id=1, class_room="D208", day="Wednesday", time="10:00"),
    Lecture(lecturer_id=1, class_room="D208", day="Friday", time="8:00"),
    StudentCourse(student_id=11005725, course_id="in700002"),
    StudentCourse(student_id=11005725, course_id="in705001"),
    StudentCourse(student_id=11005725, course_id="in711001"),
    StudentCourse(student_id=11005725, course_id="in700001"),
    StudentCourse(student_id=11005725, course_id="in710001"),
    StudentCourse(student_id=11005725, course_id="in719001"),
    StudentCourse(student_id=11005725, course_id="in721000"),
]

for r in records:
    s.add(r)
s.commit()
