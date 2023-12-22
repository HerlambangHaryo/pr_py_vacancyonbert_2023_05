# Import
import mysql.connector  
import time
 
def dynamic_wildcard(entity, update, printx, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "dynamic_wildcard()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------   
    query = "Select " 
    query += " id "   
    query += " , nama "    
    query += " , label "        
    query += " from anotasis "      
    query += " where done is null "   
    query += " and label is not null "    
    # query += " and id = 55 "    
    # query += " limit 1 "  
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
        counter         += 1 
        count_dynamic   = 0
        # ------------------------------------------------------
        idx         = str(x[0])   
        nama        = str(x[1].strip())     
        label       = str(x[2].strip())     
        # ------------------------------------------------------  
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] "
        word += " #" + idx  
        word += " __ " + nama   
        word += " __ " + label   
        print(word, flush=True)    
        # ------------------------------------------------------   
        wildcard(entity, nama, label, idx, update, printx, space)
        # ------------------------------------------------------   
        time.sleep(0.05)
        # updated_anotasi(idx, space)
        # ------------------------------------------------------   
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
 
def wildcard(entity, ner, labelX, anotasi_idx, update, printx, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "wildcard()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------   
    query = "Select " 
    query += " id "   
    query += " , dataset "    
    query += " , label "      
    query += " from " + entity      
    query += ' where dataset like "%'+ner+'%" '   
    query += " and done is null "   
    # query += " limit 1 "  
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
    time.sleep(0.05)
    updated_counter(anotasi_idx, total_rows, space)
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
        dataset     = str(x[1].strip())    
        label       = str(x[2])    
        # ------------------------------------------------------    
        dataset        = dataset.replace("'", "") 
        # ------------------------------------------------------
        old_label       = label.split(" ") 
        # ------------------------------------------------------
        token_dataset      = dataset.split(" ") 
        token_label     = ""
        # ------------------------------------------------------
        label_dynamic   = ""
        # ------------------------------------------------------
        counter_token = 0
        # ------------------------------------------------------
        # ------------------------------------------------------
        for tn in token_dataset:
            # --------------------------------------------------
            # if(tn != ner_split[count_dynamic]): 
            # print(tn + " __ " + ner_split[count_dynamic] + " __ " + str((tn == ner_split[count_dynamic])) + " __ " + str(count_dynamic) + " __ " + str((len(ner_split))) )
            # --------------------------------------------------
            ner_split_dynamic_lower = ner_split[count_dynamic].lower() 
            tn_lower = tn.lower() 
            # --------------------------------------------------
            if(tn_lower == ner_split_dynamic_lower):  
                token_label += label_split[count_dynamic] + " " 
                count_dynamic += 1 
            else:  
                if(count_dynamic == 1):      
                    count_dynamic = 0 

                if len(token_dataset) <= len(old_label) and old_label[counter_token] != "O":
                    token_label += old_label[counter_token] + " "
                else:
                    token_label += "O " 
            # --------------------------------------------------
            label_dynamic += str(count_dynamic) + " "
            counter_token += 1
            # --------------------------------------------------
            if(count_dynamic == len(ner_split)):
                count_dynamic = 0
            # --------------------------------------------------
        # ------------------------------------------------------
        # ------------------------------------------------------ 
        if(printx == "yes"):
            # --------------------------------------------------
            word = space + "__[" + str(counter) + "/" +str(total_rows) + "] "
            word += " #" + idx  
            word += " " + dataset  
            print(word, flush=True)    
            # --------------------------------------------------
            word = space + "________  "   
            word += "Old len: " + str(len(old_label)) + " __ New len: " + str(len(token_dataset)) 
            # -------------------------------------------------- 
            if(len(old_label) != len(token_dataset)):
                word += " __ " + "WARNING!"
                print(word, flush=True)    
            # --------------------------------------------------
            word = space + "________  "   
            word += label  
            print(word, flush=True)    
            # --------------------------------------------------
            word = space + "________  "   
            word += token_label  
            print(word, flush=True)    
            # --------------------------------------------------
            word = space + "________  "   
            word += label_dynamic  
            print(word, flush=True)     
        # ------------------------------------------------------
        if(update == 'yes'):
            time.sleep(0.05)
            updated_data_BIO(entity, idx, token_label.strip(), str(len(token_dataset)), dataset, space + "______")
        # ------------------------------------------------------
        # word = space + " "  
        # print(word, flush=True)    
        # ------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------

def updated_data_BIO(entity, idx, label, space_length, dataset, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "updated_data_val()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `"+entity+"` SET "
    # ----------------------------------------------------------   
    query_commit += " `dataset`='" + str(dataset) + "', "   
    query_commit += " `label`='" + str(label) + "', "   
    query_commit += " `space_length`='" + str(space_length) + "' "      
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

def updated_anotasi(idx, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "updated_anotasi()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `anotasis` SET "
    # ----------------------------------------------------------   
    query_commit += " `done` = 1 "    
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
  
def updated_counter(idx, counter, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    # print(space + "updated_counter()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `anotasis` SET "
    # ----------------------------------------------------------   
    query_commit += " `counter` = " + str(counter) + " "    
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
    #   
def urutan(entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "urutan()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    query = "Select " 
    query += " id "   
    query += " , dataset "    
    query += " , label "      
    query += " from " + entity       
    query += " where done is null "   
    query += " order by dataset asc "   
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
        dataset        = str(x[1].strip())    
        label       = str(x[2])    
        # ------------------------------------------------------ 

        word =  dataset.replace("..", ".")  
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
        dataset        = str(x[1].strip())    
        label       = str(x[2])    
        # ------------------------------------------------------ 

        word =  label  
        print(word, flush=True)    
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------   