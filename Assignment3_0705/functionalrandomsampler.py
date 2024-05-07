import random

sampledict = {"abcd": 0.04, "efgh": 0.07, "ijkl": 0.15, "mnop": 0.22, "qrst": 0.4, "uvwxyz": 0.12}
cnt = 10

def randomsampler(sampledict: dict[str: float], cnt: int) -> list[str]:
    dictcmf = {}
    for key in sampledict.keys():
        dictcmf[key] = sum(list(sampledict.values())[:list(sampledict.keys()).index(key)+1])
    randomlst = []
    for i in range(cnt):
        rf = random.uniform(0, 1)
        flag = True
        key = 0
        while flag:
            if rf<=dictcmf[list(dictcmf.keys())[key]]:
                randomlst.append(list(dictcmf.keys())[key])
                flag = False
            key += 1
    return randomlst
    
print(randomsampler(sampledict, cnt))