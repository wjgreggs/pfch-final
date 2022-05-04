import json
import csv

nodes = {}
edges = {}

node_counter = 1

data = json.load(open('complete.json'))

def decade(season):
    season[:3] + "0s"

for program in data['programs']:

    if 'season' in program:
        decade = program['season'][0:3] + '0s'
        if decade not in nodes:
            nodes[decade] = node_counter
            node_counter += 1
        for work in program['works']:
            if 'composerName' in work and 'workTitle' in work:
                if work['composerName'] not in nodes:
                    nodes[work['composerName']] = node_counter
                    node_counter = node_counter + 1

for program in data['programs']:

    if 'season' in program:
        decade = program['season'][0:3] + '0s'

        for work in program['works']:
            if 'composerName' in work:

                composer_id = nodes[work['composerName']]

                relationship = f"{composer_id}-{decade}"

                if relationship in edges:
                    edges[relationship] = edges[relationship] + 1

                else:
                    edges[relationship] = 1

with open('nodes_decades.csv', 'w') as nodefile:
    writer = csv.writer(nodefile, delimiter=';')
    writer.writerow (["Id", "Label"])

    for name in nodes:
        graph_id = nodes[name]
        writer.writerow([graph_id,name])

with open('edges_decades.csv', 'w') as edgefile:
    writer = csv.writer(edgefile,delimiter=';')
    writer.writerow (["Source","Target","Weight"])

    
    for edge in edges:
        print(edge)

        source_target = edge.split('-')
        source = source_target[0]
        target = source_target[1]
        weight = edges[edge]

        writer.writerow([source,target,weight])