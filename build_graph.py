import json
import csv

nodes = {}
edges = {}

node_counter = 1

data = json.load(open('complete.json'))

for program in data['programs']:

 	for work in program['works']:

 		if 'composerName' in work and 'conductorName' in work:
 			if work['composerName'] not in nodes:
 				nodes[work['composerName']] = node_counter
 				node_counter = node_counter + 1
 			if work['conductorName'] not in nodes:
 				nodes[work['conductorName']] = node_counter
 				node_counter = node_counter + 1


for program in data['programs']:

 	for work in program['works']:

 		if 'composerName' in work and 'conductorName' in work:

 			composer_id = nodes[work['composerName']]
 			conductor_id = nodes[work['conductorName']]

 			relantionship = f"{conductor_id}-{composer_id}"

 			if relantionship in edges:

 				edges[relantionship] = edges[relantionship] + 1

 			else:

 				edges[relantionship] = 1

# print(edges)


with open('nodes.csv','w') as nodefile:

	writer = csv.writer(nodefile,delimiter=';')

	writer.writerow(['Id','Label'])

	for name in nodes:
		graph_id = nodes[name]
		writer.writerow([graph_id,name])


with open('edges.csv','w') as edgefile:

	writer = csv.writer(edgefile,delimiter=';')

	writer.writerow(['Source','Target','Weight'])

	for edge in edges:


		source_target = edge.split('-')
		source = source_target[0]
		target = source_target[1]
		weight = edges[edge]

		writer.writerow([source,target,weight])



		# graph_id = nodes[name]
		# writer.writerow([graph_id,name])





