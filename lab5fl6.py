class RaceHorse:
    """horse characteristics"""

    def __init__(self, speed, age, name):
        self.speed = speed
        self.age = age
        self.name = name
        self.place_in_race = None

    def __repr__(self):
        return f"Racehorse({self.speed}, {self.age}, {self.name}, {self.place_in_race})"


class Race:

    def __init__(self):
        self.participants = []

    def new_participant(self, horse):
        """adding new horse - participant"""
        if 3 <= horse.age <= 7:
            self.participants.append(horse)

    def del_participant(self, horse):
        """deleting horse from participant list"""
        self.participants.remove(horse)

    def select_winner(self):
        """selecting winner-horse from participant"""
        avg_age = sum(horse.age for horse in self.participants) / len(self.participants)
        winner = sorted(self.participants, key=lambda horse: horse.speed + abs(horse.age - avg_age), reverse=True)[0]
        winner.place_in_race = 1
        return winner

    def sort_speed(self):
        """sorting participants-horse by speed"""
        self.participants.sort(key=lambda horse: horse.speed, reverse=True)

    def set_place(self):
        """setting 1 to 3 places for participant horses"""
        for i, horse in enumerate(self.participants[:3]):
            horse.place_in_race = i + 1
