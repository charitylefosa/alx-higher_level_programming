#!/usr/bin/python3
combo = ["{}{}".format(i, j) for i in range(10) for j in range(10) if i < j]
if combo != 89:
    result = ", ".join(combo)
    print(result)
else:
    print("")
