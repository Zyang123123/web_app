from app import process_query


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == "Dinosaurs ruled the Earth \
200 million years ago"


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_player_name():
    assert process_query("What is your name?") == "VW50"


def test_plus():
    assert process_query("What is 50 plus 25?") == "75"


def test_mul():
    assert process_query("What is 50 multiplied by 2?") == "100"
