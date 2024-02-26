from typing import List


class Academy:
    __all_instances_list = []
    __academy_block_types = []


    def __init__(self, name, foundation_date, *args):
        self.__name = name
        self.__foundation_date = foundation_date
        self.args = args
        # self.set_academy_block_types(args)
        # for obj in args:
        #     self.__academy_block_types.append(obj.block_type)
        self.__all_instances_list.extend(args)


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, user_name):
        self.__name = user_name

    @property
    def foundation_date(self):
        return self.__foundation_date

    @foundation_date.setter
    def foundation_date(self, user_foundation_date):
        self.__foundation_date = user_foundation_date

    def show_general_info(self):
        print(f"{self.__name.upper()}")
        print(f"Our academy was found at {self.__foundation_date}")
        all_block_types = []
        for obj in self.__all_instances_list:
            all_block_types.append(obj.block_type)
        print(f"Buildings of our academy: {', '.join(all_block_types)}\n")

    def add_new_building(self, *user_new_building):
        self.__all_instances_list.extend(user_new_building)

    def delete_building(self, *removed_building):
        for removed_obj in removed_building:
            for el in self.__all_instances_list:
                if el == removed_obj:
                    self.__all_instances_list.remove(el)

    def show_buildings_info(self):
        for obj in self.__all_instances_list:
            obj.show_info()







    # @property
    # def academy_block_types(self):
    #     return print(f"Buildings of our academy: {', '.join(self.__academy_block_types)}")

    # def set_academy_block_types(self, args):
    #     if type(args) == tuple:
    #         for obj in args:
    #             self.__academy_block_types.append(obj.block_type)
    #     else:
    #         self.__academy_block_types.append(args.block_type)

    # @academy_block_types.setter
    # def academy_block_types(self, *args):
    #     for obj in args:
    #         self.__academy_block_types.append(obj.block_type)





