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