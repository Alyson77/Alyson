def anagramSolution1(s1,s2):
    alist=list(s2)
    pos1=0
    if len(s1)<len(alist):
        stillOK=False
    else:
        stillOK=True

    while pos1<len(s1) and stillOK:
        pos2=0
        found=False
        while pos2<len(alist) and not found:
            if s1[pos1]==alist[pos2]:
                found=True
            else:
                pos2=pos2+1
        if found:
            alist[pos2]=None #s2为字符串，无法修改单独字符，所以转化成alist列表即可重新赋值
        else:
            stillOK=False
        pos1=pos1+1
    return stillOK

print(anagramSolution1('abc','bad'))


