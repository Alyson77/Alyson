#100~999之间的水仙花数
for i in range(100,1000):
    if i==(i//100)**3+((i%100)//10)**3+(i%10)**3:
        print(i)