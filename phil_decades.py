# Download philharmonic json dataset
# Extract data 
# Reshape data by decade using season key
# Group performances by decade
# Find compelling trends in performances 
# Make visualizations of findings 

import json
from collections import Counter

#transform into a python dict
with open('complete.json', 'r') as all_performances:
    all_data = json.load(all_performances)

# Make programs by decade into keys
programs_by_decade = {}
for program in all_data['programs']:
    programs_by_decade.setdefault(program['season'][:3], []).append(program)

# Make composer counter    
composer_counts = {}
for decade, programs in programs_by_decade.items():
    composers = []
    for program in programs:
        for work in program['works']:
            if 'composerName' in work:
                composers.append(work['composerName'])
    counts = Counter(composers)
    composer_counts[decade] = counts

    # output 
    print(f"{decade}0s:")
    for comp, num in counts.most_common(10):
        print(f"{num}   {comp}")
    print()



