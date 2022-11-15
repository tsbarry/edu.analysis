import csv

list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)
#get the lenght of the data 
print (len(list_data))

state_data = [row for row in list_data if row['STATE'] == 'CONNECTICUT']
print(state_data)

new_data = [row for row in state_data if row["AVG_MATH_8_SCORE"] != '']
print(new_data)

#create a new list called years 
# then using a for loop we extract "YEAR" and 'AVG_MATH_8_SCORE' 
# then we append both the YEAR and AVG_MATH_8_SCORE to the new list
# last we print the list years
years = []
for row in new_data:
     year = row["YEAR"]
     average_score = row["AVG_MATH_8_SCORE"]
     years.append([year, average_score])
print(years)

# here I played around with indexing to get the years and average scores
#print(years[0][0])
#print(years[0][1])
#print(years[1][0])
#print(years[1][1])

# to calculate the percent change, i create a for loop with a range 
# this range will containt the lenght of the list years, 
# this allows us to index through it and increment by 1
for i in range(len(years)-1):
 raw_change = (float(years[i][1]) - float(years[i+1][1]))
 raw_change = raw_change / float(years[i][1])
 raw_change = raw_change * 100
 print(raw_change) 
    