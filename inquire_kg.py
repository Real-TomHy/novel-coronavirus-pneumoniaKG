from py2neo import Graph
import re
graph = Graph('http://neo4j:1210991856hy@localhost:7474/db/data/')
def query(name):
    data = graph.run("match(p:my_entity {name:'%s'}) -[r]->(n) return p.name, r, n.name limit 50" % name)
    data = list(data)
    return get_json_data(data)



def get_json_data(data):
    json_data = {'data': [], "links": []}
    d = []

    for i in data:
        # print(i["p.Name"], i["r.relation"], i["n.Name"], i["p.cate"], i["n.cate"])
        d.append(i['p.name']+"_")
        d.append(i['n.name']+"_")
        d = list(set(d))
    name_dict = {}
    count = 0
    for j in d:
        j_array = j.split("_")

        data_item = {}
        name_dict[j_array[0]] = count
        count += 1
        data_item['name'] = j_array[0]
        #data_item['category'] = CA_LIST[j_array[1]]
        json_data['data'].append(data_item)
    for i in data:
        string=str(i['r'])
        p = re.compile(".*?:`(.*?)`]->.*?", re.S)
        result = re.findall(p, string)
        link_item = {}

        link_item['source'] = name_dict[i['p.name']]

        link_item['target'] = name_dict[i['n.name']]
        link_item['value'] = result
        json_data['links'].append(link_item)


    return json_data
def get_answer_profile(name):
    #return [get_profile(str(name))]
    pass