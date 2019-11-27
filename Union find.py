import collections
def unionfind(syn):
        ans=collections.defaultdict(list)
        tran={}
        for pair in syn:
            tran[pair[0]]=pair[0]
            tran[pair[1]]=pair[1]
        for pair in syn:
            tran[pair[0]]=pair[1]
        for key in tran:
            while(1):
                father=tran[key]
                if father!=tran[father]:
                    tran[key]=tran[father]
                else:
                    break
        for key,value in tran.items():
            ans[value].append(key)
        return list(ans.values())

if __name__=="__main__":
    print(unionfind([["happy","joy"],["sad","sorrow"],["joy","cheerful"]]))