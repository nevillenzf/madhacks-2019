import csv
from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Integer, Numeric
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

db_string = "postgres://admin:admin@http://127.0.0.1:51894/?key=9f9ce5d9-3a3c-4514-ab16-090940cbc28c"
db = create_engine(db_string)
base = declarative_base()

class Company(base):
    __tablename__ = 'metricData'

    id = Column(Integer, primary_key=True)
    company_name = Column(String)
    isin = Column(String)
    country = Column(String)
    disclosure_score = Column(Integer)
    performance_band = Column(String)
    scope_1 = Column(Numeric)
    scope_2 = Column(Numeric)
    calc_score = Column(Numeric)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

idNum = 0
with open('newMap.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        cName = row[0]
        iNum = row[1]
        cntry = row [2]
        dScore = row[3]
        pForm = row[4]
        scope1 = row[5]
        scope2 = row[6]
        currScore = row[7]

        input = Company(id = idNum, company_name = cName, isin = iNum, country = cntry,
                        disclosure_score = dScore, performance_band = pForm,
                        scope_1 = scope1, scope_2 = scope2, calc_score = currScore)

        session.add(input)
        session.commit()
        idNum += 1






        