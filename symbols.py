import finance_yql
import pickle
import operator

SYMBOLS_CACHE_FILENAME = "symbols.cache"

class Symbol(object):
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    def __unicode__(self):
        return self.symbol + " - " + self.name


def load_symbols_from_cache(filt='.L'):
    try:
        with open(SYMBOLS_CACHE_FILENAME, "r") as f:
            symbols_list = pickle.load(f)

            symbols = sorted([Symbol(c['symbol'], c['name'])
                              for c in symbols_list
                              if isinstance(c, dict)
                              and filt in c['symbol']],
                              key = operator.attrgetter('symbol'))
    except Exception as e:
        print e
        symbols = []

    return symbols

def update_symbols(filt='.L'):
    query_prepend = 'use "http://www.johnmwilson.co.uk/yahoo/finance/yahoo.finance.sectors.xml" as yahoo.finance.sectors; '
    #query = query_prepend + 'select * from yahoo.finance.sectors'
    query = query_prepend + 'select * from yahoo.finance.industry ' \
            'where id in (select industry.id from yahoo.finance.sectors)'
    result = finance_yql.execute(query)

    symbols_list = []
    for r in result.results['industry']:
        if 'company' not in r.keys():
            continue
        symbols_list += r['company']

    with open(SYMBOLS_CACHE_FILENAME, "w") as f:
        pickle.dump(symbols_list, f)

    symbols = sorted([Symbol(c['symbol'], c['name']) for c in symbols_list
                      if isinstance(c, dict) and filt in c['symbol']],
                     key = operator.attrgetter('symbol'))
    return symbols

