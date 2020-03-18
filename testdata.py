import re
data="(b5e09d2)-[:`中文名`]->(b5e09d2)"
a='(fa9c8de)-[:`外文名`]->(e23455a)'
b='(fa9c8de)-[:`命名组织`]->(c980278)'
p=re.compile(".*?:`(.*?)`]->.*?",re.S)
result=re.findall(p,a)
print(result)

