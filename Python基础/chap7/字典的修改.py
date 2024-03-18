scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('张三' not in scores)

del scores['张三']
print(scores)

scores['陈六']=98
print(scores)

scores['陈六']=100
print(scores)
