import requests
import xmltodict

def fetch_data(isbn):
    payload = {"summary": "True", "isbn": isbn}
    r = requests.get('http://classify.oclc.org/classify2/Classify' , params=payload)
    r.raise_for_status()
    tree = xmltodict.parse(r.text)
    return tree['classify']['work']