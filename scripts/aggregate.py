import json,sys,collections
for r in ("300","500"):
    d=json.load(open(sys.argv[1]+"/r%s.json"%r,encoding="utf-8"))
    print("== 반경",r,"m 총",len(d))
    c=collections.Counter(s["indsMclsNm"] for s in d)
    print(" 중분류 상위:",", ".join("%s %d"%k for k in c.most_common(18)))
    s2=collections.Counter(s["indsSclsNm"] for s in d)
    keys=["카페","커피","편의점","슈퍼","세탁","약국","의원","치과","한의원","헬스","피트니스","필라테스","스터디","독서실","학원","미용","반찬","베이커리","제과","치킨","분식","pc","PC","무인","반려","애견","호프","요리주점","노래","당구","포장마차","펍"]
    print(" 소분류 키워드:")
    for k in keys:
        n=sum(v for t,v in s2.items() if k in t)
        if n: print("   ",k,n)
    print(" 대분류:",", ".join("%s %d"%k for k in collections.Counter(s["indsLclsNm"] for s in d).most_common()))
