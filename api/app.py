from flask import Flask, render_template, request
import re
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


@app.route("/form")
def hello_githubname():
    return render_template("githubname.html")


@app.route("/form/submit", methods=["POST"])
def formsubmit():
    input_name = request.form.get("name")
    return render_template("hellogithub.html", name=input_name)


@app.route("/query")
def query():
    query = request.args.get('q')
    return process_query(query)


def process_query(query):
    add_match = re.search(r"What is (\d+) plus (\d+)?", query, re.I)
    mul_match = re.search(r"What is (\d+) multiplied by (\d+)?", query, re.I)
    minus_match = re.search(r"What is (\d+) minus (\d+)?", query, re.I)
    pa = r"Which of the following numbers are primes: ([\d, ]+)?"
    prime_match = re.search(pa, query, re.I)
    s_q = r"Which of the following numbers is both a square and a cube: " \
        r"([\d, ]+)?"
    s_q_match = re.search(s_q, query, re.I)
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif query == "asteroids":
        return "Unknown"
    elif add_match:
        num1, num2 = map(int, add_match.groups())
        return str(num1 + num2)
    elif mul_match:
        num1, num2 = map(int, mul_match.groups())
        return str(num1 * num2)
    elif minus_match:
        num1, num2 = map(int, minus_match.groups())
        return str(num1 - num2)
    elif prime_match:
        numbers_str = prime_match.group(1)
        if numbers_str:
            numbers = list(map(int, numbers_str.split(',')))
            prime_numbers = [
                str(x) for x in numbers
                if x > 1 and
                all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
            ]
        if prime_numbers:
            return ", ".join(prime_numbers)
        else:
            return "No prime numbers found."
    elif s_q_match:
        numbers_str = s_q_match.group(1)
        if numbers_str:
            numbers = list(map(int, numbers_str.split(',')))
            both_cube_and_square_numbers = [
                str(x) for x in numbers
                if round(x ** (1/3)) ** 3 == x and x == round(x ** 0.5) ** 2
               ]
            if both_cube_and_square_numbers:
                return ", ".join(both_cube_and_square_numbers)
            else:
                return "No numbers found that are both cubes and squares."
    elif query == "What is your name?":
        return "VW50"
    else:
        return f"You searched for: {query}"


def is_prime(n):
    if n < 2:
        return ""
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return ""
    return str(n)
