def anagramSolution2(s1,s2):
    alist1=list(s1)
    alist2=list(s2)
    alist1.sort() #列表自动排序
    alist2.sort()
    stillOK=True
    pos=0

    while pos<len(s1) and stillOK:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            stillOK=False
    return stillOK

print(anagramSolution2('abc','cba'))

