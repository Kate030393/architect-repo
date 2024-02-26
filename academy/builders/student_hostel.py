from building import Building
class StudentHostel(Building):
    student_hostel_instances_count = 0
    student_hostel_instances = []
    def __init__(self, block_type, address, built_up_area, levels, foundation_year, rooms_quantity, places_quantity):
        super().__init__(block_type, address, built_up_area, levels, foundation_year)
        self.__rooms_quantity = rooms_quantity
        self.__places_quantity = places_quantity
        StudentHostel.student_hostel_instances_count = StudentHostel.student_hostel_instances_count + 1
        self.__class__.student_hostel_instances.append(self.block_type)

    @property
    def rooms_quantity(self):
        return self.__rooms_quantity

    @rooms_quantity.setter
    def rooms_specification(self, user_rooms_quantity):
        self.__rooms_quantity = user_rooms_quantity

    @property
    def places_quantity(self):
        return self.__places_quantity

    @places_quantity.setter
    def places_quantity(self, user_places_quantity):
        self.__places_quantity = user_places_quantity

    def show_info(self):
        building_name = self.block_type
        print(f"{building_name.upper()}")
        print(f"    Address: {self.address}")
        print(f"    Built up area: {self.built_up_area}")
        print(f"    Number of levels: {self.levels}")
        print(f"    Year of foundation: {self.foundation_year}")
        print(f"    Rooms quantity: {self.rooms_quantity}")
        print(f"    Building capacity: {self.places_quantity} places\n")
