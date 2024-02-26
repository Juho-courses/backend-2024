# import requests as rr
from requests import get
from funktiot import plus

r = get("https://samk.fi")
print(r.status_code)

print(plus(123, 312))
