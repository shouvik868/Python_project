import mysql.connector
select_query="SELECT * FROM oc_customer"
con=mysql.connector.connect(host="localhost",port=3306,user="Admin",password="Admin123",database="openshop")
curs=con.cursor()
curs.execute(select_query)
for r in curs:
    print(r[6])
con.close()
print("finished")

