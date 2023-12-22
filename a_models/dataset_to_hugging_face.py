# Import
import mysql.connector  
import time
import json
 
def set_to_dataset(databaseX, entity, named_entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "set_to_dataset()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database=databaseX
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    query = "Select " 
    query += " id "   
    query += " , name "    
    query += " , " + named_entity      
    query += " from " + entity       
    # query += " limit 5 "   
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
    label_map = {}
    # ----------------------------------------------------------  
    for x in result:    
        # ------------------------------------------------------
        idx         = str(x[0])     
        named       = str(x[2])    
        # ------------------------------------------------------     
        data = named+ ":" + str(counter)
        # ------------------------------------------------------
        counter     += 1  
    # ----------------------------------------------------------   
    # ----------------------------------------------------------  
    with open('label_map_'+entity+'-'+named_entity+'.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)   
    # ----------------------------------------------------------   
    print("Data telah disimpan dalam label_map "+entity+"-"+named_entity+".json")
    # ----------------------------------------------------------  

    
def set_to_all_dataset(databaseX, entity, space):  
    # ----------------------------------------------------------   
    space += "__"
    # ---------------------------------------------------------- 
    print(space + "set_to_all_dataset()", flush=True)
    # ----------------------------------------------------------  
    host="localhost"
    user="root" 
    database=databaseX
    mydb = mysql.connector.connect(host=host,user=user,password="",database=database) 
    # ----------------------------------------------------------  
    # ----------------------------------------------------------  
    query = "Select " 
    query += " id "   
    query += " , name "    
    query += " , perusahaan "    
    query += " , pekerjaan_industri "    
    query += " , jabatan "    
    query += " , keterampilan_teknis "    
    query += " , penempatan_negara "    
    query += " , penempatan_wilayah "    
    query += " , penempatan_pulau "     
    query += " , penempatan_provinsi "    
    query += " , penempatan_kota "    
    query += " , penempatan_kecamatan "    
    query += " , penempatan_kelurahan "    
    query += " , penempatan_kawasan "     
    query += " , penempatan_gedung "     
    query += " , status_pekerjaan "     
    query += " , kategori_pekerjaan "     
    query += " , pengalaman_minimal "     
    query += " , keterangan_pekerjaan "     
    query += " , cara_kerja "     
    query += " from " + entity       
    # query += " limit 5 "   
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
    data = {
            "data": [
                {
                    "tokens": []
                }
            ]
        }
    # ----------------------------------------------------------  
    for x in result:    
        # ------------------------------------------------------
        controll_duplicate = 0
        # ------------------------------------------------------
        idx                     = str(x[0])     
        name                    = str(x[1])     

        perusahaan              = str(x[2])     
        pekerjaan_industri      = str(x[3])     
        jabatan                 = str(x[4])     
        keterampilan_teknis     = str(x[5])     
        penempatan_negara       = str(x[6])     
        penempatan_wilayah      = str(x[7])     
        penempatan_pulau        = str(x[8])      
        penempatan_provinsi     = str(x[9])     
        penempatan_kota         = str(x[10])     
        penempatan_kecamatan    = str(x[11])     
        penempatan_kelurahan    = str(x[12])     
        penempatan_kawasan      = str(x[13])      
        penempatan_gedung       = str(x[14])      
        status_pekerjaan        = str(x[15])      
        kategori_pekerjaan      = str(x[16])      
        pengalaman_minimal      = str(x[17])      
        keterangan_pekerjaan    = str(x[18])      
        cara_kerja              = str(x[19])      
        # ------------------------------------------------------      
        
        if(perusahaan != "O"):     
            controll_duplicate += 1
            token = {
                "text": name,
                "label": perusahaan + "-Perusahaan"
            }

        if(pekerjaan_industri != "O"):    
            controll_duplicate += 1 
            token = {
                "text": name,
                "label": pekerjaan_industri + "-Pekerjaan_industri"
            }

        if(jabatan != "O"):     
            controll_duplicate += 1
            token = {
                "text": name,
                "label": jabatan + "-Jabatan"
            }

        if(keterampilan_teknis != "O"):     
            controll_duplicate += 1
            token = {
                "text": name,
                "label": keterampilan_teknis + "-Keterampilan_teknis"
            }
 
        if(penempatan_gedung != "O"):   
            controll_duplicate += 1   
            token = {
                "text": name,
                "label": penempatan_gedung + "-Penempatan_gedung"
            }
        elif(penempatan_kawasan != "O"):     
            controll_duplicate += 1 
            token = {
                "text": name,
                "label": penempatan_kawasan + "-Penempatan_kawasan"
            }
        elif(penempatan_kelurahan != "O"):    
            controll_duplicate += 1 
            token = {
                "text": name,
                "label": penempatan_kelurahan + "-Penempatan_kelurahan"
            }
        elif(penempatan_kecamatan != "O"):   
            controll_duplicate += 1  
            token = {
                "text": name,
                "label": penempatan_kecamatan + "-Penempatan_kecamatan"
            }
        elif(penempatan_kota != "O"):     
            controll_duplicate += 1
            token = {
                "text": name,
                "label": penempatan_kota + "-Penempatan_kota"
            }
        elif(penempatan_provinsi != "O"):     
            controll_duplicate += 1
            token = {
                "text": name,
                "label": penempatan_provinsi + "-Penempatan_provinsi"
            }
        elif(penempatan_pulau != "O"):     
            controll_duplicate += 1 
            token = {
                "text": name,
                "label": penempatan_pulau + "-Penempatan_pulau"
            }
        elif(penempatan_wilayah != "O"):     
            controll_duplicate += 1
            token = {
                "text": name,
                "label": penempatan_wilayah + "-Penempatan_wilayah"
            }
        elif(penempatan_negara != "O"):     
            controll_duplicate += 1
            token = {
                "text": name,
                "label": penempatan_negara + "-Penempatan_negara"
            }





        if(status_pekerjaan != "O"):    
            controll_duplicate += 1  
            token = {
                "text": name,
                "label": status_pekerjaan + "-Status_pekerjaan"
            }

        if(kategori_pekerjaan != "O"):     
            controll_duplicate += 1 
            token = {
                "text": name,
                "label": kategori_pekerjaan + "-Kategori_pekerjaan"
            }

        if(pengalaman_minimal != "O"):      
            controll_duplicate += 1
            token = {
                "text": name,
                "label": pengalaman_minimal + "-Pengalaman_minimal"
            }

        if(keterangan_pekerjaan != "O"):      
            controll_duplicate += 1
            token = {
                "text": name,
                "label": keterangan_pekerjaan + "-Keterangan_pekerjaan"
            }

        if(cara_kerja != "O"):  
            controll_duplicate += 1
            token = {
                "text": name,
                "label": cara_kerja + "-Cara_kerja"
            }


        if(controll_duplicate > 1):
            print( "controll_duplicate " + str(idx) )
            break
        elif(controll_duplicate == 0): 
            #  "label": "B-cara_kerja"
            token = {
                "text": name,
                "label": "O"
            }
        # ------------------------------------------------------ 
        data["data"][0]["tokens"].append(token) 
        # ------------------------------------------------------
        counter     += 1  
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    with open(entity+'.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)
    # ----------------------------------------------------------   
    print("Data telah disimpan dalam dataset "+entity+".json")
    # ----------------------------------------------------------  