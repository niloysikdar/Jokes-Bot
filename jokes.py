import requests
import json
import random

linkslist = ["https://v2.jokeapi.dev/joke/Any",
             "https://official-joke-api.appspot.com/random_joke"]


def from_first():
    final_url = linkslist[0]
    response = requests.get(final_url)
    json_response = json.loads(response.text)
    type_of_joke = json_response["type"]
    if (type_of_joke == "single"):
        final_joke = json_response["joke"]

    else:
        setup = json_response["setup"]
        delivery = json_response["delivery"]
        final_joke = setup + "\n" + delivery

    return final_joke


def from_second():
    final_url = linkslist[1]
    response = requests.get(final_url)
    json_response = json.loads(response.text)
    setup = json_response["setup"]
    punchline = json_response["punchline"]
    final_joke = setup + "\n" + punchline
    return final_joke


def get_jokes():
    number = random.randint(0, 1)
    if (number == 0):
        res = from_first()
    else:
        res = from_second()

    return res
