import yql
y = yql.Public()

def execute(query):
    return y.execute(query, env="store://datatables.org/alltableswithkeys")

