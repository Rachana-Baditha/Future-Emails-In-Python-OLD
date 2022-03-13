from datetime import date as dt
import json
from EmailStats import STATS

# emailinfo = {}

# emailinfo["SerialNo"] = 10
# emailinfo["Queue"] = []


# with open("GlobalEmailInfo.json","w") as info:
#     json.dump(emailinfo, info)

stats = {}

stats["TotalSent"] = 0
stats["DaysLeft"] = 0
stats[""]

with open(STATS,"w") as statf:
    json.dump(stats, statf)


