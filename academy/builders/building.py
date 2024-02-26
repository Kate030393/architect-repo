import datetime


class Building:

    def __init__(self, block_type, address, built_up_area, levels, foundation_year):
        self.__block_type = block_type
        self.__address = address
        self.__built_up_area = built_up_area
        self.__levels = levels
        self.__foundation_year = foundation_year

    @property
    def block_type(self):
        return self.__block_type

    @block_type.setter
    def block_type(self, user_block_type):
        if user_block_type != "":
            self.__block_type = user_block_type

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, user_address):
        if user_address != "":
            self.__address = user_address

    @property
    def built_up_area(self):
        return self.__built_up_area

    @built_up_area.setter
    def built_up_area(self, user_area):
        if isinstance(user_area, (int, float)):
            self.__built_up_area = user_area

    @property
    def levels(self):
        return self.__levels

    @levels.setter
    def levels(self, user_levels):
        if isinstance(user_levels, int) and 0 <= user_levels <= 30:
            self.__levels = user_levels

    @property
    def foundation_year(self):
        return self.__foundation_year

    @foundation_year.setter
    def foundation_year(self, user_foundation_year):
        today = datetime.date.today()
        year = today.year
        if 1700 <= user_foundation_year <= year:
            self.__foundation_year = user_foundation_year

    def show_info(self):
        building_name = self.block_type
        print(f"{building_name.upper()}")
        print(f"    Address: {self.__address}")
        print(f"    Built_up_area: {self.__built_up_area}")
        print(f"    Number of levels: {self.__levels}")
        print(f"    Year of foundation: {self.__foundation_year}")
