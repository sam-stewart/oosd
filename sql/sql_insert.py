from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_declarative import Base, Person, Student, Lecturer, Lecture, Course, StudentCourse

engine=create_engine('sqlite:///my_year.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
s = DBSession()

records=[
    Person(first_name='John', last_name='Smith'),
    Student(first_name='Samuel', last_name='Stewart', student_id=11005725),
    Student(first_name='Alex', last_name='McNeil', student_id=11003423),
    Student(first_name='Matt', last_name='Ankerson', student_id=11003454),
    Lecturer(first_name='Tom', last_name='Clark'),
    Lecturer(first_name='Patricia', last_name='Hayden'),
    Lecturer(first_name='Sam', last_name='Mann'),
    Lecturer(first_name='David', last_name='Rozado'),
    Course(id="in700002", title="Project 2", desc="Fun times", lecturer_id=3, semester=2),
    Course(id="in705001", title="Databases 3", desc="Machine learning", lecturer_id=4, semester=2),
    Course(id="in711001",title="Algorithms and Data Structures", desc="Cool things", lecturer_id=1, semester=2),
    Course(id="in700001", title="Project 1", desc="Sam Mann's holiday time", lecturer_id=3, semester=1),
    Course(id="in710001", title="OOSD", desc="Gang of four", lecturer_id=1, semester=1),
    Course(id="in719001", title="Systems Administration", desc="Puppet heaven", lecturer_id=1, semester=1),
    Course(id="in721000", title="Mobile Development", desc="Design and dev", lecturer_id=2, semester=1),
    Course(id="in712000", title="Web 3", desc="Frameworks and things", lecturer_id=4, semester = 1),
    Course(id="in715000", title="Networks 3", desc="PF, OpenBSD", lecturer_id=1, semester=2),
    Course(id="in715999", title="Virtualisation", desc="OpenStack", lecturer_id=1, semester=2),
    Lecture(course_id="in710001", class_room="D208", day="Wednesday", time="10:00"),
    Lecture(course_id="in710001", class_room="D208", day="Friday", time="8:00"),
    Lecture(course_id="in719001", class_room="D313", day="Tuesday", time="10:00"),
    Lecture(course_id="in719001", class_room="D313", day="Friday", time="10:00"),
    # Sam's courses: oosd, proj1, proj2, virt, sysadmin, mobile, ads
    StudentCourse(student_id=11005725, course_id="in700002"),
    StudentCourse(student_id=11005725, course_id="in715999"),
    StudentCourse(student_id=11005725, course_id="in711001"),
    StudentCourse(student_id=11005725, course_id="in700001"),
    StudentCourse(student_id=11005725, course_id="in710001"),
    StudentCourse(student_id=11005725, course_id="in719001"),
    StudentCourse(student_id=11005725, course_id="in721000"),
    # Alex's courses: oosd, proj1, proj2, web3, ads, db3, mobile
    StudentCourse(student_id=11003423, course_id="in710001"),
    StudentCourse(student_id=11003423, course_id="in700001"),
    StudentCourse(student_id=11003423, course_id="in700002"),
    StudentCourse(student_id=11003423, course_id="in712000"),
    StudentCourse(student_id=11003423, course_id="in711001"),
    StudentCourse(student_id=11003423, course_id="in705001"),
    StudentCourse(student_id=11003423, course_id="in721000"),
    # Matt's courses: Same as alex
    StudentCourse(student_id=11003454, course_id="in710001"),
    StudentCourse(student_id=11003454, course_id="in700001"),
    StudentCourse(student_id=11003454, course_id="in700002"),
    StudentCourse(student_id=11003454, course_id="in712000"),
    StudentCourse(student_id=11003454, course_id="in711001"),
    StudentCourse(student_id=11003454, course_id="in705001"),
    StudentCourse(student_id=11003454, course_id="in721000"),
]

s.add_all(records)
s.commit()
