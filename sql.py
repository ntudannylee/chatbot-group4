import pyodbc

def DB_query(query):
    server = 'db-chatbot.database.windows.net'
    database = 'restaurant_DB'
    username = 'rest-admin'
    password = 'Chatbot4'   
    # driver= '{ODBC Driver 17 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    result = []
    while row:
        # # print(row[0], row[1], row[2])
        # result.append(row.ID)
        # result.append(row.recently)
        # result.append(row.favorite)
        result.append(row)
        row = cursor.fetchone()
    output = []
    for i in range(len(result)):
        row = result[i]
        for j in range(len(row)):
            output.append(row[j])
    return output

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

# #Sample select query 
# cursor.execute("SELECT * FROM user_info") 
# row = cursor.fetchone() 
# while row: 
#     print(row[0], row[1], row[2])
#     row = cursor.fetchone()

# with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT * FROM user_info")
#         row = cursor.fetchone()
#         while row:
#             print (str(row[0]) + " " + str(row[1]))
#             row = cursor.fetchone()