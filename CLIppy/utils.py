import itertools


# via https://stackoverflow.com/questions/6197409/ordered-sets-python-2-7
def dedupe(lst):
    """list -> deduped iterable of items, in order"""
    from collections import OrderedDict
    return OrderedDict((item, None) for item in lst).keys()


def flatten(itable):
    """Iterable -> flattened list"""
    return list(itertools.chain.from_iterable(itable))
