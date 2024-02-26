from building import Building
class StudyBlock(Building):
    study_block_instances_count = 0
    def __init__(self, block_type, address, built_up_area, levels, foundation_year, auditorium_quantity, students_quantity, additional_rooms):
        super().__init__(block_type, address, built_up_area, levels, foundation_year)
        self.__auditorium_quantity = auditorium_quantity
        self.__students_quantity = students_quantity
        self.__additional_rooms = additional_rooms
        StudyBlock.study_block_instances_count = StudyBlock.study_block_instances_count + 1

    @property
    def auditorium_quantity(self):
        return self.__auditorium_quantity

    @auditorium_quantity.setter
    def auditorium_quantity(self, user_auditorium_quantity):
        self.__auditorium_quantity = user_auditorium_quantity

    @property
    def students_quantity(self):
        return self.__students_quantity

    @students_quantity.setter
    def students_quantity(self, user_students_quantity):
        self.__students_quantity = user_students_quantity

    @property
    def additional_rooms(self):
        return self.__additional_rooms

    @additional_rooms.setter
    def additional_rooms(self, user_additional_rooms):
        self.__additional_rooms = user_additional_rooms

    def show_info(self):
        building_name = self.block_type
        print(f"{building_name.upper()}")
        print(f"    Address: {self.address}")
        print(f"    Built up area: {self.built_up_area}")
        print(f"    Number of levels: {self.levels}")
        print(f"    Year of foundation: {self.foundation_year}")
        print(f"    Auditoriums quantity: {self.auditorium_quantity}")
        print(f"    Building capacity: {self.students_quantity} students")
        print(f"    Specification of additional rooms: {', '.join(self.additional_rooms)}\n")
