s={10,20,30,40}
s2={30,40,20,10}
print(s==s2)
print(s!=s2)

s3={10,20,30,40,50}
s4={10,20,30}
s5={10,20,60}
print(s4.issubset(s3))
print(s5.issubset(s3))
print(s3.issuperset(s4))
print(s3.issuperset(s5))
print(s4.isdisjoint(s5))