import mysql.connector

def connectToDB(dbname,password):
    user='root'
    host='localhost'
    password=password
    database=dbname

    conn=mysql.connector.connect(user=user,host=host,password=password,database=database)
    return conn

def selectFromTable(tablename,conn,attribute):
    if len(attribute)==0:
        users=f'SELECT * FROM {tablename}'
    else:
        users=' SELECT '
        for i in range(len(attribute)):
            if(i<len(attribute)-1):
                users+=f'{attribute[i]},'
            else:
                users+=attribute[i]
        users+=f' FROM {tablename}'
        
    cursor = conn.cursor()
    cursor.execute(users)
    result=cursor.fetchall()
    for i in result:
        print(i) 
    

def updateTable(attribute,tablename,where,key,conn):
    update=f'UPDATE {tablename} SET '
    if(len(attribute)>0):
        j=0
        for i in attribute:
            if(j<len(attribute)-1):
                update+=f'{i} = "{attribute[i]}" ,'
            else:
                update+=f'{i} = "{attribute[i]}" '
            j+=1
    update+='WHERE '
    if(len(where)>0):
        j=0
        for i in where:
            if(j<len(where)-1):
                update+=f'{i} = "{where[i]}" {key}'
            else:
                update+=f'{i} = "{where[i]}" '
            j+=1
    print(update)
    cursor = conn.cursor()
    cursor.execute(update)
    conn.commit()
    
def showtables(conn):
    display="Show Tables"
    cursor=conn.cursor()
    cursor.execute(display)
    result=cursor.fetchall()
    print(result)

def delete(tablename,attri,key):
    delete= ' delete from '+tablename+' where '+attri+'="'+key+'"'
    print(delete)
    cursor=conn.cursor()
    cursor.execute(delete)
    conn.commit()

conn=connectToDB('student','root')
showtables(conn)
delete('student','First_Name',"Rajesh")
d={'Last_Name':'Deshpande','Address':'Goa'}
w={'First_Name':'Priya'} 
updateTable(d,'student',w,'and',conn)
selectFromTable('student',conn,[])      