lst=[{'rating':[9.7,2062397],'id':'1292052','type':['犯罪','剧情'],'title':'肖申克的救赎',
    'actor':['蒂姆·罗宾斯','摩根·弗里曼',]},
    {'rating':[9.6,1528760],'id':'1291546','type':['剧情','爱情','同性'],'title':'霸王别姬',
     'actor':['张国荣','张丰毅','巩俐','葛优']}]

name=input('请输入查询的演员：')
for item in lst:
    act_lst=item['actor']
    for actor in act_lst:
        if name in actor:
            print(name,'出演了',item['title'])
