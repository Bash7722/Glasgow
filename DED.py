from typing import Pattern
import requests as ww


v=ww.get('https://tesla.com')

print(v.text)
