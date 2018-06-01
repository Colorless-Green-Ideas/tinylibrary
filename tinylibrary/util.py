import logging
from collections import OrderedDict
import attr
import requests
import xmltodict

logger = logging.getLogger(__name__)
PREFERED_SYSTEM = "lcc" # Library of Congress categorization system


@attr.s
class ClassificationResult():
    title = attr.ib(type=str)
    author = attr.ib(type=str)
    lcc_number = attr.ib(type=str)
    isbn = attr.ib(type=str)


def _check_classify(xmldict: OrderedDict) -> None:
    # Response Codes
    # 0:  Success. Single-work summary response provided.
    # 2:  Success. Single-work detail response provided.
    # 4:  Success. Multi-work response provided.
    # 100:    No input. The method requires an input argument.
    # 101:    Invalid input. The standard number argument is invalid.
    # 102:    Not found. No data found for the input argument.
    # 200:    Unexpected error.
    if xmldict['classify']['response']['@code'] in ["101", "100", "102", "200"]:
        logger.info(xmldict['classify']['response']['@code'])
        logger.debug(xmldict)
        raise Exception("Bad status code from OCLC Classify")


def _get_reccs(owi:str, isbn:str) -> ClassificationResult:
    payload = {"summary": "True", 'owi': owi}
    r = requests.get('http://classify.oclc.org/classify2/Classify' , params=payload)
    r.raise_for_status()
    tree: OrderedDict = xmltodict.parse(r.text)
    _check_classify(tree)
    try:
        sfa = tree['classify']['recommendations'][PREFERED_SYSTEM]['mostPopular']['@sfa']
    except KeyError:
        logger.error("Wtf oclc: %s", tree)
    return ClassificationResult(title=tree['classify']['work']['@title'], lcc_number=sfa, author=tree['classify']['work']['@author'], isbn=isbn)

def fetch_data(isbn: str) -> ClassificationResult:
    "Takes an isbn and returns a good catagory for it. Thanks OCLC!"
    payload = {"summary": "True", "isbn": isbn}
    r = requests.get('http://classify.oclc.org/classify2/Classify' , params=payload)
    r.raise_for_status()
    tree: OrderedDict = xmltodict.parse(r.text)
    _check_classify(tree)
    if "work" in tree['classify']:
        work = tree['classify']['work']
    else:
        work = tree['classify']['works']['work'][0]

    # get classification of specific work
    recc_class = _get_reccs(work["@owi"], isbn)
    return recc_class
