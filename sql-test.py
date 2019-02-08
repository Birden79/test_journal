import pymssql
db_server = "36-ont-srv"
db_user = "data_read_user"
db_pwd = "1234567"
list_db = "Sensors"
journal_db = "SensorsArchiveLocal"

conn = pymssql.connect(server=db_server,user=db_user,password=db_pwd,database=list_db)
conn2 = pymssql.connect(server=db_server,user=db_user,password=db_pwd,database=journal_db)
cursor = conn.cursor(as_dict = True)
cursor2 = conn2.cursor(as_dict = True)

cursor.execute('select [ID],[sensorDesc] from sensorConfig where sensorAlgorithm is not null')

for row in cursor:    
    print("ID=%d, name=%s" % (row['ID'], row['sensorDesc']))
    cursor2.execute("select top 10 * from [sensorsJournal] where [sensorID] = '"+str(row['ID'])+"' order by [journalDateTime] desc")
    for row2 in cursor2:
        print("Object:%s Date:%s Value: %s" % (row['sensorDesc'],row2['journalDateTime'],row2['journalValue']))


