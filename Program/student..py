# Student class, OOP part
class Student:
    def __init__(self, student_id, name, class_name="Default", chinese=0, english=0, math=0):
        self.__student_id = student_id
        self.__name = name
        self.__class_name = class_name
        self.__chinese = chinese
        self.__english = english
        self.__math = math

    # Getter methods
    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_class_name(self):
        return self.__class_name

    def get_chinese(self):
        return self.__chinese

    def get_english(self):
        return self.__english

    def get_math(self):
        return self.__math

    def get_total(self):
        return self.__chinese + self.__english + self.__math

    # Setter methods, check score range
    def set_name(self, name):
        self.__name = name
        return True

    def set_class_name(self, class_name):
        self.__class_name = class_name
        return True

    def set_chinese(self, score):
        if score < 0 or score > 100:
            return False
        self.__chinese = score
        return True

    def set_english(self, score):
        if score < 0 or score > 100:
            return False
        self.__english = score
        return True

    def set_math(self, score):
        if score < 0 or score > 100:
            return False
        self.__math = score
        return True