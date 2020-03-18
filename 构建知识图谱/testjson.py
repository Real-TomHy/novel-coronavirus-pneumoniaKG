import urllib
import re
#print(urllib.parse.unquote('<http://www.openkg.cn/2019-nCoV/baidubaike/resource/C-%E5%8F%8D%E5%BA%94%E8%9B%8B%E7%99%BD> <http://www.openkg.cn/2019-nCoV/baidubaike/property/%E4%BD%9C%E7%94%A8> "身体保护"'))
# with open(r"F:\知识图谱资料\新冠知识图谱\2019nCoV-新冠baidubaike\baidubaike_infobox.nt","r",encoding='gbk') as f1:#原txt存放路径
# # with open("Noun.txt","r") as f:
#     Readeddata = f1.readlines() ##将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件
# f2 = open(r"F:\知识图谱资料\新冠知识图谱\2019nCoV-新冠baidubaike\newdata.txt","w") #新txt存放路径
# for x in Readeddata:
#     f2.write(x) #将原记事本的文件写入到另外一个记事本
# f2.close()#执行完毕，关闭文件
f3 = open(r"F:\知识图谱资料\新冠知识图谱\2019nCoV-新冠baidubaike\Threetupledata.txt","w",encoding='utf-8')
with open(r"F:\知识图谱资料\新冠知识图谱\2019nCoV-新冠baidubaike\newdata.txt","r",encoding='utf-8') as f:
    String = f.readlines()
for d in String:
    newString=urllib.parse.unquote(d)
    f3.write(newString)
f3.close()

# p=re.compile('<http://www.openkg.cn/2019-nCoV/baidubaike/resource/(.*?)> <http://www.openkg.cn/2019-nCoV/baidubaike/property/(.*?)> >(.*?)>',re.S)
# result=re.findall(p,)
# print(result)

