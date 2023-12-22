# Import
import mysql.connector  
import time
from langdetect import detect, detect_langs
from googletrans import Translator
 
def last_id(entity, attr, space):  
    # ----------------------------------------------------------    
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "last_id()", flush=True)
    # ----------------------------------------------------------   
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------   
    query = "Select "
    query += " fk_id  "  
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
    if result_check is not None and len(result_check) > 0:
        last_id = result_check[0]
    else: 
        last_id = 0
    # ---------------------------------------------------------- 
    print(space + "Last ID:" + str(last_id), flush=True) 
    # ----------------------------------------------------------   
    return last_id
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
 
def last_id_desc(entity, space):  
    # ----------------------------------------------------------    
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "last_id_desc()", flush=True)
    # ----------------------------------------------------------   
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------   
    query = "Select "
    query += " id  "  
    query += " from " + entity     
    query += " order by id desc "   
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
    if result_check is not None and len(result_check) > 0:
        last_id = result_check[0]
    else: 
        last_id = 0
    # ---------------------------------------------------------- 
    print(space + "Last ID:" + str(last_id), flush=True) 
    # ----------------------------------------------------------   
    return last_id
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
   
def last_id_asc(entity, space):  
    # ----------------------------------------------------------    
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "last_id_asc()", flush=True)
    # ----------------------------------------------------------   
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------   
    query = "Select "
    query += " id  "  
    query += " from " + entity     
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
    if result_check is not None and len(result_check) > 0:
        last_id = result_check[0]  - 1
    else: 
        last_id = 0
    # ---------------------------------------------------------- 
    print(space + "Last ID:" + str(last_id), flush=True) 
    # ----------------------------------------------------------   
    return last_id
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  

      
def last_fk_id_desc(entity, space):  
    # ----------------------------------------------------------    
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "last_fk_id_desc()", flush=True)
    # ----------------------------------------------------------   
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database)
    # ----------------------------------------------------------   
    query = "Select "
    query += " fk_id  "  
    query += " from " + entity     
    query += " order by fk_id desc "   
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
    if result_check is not None and len(result_check) > 0:
        last_id = result_check[0]  - 1
    else: 
        last_id = 0
    # ---------------------------------------------------------- 
    print(space + "Last ID:" + str(last_id), flush=True) 
    # ----------------------------------------------------------   
    return last_id
    # ---------------------------------------------------------- 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
  
def replace_text(last_id, entity, attr, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "replace_text()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " id  "  
    query += " , name  "  
    query += " from " + entity     
    query += " where id > " + str(last_id)   
    query += " and " + attr + " is null "   
    query += " order by id asc "        
    query += " limit 10000"     
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
        idx         = str(x[0])  
        text        = str(x[1])    
        # ------------------------------------------------------  
        text = text.replace("u003C", "<")
        text = text.replace("u003E", ">")
        text = text.replace("u002F", "/")
        # ------------------------------------------------------
        text = text.replace(".</li>", " ")
        text = text.replace("</li>", ". ")
        # ------------------------------------------------------
        text = text.replace("</ul>", "")
        text = text.replace("<ul>", "")
        text = text.replace("<li>", "")
        # ------------------------------------------------------
        text = text.replace("</p>", "")
        text = text.replace("<p>", "")
        # ------------------------------------------------------
        text = text.replace("</ol>", "")
        text = text.replace("<ol>", "")
        # ------------------------------------------------------
        text = text.replace("</strong>", "")
        text = text.replace("<strong>", "")
        # ------------------------------------------------------
        text = text.replace("</u>", "")
        text = text.replace("<u>", "")
        # ------------------------------------------------------
        text = text.replace("</div>", "")
        text = text.replace("<div>", "")
        # ------------------------------------------------------
        text = text.replace("</b>", "")
        text = text.replace("<b>", "")
        # ------------------------------------------------------
        text = text.replace("<br />", "")
        text = text.replace("&amp;", "&")
        text = text.replace("\'", "'") 
        text = text.replace('"', "'") 
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + idx 
        word += " __ " + text  
        print(word, flush=True)    
        # ------------------------------------------------------
        time.sleep(0.002)
        # ------------------------------------------------------
        updated_data_with_attr(entity, idx, text, attr, space)
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
 
def updated_data_with_attr(entity, idx, val, attr, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "updated_data_with_attr()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------  
    query_commit += " `name`='" + str(val).replace("'", "\\'") + "', "  
    query_commit += " `" + attr + "`='1' "  
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
 
def updated_data_only_attr(entity, idx, attr, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "updated_data_only_attr()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------   
    query_commit += " `" + attr + "`='1' "  
    query_commit += " WHERE id = '" + str(idx) + "' "  
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

    
def updated_data_val(entity, idx, attr, val, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "updated_data_val()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------   
    query_commit += " `" + attr + "`='" + str(val) + "' "  
    query_commit += " WHERE id = '" + str(idx) + "' "  
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

def updated_data_dataset(entity, idx, attr, val, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "updated_data_dataset()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------   
    query_commit += " `" + attr + "`='" + str(val) + "' "  
    query_commit += " WHERE name = '" + str(idx) + "' "  
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

def updated_data_fk(entity, idx, val, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "updated_data_fk()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ---------------------------------------------------------- 
    entity_new = entity.replace('dataset_', "") 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity_new+"` SET "
    # ----------------------------------------------------------  
    query_commit += " `"+entity_new+"_id`='" + str(idx) + "' "  
    query_commit += " WHERE name = '" + str(val).replace("'", "\\'") + "' "  
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
 
def group_by_count_not_in_one(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "group_by_count_not_in_one()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------   
    entity_replace = entity.replace("_temp", "")
    # ---------------------------------------------------------- 
    query = "Select "
    query += " name  "  
    query += " , count(name)  "  
    query += " from " + entity_replace      
    query += " where " + entity_replace + "_id is null " 
    query += " group by name " 
    query += " having count(name) > 1 " 
    query += " ORDER BY `count(name)` DESC "    
    query += " limit 50 "       
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
        translator = Translator()
        # ------------------------------------------------------
        name            = str(x[0])  
        count_rows      = str(x[1])     
        detectx          = detect(name)
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + count_rows 
        word += " __ " + name   
        word += " __ " + detectx  

        if(detectx == "id"):
            translate_id    = translator.translate(name, src="id", dest="en")
        else:
            translate_id    = translator.translate(name, src="en", dest="id")
        word += " __ " + str(translate_id.text)   

        print(word, flush=True)    
        # ------------------------------------------------------
        time.sleep(0.002)
        # ------------------------------------------------------ 
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    
def backup_original_name(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "backup_original_name()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET `original_name`= `name`;" 
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
 
def dataset_to_fk(entity, lang, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "dataset_to_fk()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " id  "  
    query += " , nama  "  
    query += " , name  "  
    query += " from " + entity  
    if(lang == 'id'):
        query += " where sama_dengan is null "   
        query += " and nama is not null "   
        query += " and nama != '' "   
    elif(lang == 'en'):
        query += " where equal is null "    
        query += " and name is not null "    
        query += " and name != '' "   
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
        idx             = str(x[0])  
        nama            = str(x[1])    
        name            = str(x[2])     
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + idx 
        word += " __ " + nama   
        word += " __ " + name    
        print(word, flush=True)    
        # ------------------------------------------------------
        time.sleep(0.002)
        # ------------------------------------------------------ 
        if(nama != 'None'):
            updated_data_fk(entity, idx, nama, space)
            updated_data_only_attr(entity, idx, 'sama_dengan', space)
        if(name != 'None'): 
            updated_data_fk(entity, idx, name, space)
            updated_data_only_attr(entity, idx, 'equal', space)
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
 
def progress(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "progress()", flush=True)
    # ---------------------------------------------------------- 
    total = total_rows(entity, space)
    fk = fk_rows(entity, space)
    # ----------------------------------------------------------  
    progress = fk / total * 100
    # ---------------------------------------------------------- 
    print(space + "progress : " + str(progress), flush=True)  
    # ----------------------------------------------------------  
 
def total_rows(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "total_rows()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "Select "
    query_commit += " count(*) as counter "
    query_commit += " from `"+entity+"` " 
    # ----------------------------------------------------------   
    print(space + query_commit)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query_commit)
    # ----------------------------------------------------------   
    result_check = mycursor.fetchone()
    total_rows = result_check[0]
    # ----------------------------------------------------------   
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------       
    return total_rows
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  

    
def fk_rows(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "fk_rows()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "Select "
    query_commit += " count(*) as counter "
    query_commit += " From `"+entity+"` " 
    query_commit += " where "+entity+"_id is not null " 
    # ----------------------------------------------------------   
    print(space + query_commit)
    # ----------------------------------------------------------   
    mycursor = mydb.cursor()
    mycursor.execute(query_commit)
    # ----------------------------------------------------------   
    result_check = mycursor.fetchone()
    total_rows = result_check[0]
    # ----------------------------------------------------------   
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------       
    return total_rows
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
   
def testing_wildcard(entity, lang, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "testing_wildcard()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ---------------------------------------------------------- 
    if(lang == 'id'):
        query = "Select " 
        query += " nama "   
        query += " , id "      
        query += " from " + entity      
        query += " where sama_dengan = 1 "  
    if(lang == 'en'):
        query = "Select " 
        query += " name "   
        query += " , id "   
        query += " from " + entity      
        query += " where equal = 1 "  
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
        idx             = str(x[1])   
        # ------------------------------------------------------
        count_wildcard(entity, lang, idx, name, space)
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
 
def count_wildcard(entity, lang, idx, name, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "count_wildcard()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    entity_replace = entity.replace("dataset_", "")
    # ----------------------------------------------------------  
    query = "Select " 
    query += " * "       
    query += " from " + entity_replace      
    query += " where name like '%"+name+"%' "  
    query += " and " + entity_replace + "_id is null"
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
    if(lang == 'id'): 
        updated_data_val(entity, idx, "wildcard_id", total_rows, space)
    elif(lang == 'en'): 
        updated_data_val(entity, idx, "wildcard_en", total_rows, space)
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
 
def migration(last_id, entity, entity_new,  space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "migration()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " id  "  
    query += " , name  "  
    query += " from " + entity     
    query += " where id > " + str(last_id)   
    query += " order by id asc "        
    query += " limit 10"     
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
        idx         = str(x[0])  
        text        = str(x[1])    
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + idx 
        word += " __ " + text  
        print(word, flush=True)    
        # ------------------------------------------------------
        time.sleep(0.002)
        # ------------------------------------------------------
        insert(entity_new, "nama", idx, text, space)
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  

def migration_and_delete(last_id, entity, entity_new, new_val, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "migration_and_delete()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " fk_id  "  
    query += " , name  "  
    query += " from " + entity     
    query += " where id > " + str(last_id)   
    query += " order by id asc "        
    query += " limit 5000"     
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
        fk_idx         = str(x[0])  
        text        = str(x[1])    
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + fk_idx 
        word += " __ " + text  
        print(word, flush=True)    
        # ------------------------------------------------------  
        time.sleep(0.002)
        # ------------------------------------------------------ 
        updated_data_id_from_dataset(entity_new, fk_idx, text, new_val, space) 
        # ------------------------------------------------------  
        time.sleep(0.002)
        # ------------------------------------------------------  
        delete_fk(entity, fk_idx, space)
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ---------------------------------------------------------- 
    
    
def insert_label_bio(entity, attr, idx, val, label, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "insert_label_bio()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "INSERT INTO `"+entity+"` ("
    # ----------------------------------------------------------  
    query_commit += " `fk_id`, "  
    query_commit += " `"+str(attr)+"`, "  
    query_commit += " `label` "  
    query_commit += " ) VALUES ( "  
    query_commit += " '"+str(idx)+"', "  
    query_commit += " '"+str(val).replace("'", "\\'")+"', "  
    query_commit += " '"+str(label)+"' "  
    query_commit += " ) "   
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

def insert(entity, attr, idx, val, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "insert()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "INSERT INTO `"+entity+"` ("
    # ----------------------------------------------------------  
    query_commit += " `fk_id`, "  
    query_commit += " `"+str(attr)+"` "  
    query_commit += " ) VALUES ( "  
    query_commit += " '"+str(idx)+"', "  
    query_commit += " '"+str(val).replace("'", "\\'")+"' "  
    query_commit += " ) "   
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

    
def insert_wo_fk(entity, attr, val, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "insert_wo_fk()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "INSERT INTO `"+entity+"` ("
    # ----------------------------------------------------------   
    query_commit += " `"+str(attr)+"` "  
    query_commit += " ) VALUES ( "   
    query_commit += " '"+str(val).replace("'", "\\'")+"' "  
    query_commit += " ) "   
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
 
def distinct_to_dataset(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "distinct_to_dataset()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------   
    entity_replace = entity.replace("_temp", "")
    # ---------------------------------------------------------- 
    query = "Select "
    query += " name  "   
    query += " from " + entity_replace   
    query += " where name is not null and name != 'null' "   
    query += " group by name "  
    query += " ORDER BY name ASC "     
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
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name    
        # ------------------------------------------------------
        time.sleep(0.002)
        # ------------------------------------------------------
        print(word, flush=True)    
        # ------------------------------------------------------
        insert_wo_fk("dataset_" + entity, "nama", name, space)
        # ------------------------------------------------------
        last_idx = last_id_desc("dataset_" + entity, space)
        # ------------------------------------------------------
        updated_data_dataset(entity, name, "name", last_idx, space) 
        # ------------------------------------------------------
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  

def distinct_to_datasetX(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "distinct_to_datasetX()", flush=True)
    # ----------------------------------------------------------  
    if(entity == "employment_types"):
        new_entity = "jobrequirement_employmenttypes"  
    elif(entity == "jobrequirement_industryvalues"):
        new_entity = "jobrequirement_industryvalues"  
        entity = "industry_values"   
    else:
        new_entity = entity
    # ----------------------------------------------------------   
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , count(*) as counter  "   
    query += " from " + new_entity   
    query += " where name is not null and name != 'null' and name != '' "   
    query += " group by name "  
    query += " ORDER BY count(*) desc, name ASC "     
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
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name    
        # ------------------------------------------------------
        time.sleep(0.002)
        # ------------------------------------------------------
        print(word, flush=True)     
        # ------------------------------------------------------
        insert_wo_fk("dataset_" + entity, "nama", name, space)
        # ------------------------------------------------------
        last_idx = last_id_desc("dataset_" + entity, space)
        # ------------------------------------------------------ 
        if(entity == "industry_values"):
            entity = "jobrequirement_industryvalues"   
        # ------------------------------------------------------ 
        updated_data_dataset(entity, name, "name", last_idx, space) 
        # ------------------------------------------------------
        print("", flush=True)
        print("", flush=True)
        # ------------------------------------------------------
        if(entity == "jobrequirement_industryvalues"):
            entity = "industry_values"   
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ---------------------------------------------------------- 
     
def delete_zonk(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "delete_zonk()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "DELETE FROM `"+entity+"` where name is null or name = 'null'  or name = ''"  
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
    
def delete_fk(entity, fkid, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "delete_fk()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "DELETE FROM `"+entity+"` where fk_id = '"+str(fkid)+"'"  
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

def updated_data_id_from_dataset(entity, fk_idx, val, attr, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "updated_data_id_from_dataset()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------  
    query_commit += " `"+attr+"`='" + str(val) + "' "   
    query_commit += " WHERE fk_id = '" + str(fk_idx) + "' "  
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

def update_and_delete(entity_new, entity, last_idx, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    # print(space + "update_and_delete()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " , fk_id  "  
    query += " from " + entity      
    query += " where id > " + str(last_idx)  
    query += " limit 5000 "       
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
        idy             = str(x[1])     
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + idy  
        word += " __ " + name  
        # ------------------------------------------------------
        print(word, flush=True)    
        # ------------------------------------------------------
        time.sleep(0.005)
        # ------------------------------------------------------
        updated_data_id_from_dataset(entity_new, idy, name, entity, space)
        # ------------------------------------------------------  
        time.sleep(0.005)
        # ------------------------------------------------------  
        delete_fk(entity, idy, space)
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   

    
def update_clean_and_replace(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    # print(space + "update_clean_and_replace()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " old  "   
    query += " , new  "  
    query += " from replace_strings "   
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
        old_value            = str(x[0])     
        new_value             = str(x[1])     
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + old_value  
        word += " __ " + new_value  
        # ------------------------------------------------------
        print(word, flush=True)    
        # ------------------------------------------------------
        updated_and_clean(entity, old_value, new_value, space)
        # ------------------------------------------------------


def updated_and_clean(entity, old_value, new_value, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "updated_and_clean()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------  
    query_commit += " `name`= REPLACE(name, '"+old_value+"', '"+new_value+"') "    
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
 
def word_cloud(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "word_cloud()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " fk_id  "  
    query += " , name  "  
    query += " from " + entity 
    query += " limit 1 "       
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
        fk              = str(x[0])  
        name            = str(x[1])      
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + fk 
        word += " __ " + name    
        # ------------------------------------------------------
        # ------------------------------------------------------
        print(word, flush=True)    
    # ----------------------------------------------------------
    

def insert_token(entity, name, counter, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "insert()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "INSERT INTO `"+entity+"` ("
    # ----------------------------------------------------------   
    query_commit += " `name`, "  
    query_commit += " `counter` "  
    query_commit += " ) VALUES ( "  
    query_commit += " '"+str(name).replace("'", "\\'")+"', "  
    query_commit += " '"+str(counter)+"' "  
    query_commit += " ) "   
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
 
def migration_as_fk(entity, entity_new, attr, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "migration_as_fk()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "   
    query += " from " + entity    
    query += " group by name "  
    query += " ORDER BY name ASC "     
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
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name  
        # ------------------------------------------------------   
        print(word, flush=True)    
        # ------------------------------------------------------   
        updated_data_id_from_dataset_using_IN(entity_new, entity, name, attr, space)
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   

    
def updated_data_id_from_dataset_using_IN(entity_new, entity, val, attr, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "updated_data_id_from_dataset_using_IN()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity_new+"` SET "
    # ----------------------------------------------------------  
    query_commit += " `"+attr+"`='" + str(val) + "' "   
    query_commit += " WHERE fk_id IN (SELECT fk_id FROM `"+entity+"` WHERE `name` LIKE '" + str(val) + "')  "  
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
 
def define_tidak_terspesifikasi(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "define_tidak_terspesifikasi()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------  
    query_commit += " `name` = 'Tidak Terspesifikasi' "   
    query_commit += " WHERE (name = '' or name is null)  "  
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

 
def extract_entity(entity, entity_extract, entity_destination, attr, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "extract_entity()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select " 
    query += " id  "  
    query += " , nama  "  
    query += " from dataset_" + entity  
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
        idx              = str(x[0])      
        name            = str(x[1])      
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + name  
        # ------------------------------------------------------ 
        print(word, flush=True)    
        # ------------------------------------------------------ 
        select_entity(entity_extract, entity_destination, idx, name, attr, space)
        # ------------------------------------------------------ 
        updated_and_clean(entity_extract, name, "", space)
    # ----------------------------------------------------------

    
def select_entity(entity, entity_destination, idx, name, attr, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "select_entity()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select " 
    query += " fk_id  " 
    query += " , name  "  
    query += " from " + entity  
    query += " WHERE `name` LIKE '%"+name+"%' "   
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
        fk_id           = str(x[0])      
        name            = str(x[1])      
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + fk_id  
        word += " __ " + name  
        # ------------------------------------------------------ 
        print(word, flush=True)    
        # ------------------------------------------------------ 
        updated_data_id_from_dataset(entity_destination, fk_id, idx, attr, space)
    # ----------------------------------------------------------
 
def usia(entity, val, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "usia()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select " 
    query += " fk_id  " 
    query += " , name  "  
    query += " from " + entity  
    query += " WHERE `name` LIKE '% "+val+" %' "   
    # query += " limit 500  "   
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
        fk_id           = str(x[0])      
        name            = str(x[1].lower())      
        # ------------------------------------------------------ 
        string_baru     = name.split(val)          
        # ------------------------------------------------------ 
        string_baru2     = string_baru[1].split("tahun")
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + fk_id  
        word += " _|_ " + str(len(string_baru))
        word += " _|_ " + string_baru2[0]  
        # ------------------------------------------------------
        if "maksimal" in string_baru2[0]: 
            word += " _|_ Valid"   
        elif "max" in string_baru2[0]: 
            word += " _|_ Valid"   
        elif "maks." in string_baru2[0]: 
            word += " _|_ Valid"    
        elif "maksimum" in string_baru2[0]: 
            word += " _|_ Valid"    
        elif "maks" in string_baru2[0]: 
            word += " _|_ Valid"   

            
        # ------------------------------------------------------ 
        print(word, flush=True)    
        # ------------------------------------------------------ 
  
def token_jobdesc(entity, fk_id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "token_jobdesc()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select " 
    query += " fk_id  " 
    query += " , name  "  
    query += " from " + entity  
    query += " where fk_id > "+str(fk_id)+" "   
    query += " and fk_id <= 5000 "
    # query += " limit 1500 "   
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
    counter_100 = 0 
    # ----------------------------------------------------------   
    for x in result:    
        # ------------------------------------------------------ 
        fk_id           = str(x[0])      
        name            = str(x[1])      
        # ------------------------------------------------------
        token_name      = name.split(".") 
        # ------------------------------------------------------
        for tn in token_name:
            # --------------------------------------------------
            time.sleep(0.005)
            # --------------------------------------------------
            tn_strip = tn.strip()
            # --------------------------------------------------
            if(tn_strip != ''):
                # ----------------------------------------------
                counter         += 1 
                # ----------------------------------------------
                jumlah_spasi    = tn_strip.count(" ") 
                # ----------------------------------------------
                label_o         = "O " * (jumlah_spasi + 1)
                # ----------------------------------------------
                insert_label_bio(entity + "_dataset", "name", fk_id, tn_strip, label_o, space)
                # ---------------------------------------------- 
                if(counter == 1000):
                    # ------------------------------------------ 
                    word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
                    word += " #" + str(1000 * counter_100)  
                    # ------------------------------------------ 
                    word += " __ " + str(jumlah_spasi)   
                    word += " __ " + label_o.strip()   
                    word += " __ " + tn_strip   
                    # ------------------------------------------ 
                    print(word, flush=True)    
                    # ------------------------------------------ 
                    counter     = 0
                    # ------------------------------------------ 
                    counter_100 += 1
                # ----------------------------------------------
            # --------------------------------------------------
        # ------------------------------------------------------ 

        
def pelabelan_entitas(entity, entitas, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "pelabelan_entitas()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` "
    # ----------------------------------------------------------  
    query_commit += "SET `entitas` = CONCAT('"+entitas+"', ' ', `entitas`) "
    query_commit += "WHERE `name` LIKE '%"+entitas+"%'; "  
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
 
def entitas_back_to_null(entity, id, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "entitas_back_to_null()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` "
    # ----------------------------------------------------------  
    query_commit += "SET `entitas` = '' "
    query_commit += "WHERE `id` = '"+str(id)+"'; "  
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

    
def pelabelan(entity, id, label, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "pelabelan()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------  
    query_commit += "`label` = '"+label+"', "
    query_commit += "`done` = 1 "
    query_commit += "WHERE `id` = '"+str(id)+"'; "  
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

def delete_duplication(entity, entitas, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "delete_duplication()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " name  "  
    query += " , count(*)  " 
    query += " from " + entity    
    query += " where entitas = '" + entitas + "'"     
    query += " group by name "     
    query += " having count(*) > 1 "    
    query += " order by count(*) desc "   
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
        name         = str(x[0])  
        counter        = str(x[1])    
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + counter 
        word += " __ " + name  
        print(word, flush=True)    
        # ------------------------------------------------------

        
def readjust_label_and_length(entity, entitas, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "readjust_label_and_length()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------    
    query = "Select "
    query += " id  "  
    query += " , name  " 
    query += " from " + entity    
    query += " where entitas like '%" + entitas + "%'"     
    query += " and done is null "   
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
        idx         = str(x[0])  
        name        = str(x[1])    
        # ------------------------------------------------------
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] " 
        word += " #" + str(counter) 
        word += " __ " + name   
        # ------------------------------------------------------
        jumlah_spasi    = name.count(" ") 
        # ------------------------------------------------------
        label_o         = ("O " * (jumlah_spasi + 1)).strip()
        # ------------------------------------------------------
        updated_data_BIO(entity, idx, label_o, space)
        # ------------------------------------------------------
        print(word, flush=True)    
        # ------------------------------------------------------
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 
    # ---------------------------------------------------------- 

    
def updated_data_BIO(entity, idx, label, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "updated_data_val()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------   
    query_commit += " `label`='" + str(label) + "', "  
    query_commit += " `length`= CHAR_LENGTH(`name`) "  
    # ----------------------------------------------------------   
    query_commit += " WHERE id = '" + str(idx) + "' "  
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