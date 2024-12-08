import pytest
from pytest_mastering.source.school import TooManyStudents, Classroom, Teacher, Student


@pytest.fixture
def hogwarts_classroom():
    """Fixture for setting up a default Hogwarts classroom."""
    teacher = Teacher("Professor McGonagall")
    students = [Student(f"Student {i}") for i in range(3)]  # Initial 3 students
    course_title = "Transfiguration"
    return Classroom(teacher=teacher, students=students, course_title=course_title)


@pytest.fixture
def harry_potter_students():
    """Fixture for Harry Potter students."""
    return [Student(name) for name in ["Harry", "Hermione", "Ron", "Neville", "Luna"]]


def test_add_student(hogwarts_classroom, harry_potter_students):
    """Test adding students to the classroom."""
    classroom = hogwarts_classroom
    for student in harry_potter_students:
        classroom.add_student(student)
    assert len(classroom.students) == 8  # 3 initial + 5 added


def test_add_too_many_students(hogwarts_classroom):
    """Test that TooManyStudents is raised if more than 10 students are added."""
    classroom = hogwarts_classroom
    with pytest.raises(TooManyStudents):
        for i in range(8):  # Adding 8 students exceeds the limit of 10
            classroom.add_student(Student(f"Extra Student {i}"))


def test_remove_student(hogwarts_classroom):
    """Test removing a student from the classroom."""
    classroom = hogwarts_classroom
    classroom.add_student(Student("Harry"))
    assert any(student.name == "Harry" for student in classroom.students)
    classroom.remove_students("Harry")
    assert all(student.name != "Harry" for student in classroom.students)


def test_change_teacher(hogwarts_classroom):
    """Test changing the teacher of the classroom."""
    classroom = hogwarts_classroom
    new_teacher = Teacher("Professor Snape")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == "Professor Snape"


@pytest.mark.parametrize(
    "teacher_name,student_names,course_title,expected",
    [
        (
            "Professor Sprout",
            ["Ernie", "Hannah", "Susan"],
            "Herbology",
            ("Professor Sprout", 3, "Herbology"),
        ),
        (
            "Professor Snape",
            ["Draco", "Pansy"],
            "Potions",
            ("Professor Snape", 2, "Potions"),
        ),
    ],
)
def test_classroom_initialization(teacher_name, student_names, course_title, expected):
    """Test the initialization of the Classroom class."""
    teacher = Teacher(teacher_name)
    students = [Student(name) for name in student_names]
    classroom = Classroom(teacher, students, course_title)
    assert classroom.teacher.name == expected[0]
    assert len(classroom.students) == expected[1]
    assert classroom.course_title == expected[2]
