scores={'张三':100,'李四':98,'王五':45}
print(scores)
print(type(scores))
scores2=dict(name='张三',age=20)
print(scores2)

print(scores['张三'])
#print(scores['陈六']) -->报错 KeyError
print(scores.get('张三'))
print(scores.get('陈六')) #-->None
print(scores.get('麻七',99))
#99是查找'麻七'所对应的value不存在时提供的默认值

