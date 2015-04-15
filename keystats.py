import finance_yql
import pprint
import cStringIO

class Keyval(str):
    def __new__(cls, content, term):
        obj = str.__new__(cls, content)
        obj.term = term
        return obj

class Keystats(object):
    def __init__(self, stats_dict):
        if not isinstance(stats_dict, dict):
            raise RuntimeError("Non-dict type passed to ctor of Keystats")
        for k, v in stats_dict.items():
            try:
                if k == "TrailingAnnualDividendYield":
                    setattr(self, "TrailingAnnualDividend", Keyval(v[0], 'N/A'))
                    setattr(self, "TrailingAnnualYield", Keyval(v[1], 'N/A'))
                elif isinstance(v, list):
                    for sv in v:
                        setattr(self, k+''.join(sv['term'].split(' ')),
                                Keyval(sv['content'], sv['term']))
                elif isinstance(v, dict):
                    setattr(self, k, Keyval(v['content'], v['term']))
                elif isinstance(v, unicode) or isinstance(v, str):
                    setattr(self, k, Keyval(v, 'N/A'))
                else:
                    raise ValueError("Can't handle type %s" % type(v))
            except Exception as e:
                print "Skipping param %s (%s)" % (str(k), e)
                print v
                pass


    def __repr__(self):
        ret = cStringIO.StringIO()
        pp = pprint.PrettyPrinter(indent=2, stream=ret)
        pp.pprint(self.__dict__)
        return ret.getvalue()

    def __getattr__(self, key):
        if key not in self.__dict__.keys():
            return 'N/A'
        else:
            return self.__dict__[key]

def get_single_keystat(symbol):

    query_prepend = 'use "http://www.johnmwilson.co.uk/yahoo/finance/yahoo.finance.keystats.xml" as yahoo.finance.keystats; '
    query = query_prepend + 'select * from yahoo.finance.keystats where symbol="%s"' % \
            symbol

    result = finance_yql.execute(query)
    stats = result.results['stats']

    # Stats is a list of metrics for each ticker returned from the query
    ret = { stats['symbol']: Keystats(stats) }

    return ret


def get_keystats(symbols):
    if hasattr(symbols, '__iter__'):
        if len(symbols) == 1:
            return get_single_keystat(symbols[0])

        query_prepend = 'use "http://www.johnmwilson.co.uk/yahoo/finance/yahoo.finance.keystats.xml" as yahoo.finance.keystats; '
        query = query_prepend + 'select * from yahoo.finance.keystats where symbol in (%s)' % \
                ('"' + '", "'.join(symbols) + '"')

        result = finance_yql.execute(query)
        stats_list = result.results['stats']

        # Stats is a list of metrics for each ticker returned from the query
        ret = {}
        for stats in stats_list:
            ret[stats['symbol']] = Keystats(stats)
        return ret
