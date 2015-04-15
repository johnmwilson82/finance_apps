import keystats
# query = 'select * from yahoo.finance.industry where id in (select industry.id from yahoo.finance.sectors)'
# result = y.execute(query, env="store://datatables.org/alltableswithkeys")
# companies_list = []
# for r in result.results['industry']:
#     if 'company' not in r.keys():
#         continue
#     companies_list += r['company']
#
# companies = [c['symbol'] for c in companies_list if isinstance(c, dict) and '.L' in c['symbol']]


FTSE_SMALLCAP = [u'FOUR.L', u'888.L', u'ATT.L', u'ALY.L', u'ARW.L', u'XPP.L', 'DIA.L']

stats = keystats.get_keystats(FTSE_SMALLCAP)

import pdb
pdb.set_trace()
