import logging
import requests
import xmltodict


logger = logging.getLogger(__name__)
PREFERED_SYSTEM = "lcc" # Library of Congress categorization system

def _get_reccs(owi:str) -> str:
    payload = {"summary": "True", 'oclc': owi}
    r = requests.get('http://classify.oclc.org/classify2/Classify' , params=payload)
    r.raise_for_status()
    tree = xmltodict.parse(r.text)
    return tree['classify']['reccomendations'][PREFERED_SYSTEM]['mostPopular']['@sfa']

def fetch_data(isbn: str) -> str:
    "Takes an isbn and returns a good catagory for it. Thanks OCLC!"
    payload = {"summary": "True", "isbn": isbn}
    r = requests.get('http://classify.oclc.org/classify2/Classify' , params=payload)
    r.raise_for_status()
    tree = xmltodict.parse(r.text)

    if tree['classify']['workCount'] is 1:
        work = tree['classify']['works']['work'][0]
    else:
        logger.error("Don't know what to do when there's several editions")
        raise NotImplementedError

    # get classification of specific work
    recc_class = _get_reccs(work["@owi"])
    return recc_class