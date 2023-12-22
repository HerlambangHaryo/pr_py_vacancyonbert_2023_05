# Import
import mysql.connector  
import time
 
def dynamic_wildcard(printX, updateX, space):   
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
        dynamic(nama, label, printX, updateX, space)
        # ------------------------------------------------------   
        time.sleep(0.05)
        # ------------------------------------------------------   
        updated_anotasi(idx, space)
        # ------------------------------------------------------   
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------


def dynamic(entity, label, printX, updateX, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "dynamic()", flush=True)
    # ----------------------------------------------------------  
    split_entity        = entity.strip().split(" ")
    len_split_entity    = len(split_entity)
    # ----------------------------------------------------------  
    split_label        = label.strip().split(" ")
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------   
    print(space + "entity: " + str(entity), flush=True)
    print(space + "split length: " + str(len_split_entity), flush=True)
    # ----------------------------------------------------------   
    token_entity_0      = split_entity[0] 
    token_label_0       = split_label[0] 
    # ---------------------------------------------------------- 
    named_entity        = token_label_0.split("-")
    # ----------------------------------------------------------
    if(len_split_entity == 1):
        # ------------------------------------------------------ 
        updated_data_single_begining(token_entity_0, token_label_0, space)
        # ------------------------------------------------------   
    else:
        # ------------------------------------------------------ 
        word_0(token_entity_0, named_entity[1], split_entity, len_split_entity, label, printX, updateX, space)
        # ------------------------------------------------------  
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
 
def word_0(token_entity_0, named_entity, split_entity, len_split_entityX, labelX, printX, updateX, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "word_0()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------   
    query = "Select " 
    query += " id "   
    query += " , name "          
    query += " from datasets "      
    query += ' where name like "'+str(token_entity_0.replace("'", "\\'"))+'" '    
    query += ' and "'+str(named_entity.lower().replace("'", "\\'"))+'"  != "B" '    
    query += " order by id asc "    
    # query += " limit 10 "    
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
    round_10_perc = round(total_rows / 10)
    # ---------------------------------------------------------- 
    if(round_10_perc == 0):
        round_10_perc = 1
    # ---------------------------------------------------------- 
    print(space + "round_10_perc Row(s) : " + str(round_10_perc), flush=True) 
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter         = 0 
    # ----------------------------------------------------------
    new_UPDATE_ID   = ""
    # ----------------------------------------------------------
    for x in result:    
        # ------------------------------------------------------  
        time.sleep(0.05)
        # ------------------------------------------------------  
        counter             += 1
        # ------------------------------------------------------ 
        counter_split       = 0
        # ------------------------------------------------------ 
        idx         = str(x[0])   
        nama        = str(x[1])       
        # ------------------------------------------------------   
        word = space + "__[" + str(counter) + "/" +str(total_rows) + "] "
        word += " #" + idx  
        word += " __ " + nama    
        word += " __ " + str(counter_split)    
        # ------------------------------------------------------  
        if(counter % round_10_perc == 0 or counter == 1 or printX == "yes"):
            print(word, flush=True)    
        # ------------------------------------------------------  
        counter_split      += 1  
        # ------------------------------------------------------  
        new_token_entity    = split_entity[counter_split]
        # ------------------------------------------------------   
        new_UPDATE_ID       = idx + " "
        # ------------------------------------------------------   
        word_x(idx, new_token_entity, new_UPDATE_ID, counter_split, len_split_entityX, labelX, split_entity, counter, round_10_perc, printX, updateX, space)
        # ------------------------------------------------------   
        if(counter % round_10_perc == 0 or counter == 1 or printX == "yes"):
            word = space 
            print(word, flush=True)    
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
 
def word_x(PARAM_id, new_token_entity, new_UPDATE_ID, counter_splitX, len_split_entityX, labelX, split_entityX, counterX, round_10_percX, printX, updateX, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    # print(space + "word_x()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------   
    query = "Select " 
    query += " id "   
    query += " , name "          
    query += " from datasets "      
    query += " where id > '"+str(PARAM_id)+"' "    
    query += " order by id asc "    
    query += " limit 1 "    
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
    # ---------------------------------------------------------- 
    # print(space + "NTE : " + str(new_token_entity), flush=True) 
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ---------------------------------------------------------- 
    counter         = 0 
    # ----------------------------------------------------------
    for x in result:    
        # ------------------------------------------------------  
        time.sleep(0.05)
        # ------------------------------------------------------  
        counter     += 1
        # ------------------------------------------------------ 
        idx         = str(x[0])   
        nama        = x[1]    
        # ------------------------------------------------------   
        word        = space + "__[" + str(counter) + "/" +str(total_rows) + "] "
        word        += " #" + idx   
        word        += " __ " + str(nama) 
        word        += " __ nte: " + new_token_entity 
        word        += " __ csX: " + str(counter_splitX) 
        word        += " __ lsX: " + str(len_split_entityX) 
        # ------------------------------------------------------      
        if(counterX % round_10_percX == 0 or counterX == 1 or printX == "yes"):
            print(word, flush=True)     
        # ------------------------------------------------------     
        good_to_go = 0
        # ------------------------------------------------------     
        if new_token_entity == "int":   
            if nama.isdigit(): 
                good_to_go = 1  
        elif(nama.lower() == new_token_entity.lower()): 
            good_to_go = 1  
        # else:
        #     print(space + str(type(nama)), flush=True)
        # ------------------------------------------------------   
        if(good_to_go == 1):
            # --------------------------------------------------   
            new_UPDATE_ID += idx + " "
            # -------------------------------------------------- 
            # print(space + "OKE __ " + new_UPDATE_ID, flush=True)    
            # -------------------------------------------------- 
            # print(word, flush=True)     
            # -------------------------------------------------- 
            if(len_split_entityX == counter_splitX + 1):
                # ---------------------------------------------- 
                # print(space + "counter __ " + str(counter_splitX) + " __ " + str(len_split_entityX), flush=True)    
                # ----------------------------------------------  
                split_ID(new_UPDATE_ID, labelX, counterX, round_10_percX, printX, updateX, space)
                # ----------------------------------------------  
            else:
                # ----------------------------------------------  
                counter_splitX      += 1  
                # ----------------------------------------------  
                new_token_entity    = split_entityX[counter_splitX] 
                # ---------------------------------------------- 
                word_x(idx, new_token_entity, new_UPDATE_ID, counter_splitX, len_split_entityX, labelX, split_entityX, counterX, round_10_percX, printX, updateX, space)
        # ------------------------------------------------------  
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
 
def split_ID(split_IDX, labelX, counterX, round_10_percX, printX, updateX, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------    
    if(counterX % round_10_percX == 0 or counterX == 1 or printX == "yes"): 
        print(space + "split_ID() " + split_IDX + " __ " + labelX, flush=True) 
    # ----------------------------------------------------------  
    split_ID            = split_IDX.strip().split(" ")
    split_labelX        = labelX.strip().split(" ") 
    # ----------------------------------------------------------   
    counter             = 0
    # ----------------------------------------------------------   
    for label in split_labelX:
        # ------------------------------------------------------ 
        if(label != "O"):
            # ------------------------------------------------------ 
            idx       = split_ID[counter] 
            # ------------------------------------------------------ 
            updated_data_dynamic(idx, label, counterX, round_10_percX, printX, updateX, space)
            # ------------------------------------------------------ 
        # ------------------------------------------------------ 
        counter         += 1
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------

def updated_data_dynamic(idxX, labelX, counterX, round_10_percX, printX, updateX, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    time.sleep(0.5)
    # ----------------------------------------------------------   
    if(counterX % round_10_percX == 0 or counterX == 1 or printX == "yes"): 
        print(space + "updated_data_dynamic() " + str(idxX) + " __ " + str(labelX), flush=True)
    # ----------------------------------------------------------   
    split_labelX        = labelX.strip().split("-") 
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `datasets` SET "
    # ----------------------------------------------------------   
    query_commit += " `" + str(split_labelX[1].lower()) + "` = '" + str(split_labelX[0]) + "' "     
    # ----------------------------------------------------------   
    query_commit += " WHERE id = " + str(idxX) + " "  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    mycursor = mydb.cursor()
    # ----------------------------------------------------------  
    if(counterX % round_10_percX == 0 or counterX == 1 or printX == "yes"): 
        # ------------------------------------------------------  
        if(updateX == "yes"):
            # --------------------------------------------------  
            print(space + query_commit, flush=True)
            # --------------------------------------------------  
            mycursor.execute(query_commit)
            mydb.commit()     
            # -------------------------------------------------- 
        # ------------------------------------------------------ 
    # ----------------------------------------------------------  
    mycursor.close()
    mydb.close()
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    # ----------------------------------------------------------

def updated_data_single_begining(token_entity, token_label, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ----------------------------------------------------------  
    print(space + "updated_data_single_begining()", flush=True)
    # ----------------------------------------------------------   
    split_labelX        = token_label.strip().split("-") 
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database="pr_laravel_8_vacancyonbert_2023_05"
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    query_commit = "UPDATE `datasets` SET "
    # ----------------------------------------------------------   
    query_commit += " `" + str(split_labelX[1].lower()) + "` = '" + str(split_labelX[0]) + "' "     
    # ----------------------------------------------------------    
    query_commit += ' where name like "'+str(token_entity.replace("'", "\\'"))+'" '  
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