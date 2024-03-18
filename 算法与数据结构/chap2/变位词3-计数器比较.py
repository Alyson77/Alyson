def anagramSolution2(s1,s2):
    c1=[0]*26
    c2=[0]*26
    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a') #计算s1[i]与a的差，就是c1中各字母的索引值
        c1[pos]=c1[pos]+1 #初始值都是0，但各个位置代表a~z,c1[0]代表a的个数
    for i in range(len(s2)):
        pos=ord(s2[i])-ord('a')
        c2[pos]=c2[pos]+1
    j=0
    stillOK=True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j=j+1
        else:
            stillOK=False
    return stillOK
print(anagramSolution2('bac','cba'))

