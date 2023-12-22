# Import
import mysql.connector  
import time


def last_id(entity, attr, space):  
    # ----------------------------------------------------------    
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "last_id()", flush=True)
    # ----------------------------------------------------------   
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------   
    query = "Select "
    query += " id  "  
    query += " from " + entity    
    query += " where " + attr + " is null "   
    query += " order by id asc "   
    query += " limit 1 "    
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------    
    mycursor = mydb.cursor()
    mycursor.execute(query) 
    result_check = mycursor.fetchone()
    # ---------------------------------------------------------- 
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------    
    space += "__"
    # ----------------------------------------------------------   
    last_id = result_check[0] 
    # ---------------------------------------------------------- 
    print(space + "Last ID:" + str(last_id), flush=True) 
    # ----------------------------------------------------------   
    return last_id
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  

def updated_and_clean(entity, attr, old_value, new_value, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "updated_and_clean()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------  
    query_commit += " `"+attr+"`= REPLACE("+attr+", '"+old_value+"', '"+new_value+"') "    
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + query_commit, flush=True)
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

def name_to_dataset(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "name_to_dataset()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------  
    query_commit += " `dataset` = `name` "    
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + query_commit, flush=True)
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

    
def pelabelan(entity, id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "pelabelan()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select " 
    query += " id  " 
    query += " , dataset  "  
    query += " from " + entity  
    query += " where id >= "+str(id)+" "    
    query += " limit 10000 "   
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    print(space + query)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result =  mycursor.fetchall()
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    total_rows = len(result)
    print(space + "Total Row(s) : " + str(total_rows), flush=True) 
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close() 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------ 
        time.sleep(0.002)
        # ------------------------------------------------------ 
        id           = str(x[0])      
        dataset            = str(x[1].strip())
        # ------------------------------------------------------ 
        jumlah_spasi    = dataset.count(" ") 
        # ------------------------------------------------------ 
        label_o         = "O " * (jumlah_spasi + 1)
        # ------------------------------------------------------ 
        update_label_bio(entity, "label", id, label_o.strip(), dataset, jumlah_spasi, space)
        # ------------------------------------------------------ 
        # ------------------------------------------------------ 

        
def update_label_bio(entity, attr, idx, label, dataset, jumlah_spasi, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "update_label_bio()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------   
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------   
    query_commit += " `" + attr + "` = '"+str(label)+"', "  
    query_commit += " `space_length` = '"+str(jumlah_spasi)+"', "  
    query_commit += " `dataset` = '"+str(dataset.replace("'", "\\'"))+"' "  
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