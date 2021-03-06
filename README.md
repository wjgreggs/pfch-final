# pfch-final
NY Philharmonic data project

These scripts are all written to interact with the open json dataset "Performance History," which is a comprehensive listing of all performances at the New York Philharmonic from 1842-present. It can be found as the file "complete.json" at https://github.com/nyphilarchive/PerformanceHistory/tree/master/Programs/json. 

Each script takes values from two keys in the nested dataset (e.g. "composerName" or "Venue") to create a csv file, titled "nodes-[name]" that includes a unique ID column generated by counters and a labels column populated the key values. An "edges-[name]" csv file with three columns—Source, Target, and Weight—is generated by creating a source-target relationship between the two key values via a string and weighting that relationship with a counter. The string is then split back into Source and Target.   

The resultant nodes and edges csv files are then imported into Gephi where the data can be maniuplated via layout algorithms, filters, statistical analysis, and appearance to create visualized network graphs. 

ISSUES WITH CODE

• All of these scripts except "works-graph.py", which had a unhashable dict error I couldn't resolve, produce the desired csv files, which have been uploaded in a zip file to Canvas.

ISSUES WITH GEPHI

• Although Gephi was designed to handle large datasets, I was not able to make a graph that could manage the scale of my data. In order to view the entire image, I have to zoom out so much that the labels are no longer visible, thus making the relationships between different nodes unclear. 

• When zooming in to highlight nodes and read labels, the labels still create clutter. A number of layouts required me to hide non-selected nodes in order to make sense of things. Unfortunately, this makes it impossible to see the label of the nodes connected to highlighted node. Even when all the labels are displayed, zooming in means that you cannot see all the nodes the selected nodes connects to.

• For the graphs that are related to performances "by Decade," the labels for the decade nodes does not display. If I had figured out how to fix this error, these two graphs would have presented the most compelling relationships I found. As is, they only show that there *are* interesting relationships present, but not *what* exactly they represent (i.e. it is clear that the composer or venue selected have a relationship to particular decades, but it is impossible to tell which decade that is).

• Gephi's native exporting abilities are weak, allowing the user to generate only svg/pdf/png files. These take away all the interactivity from the graphs. What is produced (from settings in the Preview tab) is also quite different than image in Gephi, often with a lot of added illustration. After consulting the internet, I imported the plugin Sigma.js, which exports the graph as web page, but setting it up through Github required more Javascript and HTML skills than I possess. I have uploaded my deliverables as a Gephi file into Canvas. Each graph is a different (titled) workspace.  

• There is no undo/revert function in Gephi. I lost a lot of time and content when I misstepped.  
