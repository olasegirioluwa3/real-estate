"""Module providingFunction printing python version."""
import sys #
import requests

print("hi")
def my_printer():
    r = requests.get("https://early.school")
    return r.status_code

print(my_printer())