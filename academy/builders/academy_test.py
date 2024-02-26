from sport_block import SportBlock
from study_block import StudyBlock
from student_hostel import StudentHostel
from academy import Academy
import datetime

# создаем экземпляры класса StudyBlock
additional_rooms_1 = ["administration office", "bookkeeping", "admission office", "canteen", "wc", "storage"]
study_block_1 = StudyBlock("main study building", "Kharkiv, Sumska, 40", 3000, 7, 1983, 200, 3500, additional_rooms_1)

additional_rooms_2 = ["library", "buffet", "wc", "storage"]
study_block_2 = StudyBlock("study building 2", "Kharkiv, Artema, 17", 2500, 5, 1996, 50, 654, additional_rooms_2)

additional_rooms_3 = ["concert room", "changing room", "buffet", "wc", "storage"]
study_block_3 = StudyBlock("study building 3", "Kharkiv, Chernyshevskogo, 1/2", 2000, 2, 2003, 10, 300, additional_rooms_3)


# создаем экземпляры класса SportBlock
pool_rooms = ["entrance hall", "wardrobe", "wc", "women changing room", "men changing room", "women shower room", "men shower room", "sauna", "massage room"]
pool_activities = ["swimming", "sauna visiting", "massage"]
pool = SportBlock("pool", "Kharkiv, Pushkinska, 5", 7000, 3, 1930, pool_rooms, pool_activities, 15000)

tennis_club_rooms = ["reception", "tennis courts space", "couch room", "buffet", "wc", "women changing room", "men changing room", "women shower room", "men shower room"]
tennis_club_activities = ["playing tennis", "buffet visiting", "tournament organisation"]
tennis_club = SportBlock("tennis club", "Kharkiv, Sumska, 211", 5200, 1, 2011, tennis_club_rooms, tennis_club_activities, 4500)

multifunctional_center_rooms = ["entrance hall", "table tennis room", "badminton room", "squash room", "gym"]
multifunctional_center_activities = ["playing table tennis", "playing badminton", "playing squash", "gym visiting"]
multifunctional_center = SportBlock("multifunctional sport center", "Kharkiv, Sumska, 248", 10000, 3, 1930, multifunctional_center_rooms, multifunctional_center_activities, 25000)


# создаем экземпляр класса StudentHostel
student_hostel_1 = StudentHostel("student hostel", "Kharkiv, Akademika Pavlova, 12", 4000, 9, 2000, 180, 520)


# создаем экземпляр класса Academy, передаем все уже созданные экземпляры
academy_1 = Academy("My Beautiful Academy", 2024, study_block_1, study_block_2, study_block_3, pool, tennis_club, multifunctional_center, student_hostel_1)

# теперь мы можем вывести общую информацию, включающую список всех зданий нашей академии
academy_1.show_general_info()

# можем добавить новые здания в нашу академию
student_hostel_2 = StudentHostel("student hostel 2", "Kharkiv, Akademika Pavlova, 13", 4000, 9, 2000, 180, 520)
academy_1.add_new_building(student_hostel_2)
print("We add one more building to our academy buildings list:")
academy_1.show_general_info()

# можно добавлять сразу несколько новых зданий
student_hostel_3 = StudentHostel("student hostel 3", "Kharkiv, Akademika Pavlova, 14", 4000, 9, 2000, 180, 520)
student_hostel_4 = StudentHostel("student hostel 4", "Kharkiv, Akademika Pavlova, 15", 4000, 9, 2000, 180, 520)
academy_1.add_new_building(student_hostel_3, student_hostel_4)
print("We add 2 more buildings to our academy buildings list:")
academy_1.show_general_info()

# можем удалить здание из списка
academy_1.delete_building(student_hostel_4)
print("We delete one building from our academy buildings list:")
academy_1.show_general_info()

# можем удалить сразу несколько зданий
academy_1.delete_building(student_hostel_3, student_hostel_2)
print("We delete 2 more buildings from our academy buildings list:")
academy_1.show_general_info()

# можем вывести расширенную информацию о всех зданиях
academy_1.show_buildings_info()
