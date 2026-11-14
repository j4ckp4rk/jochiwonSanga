import json,sys
d=json.load(open(sys.argv[1],encoding="utf-8"))
for s in d:
    if "새내12길" in s["rdnmAdr"]:
        print(s["bizesNm"],s["rdnmAdr"],s["flrNo"],s["lon"],s["lat"],s["indsMclsNm"])
