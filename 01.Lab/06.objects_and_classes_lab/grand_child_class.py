from child_class import ChildClass


class GrandChildClass(ChildClass):
    def __init__(self, name, age, address):
        ChildClass.__init__(self, name, age)
        self.address = address

    def get_address(self):
        return self.address


obj = GrandChildClass("Boyan", 38, "Sofia")
print(obj.get_name(), obj.get_age(), obj.get_address())
