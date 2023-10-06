from typing import List

def longCommon(strs: List[str]) -> str:
    ls = []

    for i in range(0, len(strs)):
        a = list(strs[i])
        ls.append(a)
    
    return ls

test = ["Marcus","is", "broke", "as", "fuck"]
for i in longCommon(test):
    print(i)