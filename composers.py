import json
import csv

# each record in complete.json is structed like this
# {
#	"concerts" : [ { metadata about the concert, time, etc. no identifiers  }],
#	"works" : [ { metadata about each work performed, there are IDs so you can say one work was performed at different concerts }]
#	 other metadat about the program
# }


# lets make a place to store information about the works
# and conductors
all_works = {}

# todo: composers
all_composers = {}



# so if if we want to count the works by decade we need to loop throuhg the programs
all_programs = json.load(open('complete.json'))

# everythign lives in this key "programs"
for program in all_programs['programs']:

	# an the works for that program
	for work in program['works']:

		if work['ID'] != "0*":
			if 'composerName' in work:
				composer = work["composerName"]
			else:
				composer = "unknown"

			# do we have it already?
			if composer not in all_works:
				all_works[composer] = { "composer" : composer, "dates": [], "decades" : []	}


		# if we get here it has been created, so add in this date to the list of dates
		# the date is not stored at the work level, but at the program level
		all_works[composer]['dates'].append(program["season"])


# we can loop through them now, by work id
for composer in all_works:

	#print(all_works[composer])

	# and here are all the dates
	for date in all_works[composer]['dates']:

		# to make the decade, we can just take the first piece of the range, remove the last year and change it to a zero
		# for example 2019-20 becomes
		# 2019 then
		# 2010
		# so it happened in the 2010s

		decade = date
		decade = decade[0:4] # take the first 4 charaters of the string
		# now take the first three and and a zero to the end
		decade = decade[0:3] + '0' 
		# now we have decade


		# lets keep count per decade, add that decade to the list of decades it was performed, there maybe duplicates, that's fine were going to count them
		all_works[composer]['decades'].append(decade)




		
	print(all_works[composer])

		

# lets make a CSV of all the works adn their occurances by decade
# these will be the fields for our CSV
# each decade will have a count
fields = ['composer','1840','1850','1860','1870','1880','1890','1900','1910','1920','1930','1940','1950','1960','1970','1980','1990','2000','2010','2020']

with open('composer_with_decade_count.csv','w') as outfile:

	writer = csv.DictWriter(outfile,fieldnames=fields)

	writer.writeheader()

	# loop throuh again
	for composer in all_works:

		# lets build a dictonary for each work


		work= {
			"composer": all_works[composer]['composer'],
			# and now all the years we just count the number of times that decade appears in our list of decades it was played
			'1840': all_works[composer]['decades'].count('1840'),
			'1850': all_works[composer]['decades'].count('1850'),
			'1860': all_works[composer]['decades'].count('1860'),
			'1870': all_works[composer]['decades'].count('1870'),
			'1880': all_works[composer]['decades'].count('1880'),
			'1890': all_works[composer]['decades'].count('1890'),
			'1900': all_works[composer]['decades'].count('1900'),
			'1910': all_works[composer]['decades'].count('1910'),
			'1920': all_works[composer]['decades'].count('1920'),
			'1930': all_works[composer]['decades'].count('1930'),
			'1940': all_works[composer]['decades'].count('1940'),
			'1950': all_works[composer]['decades'].count('1950'),
			'1960': all_works[composer]['decades'].count('1960'),
			'1970': all_works[composer]['decades'].count('1970'),
			'1980': all_works[composer]['decades'].count('1980'),
			'1990': all_works[composer]['decades'].count('1990'),
			'2000': all_works[composer]['decades'].count('2000'),
			'2010': all_works[composer]['decades'].count('2010'),
			'2020': all_works[composer]['decades'].count('2020')
		}

		# write it to our csv
		writer.writerow(work)