from lab5.lab5 import RaceHorse, Race

horse1 = RaceHorse(10, 7, "horse 1")
horse2 = RaceHorse(12, 5, "horse 2")
horse3 = RaceHorse(16, 3, "horse 3")
horse4 = RaceHorse(9, 7, "horse 4")

if __name__ == '__main__':

    race = Race()
    race.new_participant(horse1)
    race.new_participant(horse2)
    race.new_participant(horse3)
    race.new_participant(horse4)

    print(race.select_winner())

    race.sort_speed()
    print(race.participants)

    race.set_place()
    print(race.participants)

    race.del_participant(horse4)
    print(race.participants)
