from datetime import datetime, timedelta
import sys

from dateutil import parser as dparser


def convert_date(date_in, fmt_out='%Y-%m-%d'):
    """Convert string to uniform `datetime` string

    :date_in: str
    :fmt_out: string format out
    :returns: str (default: 'YYYY-MM-DD')
    """
    D_CONVERSIONS = {
        'today':    datetime.now(),
        'tom':      datetime.now() + timedelta(days=1),
        'tomorr':   datetime.now() + timedelta(days=1),
        'tomorrow': datetime.now() + timedelta(days=1),
        'mon':   'monday',
        'tues':  'tuesday',
        'wed':   'wednesday',
        'weds':  'wednesday',
        'thurs': 'thursday',
        'fri':   'friday'
    }

    # if abbrev, uncompress for parser
    date_out = D_CONVERSIONS.get(date_in.lower(), date_in)

    try: # if str, convert to datetime
        date_out = dparser.parse(date_out)
    except(AttributeError, TypeError): # already datetime
        date_out = date_out
    except(ValueError):
        print("\nI don't recognize that date.. try again ?\n")
        sys.exit(0)

    return date_out.strftime(fmt_out)
