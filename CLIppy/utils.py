from functools import wraps
import itertools
import os
import re
import sys


# via https://stackoverflow.com/questions/6197409/ordered-sets-python-2-7
def dedupe(lst):
    """list -> deduped iterable of items, in order"""
    from collections import OrderedDict
    return list(OrderedDict((item, None) for item in lst).keys())


def fail_gracefully(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except(KeyboardInterrupt):
            sys.exit(0)
    return wrapper


def flatten(itable):
    """Iterable -> flattened list"""
    return list(itertools.chain.from_iterable(itable))


def get_from_file(suffix=None, prefix=None, sep='_', fname=None, dirname=None, f=None):
    """Get line-by-line list from file `dirname/prefix_suffix` OR `fname`

    :suffix: str
    :prefix: str
    :sep: str separator b/w suffix & prefix
    :fname: str filename
    :dirname: directory (default: path/to/scriptdir)
    :f: direct path/to/file
    :returns: line-by-line list of strs
    """
    assert (suffix and prefix) or f or fname, 'Must give suffix+prefix or fname or path/to/f !'
    assert (bool(suffix and prefix) + bool(fname) + bool(f)) == 1, 'Unclear: must specify among suffix+prefix vs. fname vs. path/to/f !'

    COMMENT_CHAR = '#'
    PATTERN = re.compile('{}.*$'.format(COMMENT_CHAR))

    if not f:
        dirname = (os.path.dirname(os.path.realpath(__file__)) if dirname is None
                   else dirname)
        fname = fname if fname is not None else sep.join((prefix, str(suffix)))
        f = os.path.join(dirname, fname)

    with open(f, 'r') as openfile:
        strlst = [re.sub(PATTERN, '', l.strip().lower()) for l in openfile
                  if not l.startswith(COMMENT_CHAR)]

    return strlst


class AttrDict(dict):
    """dicts w/ less typing

    via https://danijar.com/patterns-for-fast-prototyping-with-tensorflow/
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
