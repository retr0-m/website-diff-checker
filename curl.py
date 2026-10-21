import requests



def fetch(url: str) -> str: 
    r = requests.get(url)
    return r.text

