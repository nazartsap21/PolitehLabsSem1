"""importing RaceHorse and Race modules"""
from lab5fl6 import RaceHorse, Race
import pytest


@pytest.fixture(name="race_fixture")
def test_race():
    """making test_race to use it in our test-functions"""
    race = Race()
    horse1 = RaceHorse(10, 7, "horse 1")
    horse2 = RaceHorse(12, 5, "horse 2")
    horse3 = RaceHorse(16, 3, "horse 3")
    horse4 = RaceHorse(9, 7, "horse 4")
    race.new_participant(horse1)
    race.new_participant(horse2)
    race.new_participant(horse3)
    race.new_participant(horse4)
    yield race


def test_new_participant():
    """testing adding new horse - participant"""
    race = Race()
    horse1 = RaceHorse(10, 7, "horse 1")
    race.new_participant(horse1)
    assert horse1 in race.participants


def test_del_participant():
    """testing deleting horse from participant list"""
    race = Race()
    horse1 = RaceHorse(10, 7, "horse 1")
    race.new_participant(horse1)
    race.del_participant(horse1)
    assert horse1 not in race.participants


def test_select_winner(race_fixture):
    """testing selecting winner-horse from participant"""
    winner = race_fixture.select_winner()
    assert winner.place_in_race == 1


def test_sort_speed(race_fixture):
    """testing sorting participants-horse by speed"""
    race_fixture.sort_speed()
    speeds = [horse.speed for horse in race_fixture.participants]
    assert speeds == sorted(speeds, reverse=True)


def test_set_place(race_fixture):
    """testing setting 1 to 3 places for participant horses"""
    race_fixture.set_place()
    places = [horse.place_in_race for horse in race_fixture.participants[:3]]
    assert places == [1, 2, 3]


if __name__ == "__main__":
    pytest.main()
