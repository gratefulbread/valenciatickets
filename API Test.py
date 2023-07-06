#!/usr/bin/env python3

#https://data.sfgov.org/resource/ab4h-6ztd.csv?$query=SELECT%0A%20%20%60citation_number%60%2C%0A%20%20%60citation_issued_datetime%60%2C%0A%20%20%60violation%60%2C%0A%20%20%60violation_desc%60%2C%0A%20%20%60citation_location%60%2C%0A%20%20%60vehicle_plate_state%60%2C%0A%20%20%60vehicle_plate%60%2C%0A%20%20%60fine_amount%60%2C%0A%20%20%60date_added%60%2C%0A%20%20%60the_geom%60%2C%0A%20%20%60%3A%40computed_region_jwn9_ihcz%60%2C%0A%20%20%60%3A%40computed_region_6qbp_sg9q%60%2C%0A%20%20%60%3A%40computed_region_qgnn_b9vv%60%2C%0A%20%20%60%3A%40computed_region_26cr_cadq%60%2C%0A%20%20%60%3A%40computed_region_ajp5_b2md%60%0AWHERE%0A%20%20caseless_contains(%60citation_location%60%2C%20%22Valencia%22)%0A%20%20AND%20((%60citation_issued_datetime%60%0A%20%20%20%20%20%20%20%20%20%20%3E%20%222023-06-01T03%3A00%3A00%22%20%3A%3A%20floating_timestamp)%0A%20%20%20%20%20%20%20%20%20AND%20(%60violation_desc%60%20NOT%20IN%20(%0A%20%20%20%20%20%20%20%20%20%20%20%22NO%20PLATES%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%22PLATECOVER%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%22STR%20CLEAN%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%22FIRE%20HYD%22%0A%20%20%20%20%20%20%20%20%20)))

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.sfgov.org", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.sfgov.org,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("ab4h-6ztd", violation = "V21211", limit=200)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
results_df = results_df.drop(results_df.columns[[2,3,5,7,8,9]], axis=1)
print(results_df)