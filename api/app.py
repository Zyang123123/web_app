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


@app.route("/query")
def query():
    query = request.args.get('q')
    return process_query(query)


def process_query(query):
    add_match = re.search(r"What is (\d+) plus (\d+)?", query, re.I)
    mul_match = re.search(r"What is (\d+) multiplied by (\d+)?", query, re.I)
    minus_match = re.search(r"What is (\d+) minus (\d+)?", query, re.I)
    prime_match = re.search(r"Which of the following numbers\
            are primes: (\d+), (\d+), (\d+), (\d+), (\d+)?", query, re.I)
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
        num1, num2, num3, num4, num5 = map(int, minus_match.groups())
        return is_prime(num1) + is_prime(num2) + is_prime(num3) + \
            is_prime(num4) + is_prime(num5)
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
