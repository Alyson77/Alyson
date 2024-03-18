scores={'张三':100,'李四':98,'王五':45}
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))

values=scores.values()
print(values)
print(list(values))

items=scores.items()
print(items)
print(list(items)) #-->[('张三', 100), ('李四', 98), ('王五', 45)]