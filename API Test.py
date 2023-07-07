#!/usr/bin/env python3



import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.sfgov.org", None)


# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("ab4h-6ztd", where="citation_location LIKE '%VALENCIA%' AND citation_issued_datetime >= '2023-06-01' AND (violation LIKE 'V21211' OR violation LIKE 'TRC7.2.34' OR violation LIKE 'TRC7.2.70')",limit=200)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
results_df = results_df.drop(results_df.columns[[5,6,7,8]], axis=1)
dflist = results_df.values.tolist()
for item in dflist:
	print(item)
print(len(dflist))