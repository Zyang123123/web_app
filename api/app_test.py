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


def test_minus():
    assert process_query("What is 50 minus 25?") == "25"


def test_mul():
    assert process_query("What is 50 multiplied by 2?") == "100"


def test_prime():
    s1 = "Which of the following numbers are primes: 5, 55, 32, 41, 35?"
    assert process_query(s1) == "5, 41"


def test_s_c():
    s = "Which of the following numbers is both a square and a cube: " + \
        "1, 64, 729, 555, 1156, 4928, 4096?"
    assert process_query(s) == "1, 64, 729, 4096"
