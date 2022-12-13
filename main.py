from abc import ABC, abstractmethod


class Teacher:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if not isinstance(n, str):
            raise TypeError
        self.__name = n

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, n):
        if not isinstance(n, str):
            raise TypeError
        self.__surname = n

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class Course(ABC):
    @abstractmethod
    def new_course(self, *args):
        pass


class LocalCourse(Course):
    def __init__(self, name, address, *args):
        self.name = name
        self.address = address
        self.theme = list()
        for x in args:
            if not isinstance(x, str):
                raise TypeError
        for x in args:
            self.theme.append(x)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if not isinstance(n, str):
            raise TypeError
        self.__name = n

    @property
    def address(self, a):
        return self.__address

    @address.setter
    def address(self, a):
        if not isinstance(a, str):
            raise TypeError

    def new_course(self, *args):
        for x in args:
            if not isinstance(x, str):
                raise TypeError
            self.theme.append(x)

    def __str__(self):
        k = ''
        for x in self.theme:
            k += f'"{x}" '
        return f'Name: {self.name}\nThemes: {k}.'


class OffsiteCourse(Course):
    def __init__(self, name, address, *args):
        self.name = name
        self.address = address
        self.theme = list()
        for x in args:
            if not isinstance(x, str):
                raise TypeError
        for x in args:
            self.theme.append(x)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if not isinstance(n, str):
            raise TypeError
        self.__name = n

    @property
    def address(self, a):
        return self.__address

    @address.setter
    def address(self, a):
        if not isinstance(a, str):
            raise TypeError

    def new_course(self, *args):
        for x in args:
            if not isinstance(x, str):
                raise TypeError
            self.theme.append(x)

    def __str__(self):
        k = ''
        for x in self.theme:
            k += f'"{x}" '
        return f'Name: {self.name}\nThemes: {k}.'


class CourseFactory:
    def __init__(self, teacher, *args):
        self.teacher = teacher
        self.course = list()
        for x in args:
            if not isinstance(x, LocalCourse) and not isinstance(x, OffsiteCourse):
                raise TypeError
        for x in args:
            self.course.append(x)

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, t):
        if not isinstance(t, Teacher):
            raise TypeError
        self.__teacher = t

    def course_add(self, t):
        for x in t:
            if not isinstance(x, LocalCourse or OffsiteCourse):
                raise TypeError
        for x in t:
            self.course.append(x)

    def __str__(self):
        k = ''
        for x in self.course:
            k += f'{x}\n'
        return f'{self.teacher}\n{k}'


academy_address = 'Privit-drive'
course1 = LocalCourse('Python', academy_address, 'lab1', 'Basic', 'Classes')
course1.new_course('Libraries', 'Functions')
course12 = OffsiteCourse('C++', 'Hogwarts', 'Basic', 'Classes')
teacher1 = Teacher('Hezer', 'Linda')
course2 = CourseFactory(teacher1, course1, course12)
print(course2)
