import csv

idNum = 0

with open('dataFile.csv') as csvfile:
    with open('cleanData.csv', 'w') as csvwrite:

        readCSV = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(csvwrite, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        for row in readCSV:
            cName = row[0]
            iNum = row[1]
            cntry = row [2]
            dScore = row[3]
            pForm = row[4]
            scope1 = row[5]
            scope2 = row[6]
            currScore = row[7]

            if not row[1]:
                iNum = '""'
            if not row[2]:
                cntry = '""'
            if not row[3]:
                dScore = -1
            if not row[4]:
                pForm = '""'
            if not row[5]:
                scope1 = -1
            if not row[6]:
                scope2 = -1
            if not row[7]:
                currScore = -1

            # print(idNum)

            writer.writerow([idNum, cName, iNum, cntry, dScore, pForm, scope1, scope2, currScore])

            idNum += 1






        