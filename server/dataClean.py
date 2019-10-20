import csv

load_dotenv()

# db = sqlalchemy.create_engine(
#     # sqlalchemy.engine.url.URL(
#     #     drivername="postgres+pg8000",
#     #     username=os.getenv("DBUSER"),
#     #     password=os.getenv("DBPASS"),
#     #     database=os.getenv("DBNAME"),
#     #     query={
#     #         'unix_sock': '/cloudsql/{}/.s.PGSQL.5432'.format(os.getenv("DBHOST"))
#     #     }
#     # )
#     "172.17.0.1:5432"
# )

conn = psycopg2.connect(dbname=os.getenv("DBNAME"), user=os.getenv("DBUSER"), password=os.getenv("DBPASS"), host=os.getenv("DBHOST"), port='5432', sslmode='require')
cur = conn.cursor()


# base = declarative_base()

# class Company(base):
#     __tablename__ = 'metricData'

#     id = Column(Integer, primary_key=True)
#     company_name = Column(String)
#     isin = Column(String)
#     country = Column(String)
#     disclosure_score = Column(Integer)
#     performance_band = Column(String)
#     scope_1 = Column(Numeric)
#     scope_2 = Column(Numeric)
#     calc_score = Column(Numeric)

# Session = sessionmaker(db)
# session = Session()

# base.metadata.create_all(db)

idNum = 0
with open('dataFile.csv') as csvfile:
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

        print(idNum)
        # input = Company(id = idNum, company_name = cName, isin = iNum, country = cntry,
        #                 disclosure_score = dScore, performance_band = pForm,
        #                 scope_1 = scope1, scope_2 = scope2, calc_score = currScore)

        # session.add(input)
        # session.commit()
        idNum += 1






        