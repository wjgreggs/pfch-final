import json
import csv

nodes = {}
edges = {}

node_counter = 1

data = json.load(open('complete.json'))

for program in data['programs']:

    for concerts in program['concerts']:
        if "Venue" in concerts:
            if concerts['Venue'] not in nodes:
                nodes[concerts['Venue']] = node_counter
                node_counter = node_counter + 1


    for work in program['works']:

        if 'composerName' in work:
            if work['composerName'] not in nodes:
                nodes[work['composerName']] = node_counter
                node_counter = node_counter + 1
           
for program in data['programs']:
    
    for concerts in program['concerts']:

        if 'Venue' in concerts:
            venue_id = nodes[concerts['Venue']]

    for work in program['works']:

        if 'composerName' in work:

            composer_id = nodes[work['composerName']]
        

            relationship = f"{composer_id}-{venue_id}"

            if relationship in edges:
                edges[relationship] = edges[relationship] + 1

            else:
                edges[relationship] = 1

#print(edges) 

with open('nodes_venues.csv', 'w') as nodefile:
    writer = csv.writer(nodefile, delimiter=';')
    writer.writerow (["Id", "Label"])

    for name in nodes:
        graph_id = nodes[name]
        writer.writerow([graph_id,name])

with open('edges_venues.csv', 'w') as edgefile:
    writer = csv.writer(edgefile,delimiter=';')
    writer.writerow (["Source","Target","Weight"])

    
    for edge in edges:
        print(edge)

        source_target = edge.split('-')
        source = source_target[0]
        target = source_target[1]
        weight = edges[edge]

        writer.writerow([source,target,weight])
