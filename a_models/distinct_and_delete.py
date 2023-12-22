# Import
import mysql.connector   
import time

def distinct_and_delete(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    # print(space + "distinct_and_delete()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "     
    query += " , COUNT(*) AS count  "    
    query += " from " + entity 
    query += " where distinct_and_delete is null "  
    query += " group by name "  
    query += " HAVING count > 1 "    
    # query += " order by name asc "   
    query += " order by count desc "   
    # query += " limit 10000 "     
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    total_rows = len(result)
    # print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        count             = str(x[1])    
        # ------------------------------------------------------ 
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "]" 
        word += " __ " + count   
        word += " __ " + name   
        if(counter == 9000):
            print(word, flush=True)     
            counter = 0
        # ------------------------------------------------------ 
        distinct_and_delete_part2(entity, name, space)
        # ------------------------------------------------------ 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 

    
def distinct_and_delete_part2(entity, name, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    # print(space + "distinct_and_delete_part2()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "     
    query += " , id  "      
    query += " from " + entity 
    query += " where name like '"+str(name.replace("'", "\\'"))+"' "   
    query += " order by id asc "      
    # query += " limit 100 "      
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    # print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    total_rows = len(result)
    # print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        time.sleep(0.005)
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        idx             = str(x[1])    
        # ------------------------------------------------------
        name            = name.replace("'", "") 
        # ------------------------------------------------------ 
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name   
        word += " __ " + idx   
        # print(word, flush=True)     
        # ------------------------------------------------------ 
        if(counter == 1):
            update_dataset(entity, idx, name.strip(), space)
        else:
            delete_dataset(entity, idx, space)
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 

def update_dataset(entity, idx, name, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "update_dataset()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------   
    query_commit += " `name`='" + str(name) + "'"    
    # ----------------------------------------------------------   
    query_commit += " WHERE id = '" + str(idx) + "' "  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + query_commit, flush=True)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor()
    mycursor.execute(query_commit)
    mydb.commit()     
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------

    
def delete_dataset(entity, idx, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "delete_dataset()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "DELETE FROM `"+entity+"`  " 
    # ----------------------------------------------------------   
    query_commit += " WHERE id = '" + str(idx) + "' "  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + query_commit, flush=True)
    # ----------------------------------------------------------  
    mycursor = mydb.cursor()
    mycursor.execute(query_commit)
    mydb.commit()     
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------