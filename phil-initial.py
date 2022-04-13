# Download philharmonic json dataset
# Extract data 
# Reshape data by decade using season key
# Group performances by decade
# Find compelling trends in performances 
# Make visualizations of findings 

import json
import glob
import re
from textwrap import indent

season_pattern = re.compile(r'([0-9]*-[0-9]*)"')
item_counter = 0

# transform into a python dict
with open('complete.json', 'r') as all_performances:
    all_data = json.load(all_performances)


    #Make seasons into keys
    #programs_by_season = {}
    #for program in all_data['programs']:
        #programs_by_season.setdefault(program['season'], []).append(program)

    #programs_by_season.keys()
    
    # Make programs by decade into keys
    programs_by_decade = {}
    for program in all_data['programs']:
        programs_by_decade.setdefault(program['season'][:3], []).append(program)

        with open ('phil_1840s.json', 'w') as philfile1:
            json.dump(programs_by_decade['184'],philfile1,indent=2)
        
        #print(json.dumps(programs_by_decade['184'], indent=2))
        

