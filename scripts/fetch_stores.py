import os,sys,json,urllib.request,urllib.parse
key=os.environ["SK"]
cx,cy,r=sys.argv[1],sys.argv[2],sys.argv[3]
out=[];p=1
while True:
    q=urllib.parse.urlencode({"serviceKey":key,"radius":r,"cx":cx,"cy":cy,"pageNo":p,"numOfRows":1000,"type":"json"})
    d=json.load(urllib.request.urlopen("https://apis.data.go.kr/B553077/api/open/sdsc2/storeListInRadius?"+q,timeout=60))
    it=d["body"]["items"];out+=it
    if len(out)>=d["body"]["totalCount"] or not it:break
    p+=1
json.dump(out,open(sys.argv[4],"w",encoding="utf-8"),ensure_ascii=False)
print(len(out))
