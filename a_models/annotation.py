# Import
import mysql.connector  
import time
 
def wildcard(entity, ner, labelX, entitas, update, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "wildcard()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    query = "Select " 
    query += " id "   
    query += " , name "    
    query += " , label "      
    query += " from " + entity      
    query += " where name like '%"+ner+"%' "   
    query += " and done is null "   
    # query += " limit 100 "   
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
    ner_split = ner.split(" ")
    print(space + "ner length: " + str(len(ner_split)))
    # ----------------------------------------------------------
    label_split = labelX.split(" ")
    print(space + "label length: " + str(len(label_split)))
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    for x in result:    
        # ------------------------------------------------------
        counter     += 1 
        count_dynamic = 0
        # ------------------------------------------------------
        idx         = str(x[0])   
        name        = str(x[1].strip())    
        label       = str(x[2])    
        # ------------------------------------------------------    
        name        = name.replace("'", "")
        # Bachelor's
        # ------------------------------------------------------
        old_label       = label.split(" ") 
        # ------------------------------------------------------
        token_name      = name.split(" ") 
        token_label     = ""
        # ------------------------------------------------------
        label_dynamic   = ""
        # ------------------------------------------------------
        counter_token = 0
        # ------------------------------------------------------
        # ------------------------------------------------------
        for tn in token_name:
            # if(tn != ner_split[count_dynamic]): 
            # print(tn + " __ " + ner_split[count_dynamic] + " __ " + str((tn == ner_split[count_dynamic])) + " __ " + str(count_dynamic) + " __ " + str((len(ner_split))) )
             
            ner_split_dynamic_lower = ner_split[count_dynamic].lower() 
            tn_lower = tn.lower() 


            if(tn_lower == ner_split_dynamic_lower):  
                token_label += label_split[count_dynamic] + " " 
                count_dynamic += 1 
            else:  
                if(count_dynamic == 1):      
                    count_dynamic = 0 

                if len(token_name) <= len(old_label) and old_label[counter_token] != "O":
                    token_label += old_label[counter_token] + " "
                else:
                    token_label += "O " 

            label_dynamic += str(count_dynamic) + " "
            counter_token += 1

            
            if(count_dynamic == len(ner_split)):
                count_dynamic = 0
        # ------------------------------------------------------


        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] "
        word += " " + name  
        print(word, flush=True)    
        # ------------------------------------------------------ 
        word = space + "________  "   
        word += "Old len: " + str(len(old_label)) + " __ New len: " + str(len(token_name))  
        if(len(old_label) != len(token_name)):
           word += " __ " + "WARNING!"
        print(word, flush=True)    
        # ------------------------------------------------------
        word = space + "________  "   
        word += label  
        print(word, flush=True)    
        # ------------------------------------------------------
        word = space + "________  "   
        word += token_label  
        print(word, flush=True)    
        # ------------------------------------------------------
        word = space + "________  "   
        word += label_dynamic  
        print(word, flush=True)    
        # ------------------------------------------------------
        word = space + "________  "   
        word += 'http://127.0.0.1:8001/Jobdescription/SetDone/' + str(idx) 
        print(word, flush=True)    
        # ------------------------------------------------------
        if(update == 'yes'):
            time.sleep(0.002)
            updated_data_BIO(entity, idx, token_label.strip(), str(len(token_name)), entitas, name, space + "______")
        # ------------------------------------------------------
        word = space + " "  
        print(word, flush=True)    
        # ------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------

    
def updated_data_BIO(entity, idx, label, space_length, entitas, name, space):  
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
    query_commit += " `name`='" + str(name) + "', "   
    query_commit += " `label`='" + str(label) + "', "   
    query_commit += " `space_length`='" + str(space_length) + "', "     
    query_commit += " `"+entitas+"` = 1 " 
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

    
def urutan(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "urutan()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_scraping_job_vacancy_indonesia_2023_07"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    query = "Select " 
    query += " id "   
    query += " , name "    
    query += " , label "      
    query += " from " + entity       
    query += " where done is null "   
    query += " order by name asc "   
    query += " limit 10 "   
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
    # ----------------------------------------------------------  
    for x in result:    
        # ------------------------------------------------------
        counter     += 1 
        count_dynamic = 0
        # ------------------------------------------------------
        idx         = str(x[0])   
        name        = str(x[1].strip())    
        label       = str(x[2])    
        # ------------------------------------------------------ 

        word =  name.replace("..", ".")  
        print(word, flush=True)    
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  
    print("", flush=True)     
    print("", flush=True)     
    # ----------------------------------------------------------  
    for x in result:    
        # ------------------------------------------------------
        counter     += 1 
        count_dynamic = 0
        # ------------------------------------------------------
        idx         = str(x[0])   
        name        = str(x[1].strip())    
        label       = str(x[2])    
        # ------------------------------------------------------ 

        word =  label  
        print(word, flush=True)    
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------   