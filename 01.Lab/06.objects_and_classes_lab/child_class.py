from parent_class import BaseClass


class ChildClass(BaseClass):
    def __init__(self, name, age):
        BaseClass.__init__(self, name)
        self.age = age

    def get_age(self):
        return self.age