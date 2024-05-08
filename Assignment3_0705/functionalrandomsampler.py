import random

sampledict = {"abcd": 0.04, "efgh": 0.07, "ijkl": 0.15, "mnop": 0.22, "qrst": 0.4, "uvwxyz": 0.12}
cnt = 10

def drawSample(pmfdict: dict[str: float], n: int) -> list[str]:
    lstkey = list(pmfdict.keys())
    for i in range(1, len(lstkey)):
        pmfdict[lstkey[i]] += pmfdict[lstkey[i-1]]
    randomlst = []    
    for i in range(n):
        rf = random.uniform(0, 1)
        flag = True
        key = 0
        while flag:
            if rf<=pmfdict[lstkey[key]]:
                randomlst.append(lstkey[key])
                flag = False
            key += 1
    return randomlst
    
print(drawSample(sampledict, cnt))