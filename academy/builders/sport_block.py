from building import Building


class SportBlock(Building):
    sport_block_instances_count = 0
    def __init__(self, block_type, address, built_up_area, levels, foundation_year, rooms_specification, activities, useable_area):
        super().__init__(block_type, address, built_up_area, levels, foundation_year)
        self.__rooms_specification = rooms_specification
        self.__activities = activities
        self.__useable_area = useable_area
        SportBlock.sport_block_instances_count = SportBlock.sport_block_instances_count + 1


    @property
    def rooms_specification(self):
        return self.__rooms_specification

    @rooms_specification.setter
    def rooms_specification(self, user_rooms_specification):
        self.__rooms_specification = user_rooms_specification

    @property
    def activities(self):
        return self.__activities

    @activities.setter
    def activities(self, user_activities):
        self.__activities = user_activities

    @property
    def useable_area(self):
        return self.__useable_area

    @useable_area.setter
    def useable_area(self, user_useable_area):
        self.__useable_area = user_useable_area

    def show_info(self):
        building_name = self.block_type
        print(f"{building_name.upper()}")
        print(f"    Address: {self.address}")
        print(f"    Built up area: {self.built_up_area}")
        print(f"    Effective  area: {self.useable_area}")
        print(f"    Number of levels: {self.levels}")
        print(f"    Year of foundation: {self.foundation_year}")
        print(f"    Sport buildings quantity: {self.sport_block_instances_count}")
        print(f"    Possible activities: {', '.join(self.activities)}")
        print(f"    Specification of rooms: {', '.join(self.rooms_specification)}\n")
