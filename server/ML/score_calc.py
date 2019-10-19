import csv, sys

#Opens a csv file
#Calculates the score of the csv files based off metrics
#append a new column to the csv files to act as the Y val
#save as a new csv file

my_dict = []

#compress data and give it a scale of min emission vals to max emission vals
scope1_max = 0
scope1_min = sys.maxint
scope2_max = 0
scope2_min = sys.maxint
#load csv file
with open('map.csv',"rb") as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0

    for row in csv_reader:
        my_dict.append(row)
        if line_count == 0:
            line_count += 1
            continue

        #evaluate all scope1, scope2 max mins
        if row[11] is not "":
            if float(row[11]) > scope1_max:
                scope1_max = float(row[11])
            if float(row[11]) < scope1_min:
                scope1_min = float(row[11])

        if row[12] is not "":
            if float(row[12]) > scope1_max:
                scope2_max = float(row[12])
            if float(row[12]) < scope1_min:
                scope2_min = float(row[12])
        line_count += 1

print("Parsed {} lines from the file".format(line_count))
#dumb algorithm for calculating score for now
#disclosure score takes up 2/10
print("Range for Scope 1 is {} - {}".format(scope1_min, scope1_max))
print("Range for Scope 2 is {} - {}".format(scope2_min, scope2_max))

itr = 0

#ignore first line cause it is schema
for row in my_dict:
    if itr is 0:
        row.append("score")
        itr += 1
        continue
    if row[6] != '':
        disclosure = float(row[6])
    else:
        disclosure = 0

    if row[11] != '':
        scope1 = float(row[11])
    else:
        scope1 = 0

    if row[12] != '':
        scope2 = float(row[12])
    else:
        scope2 = 0

    score = (disclosure * 2.0 / 100) \
    + (float(scope1) * 5.0 / (scope1_max - scope1_min)) \
    + (float(scope2) * 3.0 / (scope2_max - scope2_min)) 
    row.append(score)
    #row 15 is the score
    print("Calculated score for {} is {}".format(row[0],row[15]))

    itr += 1

with open("new_file.csv", mode = "w") as new_file:
    csv_writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for line in my_dict:
        csv_writer.writerow(line)
