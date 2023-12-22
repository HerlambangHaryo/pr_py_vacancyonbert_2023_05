# Import
import mysql.connector  
from a_models.general import *   

def lihat_data_usia(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "lihat_data_usia()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , label  "   
    query += " , id  "    
    query += " from " + entity      
    query += " where entitas = 'Usia' "  
    query += " and done is null "  
    query += " order by name asc " 
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
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        label           = str(x[1])   
        idx             = str(x[2])   
        # ------------------------------------------------------ 
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name  
        word += " __ " + label   
        print(word, flush=True)     
    # ---------------------------------------------------------- 
 
def berusia_maksimal_xx_tahun(entity, new_label, update, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "berusia_maksimal_xx_tahun()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , label  "   
    query += " , id  "   
    query += " , length  "   
    query += " from " + entity      
    query += " where entitas = 'Usia' " 
    query += " and length = 25 " 
    query += " and name like 'Berusia Maksimal%' "  
    query += " order by name asc " 
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
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        label           = str(x[1])   
        idx             = str(x[2])   
        length          = str(x[3])   
        # ------------------------------------------------------
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name   
        word += " __ " + new_label  
        word += " __ " + length  
        print(word, flush=True)    
        # ------------------------------------------------------
        if(update == 'yes'):
            pelabelan(entity, idx, new_label, space)
        else:
            print(space + "Gurung diupdate", flush=True)
    # ---------------------------------------------------------- 
  
def maksimal_usia_xx_tahun(entity, new_label, update, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "maksimal_usia_xx_tahun()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , label  "   
    query += " , id  "   
    query += " , length  "   
    query += " from " + entity      
    query += " where entitas = 'Usia' " 
    query += " and length = 22 " 
    query += " and name like 'Maksimal Usia%' "  
    query += " order by name asc " 
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
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        label           = str(x[1])   
        idx             = str(x[2])   
        length          = str(x[3])   
        # ------------------------------------------------------
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name   
        word += " __ " + new_label  
        word += " __ " + length  
        print(word, flush=True)    
        # ------------------------------------------------------
        if(update == 'yes'):
            pelabelan(entity, idx, new_label, space)
        else:
            print(space + "Gurung diupdate", flush=True)
    # ---------------------------------------------------------- 

def minimal_usia_xx_tahun(entity, new_label, update, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "minimal_usia_xx_tahun()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , label  "   
    query += " , id  "   
    query += " , length  "   
    query += " from " + entity      
    query += " where entitas = 'Usia' " 
    query += " and length = 21 " 
    query += " and name like 'Minimal Usia%' "  
    query += " order by name asc " 
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
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        label           = str(x[1])   
        idx             = str(x[2])   
        length          = str(x[3])   
        # ------------------------------------------------------
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name   
        word += " __ " + new_label  
        word += " __ " + length  
        print(word, flush=True)    
        # ------------------------------------------------------
        if(update == 'yes'):
            pelabelan(entity, idx, new_label, space)
        else:
            print(space + "Gurung diupdate", flush=True)
    # ---------------------------------------------------------- 

def General_usia_xx_tahun(entity, new_label, update, wildcard, length, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "General_usia_xx_tahun()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , label  "   
    query += " , id  "   
    query += " , length  "   
    query += " from " + entity      
    query += " where entitas = 'Usia' " 
    query += " and length = " + str(length) 
    query += " and name like '"+wildcard+"' "  
    query += " order by name asc " 
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
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        label           = str(x[1])   
        idx             = str(x[2])   
        length          = str(x[3])   
        # ------------------------------------------------------
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name   
        word += " __ " + new_label  
        word += " __ " + length  
        print(word, flush=True)    
        # ------------------------------------------------------
        if(update == 'yes'):
            pelabelan(entity, idx, new_label, space)
        else:
            print(space + "Gurung diupdate", flush=True)
    # ---------------------------------------------------------- 


def General_ver3_usia_xx_tahun(entity, new_label, update, wildcard1, wildcard2, wildcard3, length, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "General_ver3_usia_xx_tahun()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , label  "   
    query += " , id  "   
    query += " , length  "   
    query += " from " + entity      
    query += " where entitas = 'Usia' " 
    query += " and length = " + str(length) 
    query += " and name like '"+wildcard1+"' "  
    query += " and name like '"+wildcard2+"' "  
    query += " and name like '"+wildcard3+"' "  
    query += " and done is null " 
    query += " order by name asc " 
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
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        label           = str(x[1])   
        idx             = str(x[2])   
        length          = str(x[3])   
        # ------------------------------------------------------
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name   
        word += " __ " + new_label  
        word += " __ " + length  
        print(word, flush=True)    
        # ------------------------------------------------------
        if(update == 'yes'):
            pelabelan(entity, idx, new_label, space)
        else:
            print(space + "Gurung diupdate", flush=True)
    # ---------------------------------------------------------- 

def General_ver2_usia_xx_tahun(entity, new_label, update, wildcard1, wildcard2, length, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "General_ver2_usia_xx_tahun()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , label  "   
    query += " , id  "   
    query += " , length  "   
    query += " from " + entity      
    query += " where entitas = 'Usia' " 
    query += " and length = " + str(length) 
    query += " and name like '"+wildcard1+"' "  
    query += " and name like '"+wildcard2+"' "  
    query += " and done is null " 
    query += " order by name asc " 
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
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        label           = str(x[1])   
        idx             = str(x[2])   
        length          = str(x[3])   
        # ------------------------------------------------------
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name   
        word += " __ " + new_label  
        word += " __ " + length  
        print(word, flush=True)    
        # ------------------------------------------------------
        if(update == 'yes'):
            pelabelan(entity, idx, new_label, space)
        else:
            print(space + "Gurung diupdate", flush=True)
    # ---------------------------------------------------------- 

def maksimal_berusia_xx_tahun(entity, new_label, update, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "maksimal_berusia_xx_tahun()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , label  "   
    query += " , id  "   
    query += " , length  "   
    query += " from " + entity      
    query += " where entitas = 'Usia' " 
    query += " and length = 25 " 
    query += " and name like 'Maksimal Berusia%' "  
    query += " order by name asc " 
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
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        label           = str(x[1])   
        idx             = str(x[2])   
        length          = str(x[3])   
        # ------------------------------------------------------
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name   
        word += " __ " + new_label  
        word += " __ " + length  
        print(word, flush=True)    
        # ------------------------------------------------------
        if(update == 'yes'):
            pelabelan(entity, idx, new_label, space)
        else:
            print(space + "Gurung diupdate", flush=True)
    # ---------------------------------------------------------- 

def usia_maksimal_xx_tahun(entity, new_label, update, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "usia_maksimal_xx_tahun()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , label  "   
    query += " , id  "   
    query += " , length  "   
    query += " from " + entity      
    query += " where entitas = 'Usia' " 
    query += " and length = 22 " 
    query += " and name like 'usia Maksimal%' "  
    query += " order by name asc " 
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
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        label           = str(x[1])   
        idx             = str(x[2])   
        length          = str(x[3])   
        # ------------------------------------------------------
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name   
        word += " __ " + new_label  
        word += " __ " + length  
        print(word, flush=True)    
        # ------------------------------------------------------
        if(update == 'yes'):
            pelabelan(entity, idx, new_label, space)
        else:
            print(space + "Gurung diupdate", flush=True)
    # ---------------------------------------------------------- 

def usia_max_xx_tahun(entity, new_label, update, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "usia_maksimal_xx_tahun()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , label  "   
    query += " , id  "   
    query += " , length  "   
    query += " from " + entity      
    query += " where entitas = 'Usia' " 
    query += " and length = 17 " 
    query += " and name like 'usia Max%' "  
    query += " order by name asc " 
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
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        label           = str(x[1])   
        idx             = str(x[2])   
        length          = str(x[3])   
        # ------------------------------------------------------
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name   
        word += " __ " + new_label  
        word += " __ " + length  
        print(word, flush=True)    
        # ------------------------------------------------------
        if(update == 'yes'):
            pelabelan(entity, idx, new_label, space)
        else:
            print(space + "Gurung diupdate", flush=True)
    # ---------------------------------------------------------- 

def berusia_minimal_xx_tahun(entity, new_label, update, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "berusia_minimal_xx_tahun()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , label  "   
    query += " , id  "   
    query += " , length  "   
    query += " from " + entity      
    query += " where entitas = 'Usia' " 
    query += " and length = 24 " 
    query += " and name like 'Berusia Minimal%' "  
    query += " order by name asc " 
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
    counter = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0])   
        label           = str(x[1])   
        idx             = str(x[2])   
        length          = str(x[3])   
        # ------------------------------------------------------
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name    
        word += " __ " + new_label  
        word += " __ " + length  
        print(word, flush=True)    
        # ------------------------------------------------------
        if(update == 'yes'):
            pelabelan(entity, idx, new_label, space)
        else:
            print(space + "Gurung diupdate", flush=True)
    # ---------------------------------------------------------- 

def bukan_usia(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "bukan_usia()", flush=True)
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
    query += " where entitas = 'Usia' " 
    query += " order by name asc " 
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
    counter = 0
    # ----------------------------------------------------------   
    entity_replace = entity.replace("_temp", "")
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------
        counter        += 1 
        # ------------------------------------------------------
        name            = str(x[0].replace("-", " "))   
        idx             = str(x[1])
        # ------------------------------------------------------
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        # ------------------------------------------------------ 
        token_name      = name.split(" ") 
        # ------------------------------------------------------
        isinstanceX = 0
        # ------------------------------------------------------
        for tn in token_name: 
            if isinstance(tn, int) or tn.isdigit():
                # print(space + str(tn) + "_ YES", flush=True)
                isinstanceX = 1
            # else:
                # print(space + str(tn) + "_ NOT", flush=True)
        # ------------------------------------------------------
        if(isinstanceX == 1):
            word += " __INT__ "
        else:
            word += " __NOT__ "
            entitas_back_to_null(entity, idx, space)
        # ------------------------------------------------------
        word += " #" + name   
        # ------------------------------------------------------
        print(word, flush=True)    
        # ------------------------------------------------------
    # ---------------------------------------------------------- 