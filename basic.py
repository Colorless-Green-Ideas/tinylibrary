# tinylibrary
import requests
import xmltodict
import sys

def fetch_data(isbn):
    payload = {"summary": "True", "isbn": isbn}
    r = requests.get('http://classify.oclc.org/classify2/Classify' , params=payload)
    r.raise_for_status()
    tree = xmltodict.parse(r.text)
    return tree['classify']['work']

def main():
    """Take a ISBN and give nice info"""
    isbns = sys.argv[1:]
    for isbn in isbns:
        print fetch_data(isbn)['@title']



if __name__ == '__main__':
    main()