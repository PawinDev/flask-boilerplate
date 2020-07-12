import psycopg2
import os
try:
    # db_secret = os.environ["DATABASE_URL"]
    db_secret = 'postgres://vlkyhzujukdowu:1f7b4adec4f0685fe183f22949f40b01294729191c5b4ad3d6819dad247df801@ec2-3-211-48-92.compute-1.amazonaws.com:5432/daheo9mredap6r'
    connection = psycopg2.connect(db_secret)
    connection.set_session(autocommit=True)


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

def getStudentData():
    cur = connection.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    print(rows)
    # print('student firstname:')
    # for row in rows:
    #     print("   ", row)
    # cur.close()
    return rows
getStudentData()
