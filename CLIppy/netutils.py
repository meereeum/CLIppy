from functools import wraps
import itertools
import re
import requests
import sys
from urllib.parse import quote_plus

from bs4 import BeautifulSoup
from selenium import webdriver


def connect_gracefully(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except(requests.ConnectionError):
            #print('\nno connection...\n')
            print('no connection...\n')
            sys.exit(0)
    return wrapper


def safe_encode(*args, pattern=' ', space_char='+'):
    """default: replace spaces with '+'
    """
    # SPACE_CHAR = '+'
    # return SPACE_CHAR.join(args).replace(' ', SPACE_CHAR)
    # args = (quote_plus(str(arg) for arg in args))
    args = itertools.chain.from_iterable(
        (quote_plus(argwd) for argwd in arg.split(pattern)) for arg in args)
    return re.sub(re.compile(pattern),
                  space_char,
                  space_char.join(args),
                  re.DOTALL)


def compose_query(base_url, d_params=None):
    """Compose query URL, as per requests lib"""
    d_params = d_params if d_params is not None else {}

    paramstr = '?' if d_params is not None else ''
    paramstr += '&'.join(('{}={}'.format(k, safe_encode(v))
                         for k,v in d_params.items()))

    return base_url + paramstr


# @connect_gracefully
def soup_me(*args, verbose=False, encoding='base6', from_headless=False,
            **kwargs):
    # N.B. args expects base_url (str) + optional params (dict)
    DEFAULT = {'headers': {'User-agent': 'shiffy47'}}
    kwargs = {**DEFAULT, **kwargs}

    if verbose:
        print('pinging...')
        print(args)
        print(kwargs)

    def request_html(*args, encoding=encoding, **kwargs):
        requested = requests.get(*args, **kwargs)
        if encoding:
            requested.encoding = encoding # fix Petite Sour Rosé
        return requested.text

    def request_js(*args, encoding=encoding, **kwargs): # TODO - encoding ?
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            browser = webdriver.PhantomJS() # TODO headless ffox
        #options = webdriver.firefox.options.Options()
        #options.set_headless(headless=True)
        #geckodriver = '/usr/local/bin/geckodriver'
        #browser = webdriver.Firefox(executable_path=geckodriver,
        #                            firefox_options=options)
        browser.get(compose_query(*args))
        return browser.page_source

    requester = request_js if from_headless else request_html
    try:
        requesttxt = requester(*args, encoding=encoding, **kwargs)
    except(requests.exceptions.ConnectionError): # TODO selenium exception ?
        print('\nno connection...\n')
        sys.exit(0)

    soup = BeautifulSoup(requesttxt, 'lxml')

    if verbose:
        print('...&done')

    return soup
