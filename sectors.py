import finance_yql
import pickle
import operator

SECTORS_CACHE_FILENAME = "sectors.cache"


class Industry(object):
    def __init__(self, id, name):
        self.name = name
        self.id = int(id)

    def __unicode__(self):
        return unicode(self.id) + ' - ' + self.name


class Sector(object):
    def __init__(self, name, industry_list):
        self.name = name
        if not isinstance(industry_list, list):
            industry_list = [industry_list]

        self.industry_list = [Industry(c['id'], c['name'])
                              for c in industry_list]

    def __unicode__(self):
        return self.name


def load_sectors_from_cache():
    try:
        with open(SECTORS_CACHE_FILENAME, "r") as f:
            sectors = pickle.load(f)

    except Exception as e:
        print e
        sectors = []

    return sectors

def update_sectors():
    query_prepend = 'use "http://www.johnmwilson.co.uk/yahoo/finance/yahoo.finance.sectors.xml" as yahoo.finance.sectors; '
    query = query_prepend + 'select * from yahoo.finance.sectors'
    result = finance_yql.execute(query)

    sectors = sorted([Sector(c['name'], c['industry'])
                      for c in result.results['sector']
                      if isinstance(c, dict)],
                     key = operator.attrgetter('name'))

    with open(SECTORS_CACHE_FILENAME, "w") as f:
        pickle.dump(sectors, f)

    return sectors

def update_industries(sectors, sector_indices=[]):
    if len(sector_indices) == 0:
        sector_indices = range(len(sectors))

    industries = []
    for index in sector_indices:
        industries += sectors[index].industry_list

    industries.sort(key = lambda x: x.id)
    return industries
