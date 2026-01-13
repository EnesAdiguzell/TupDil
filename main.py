output = ""
def main():
    # DO NOT CHANGE
    global output
    handle = open('input.tup')
    code = handle.read()
    handle.close()

    from decimal import Decimal

    rakamlar = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    changable = code.replace("İ", "i").replace("I", "ı").replace("r","r")
    code = changable
    welcome_list = code.lower().split("\n")
    result = ""
    ce = []

    for rmp in range(len(welcome_list)):
       jnk = welcome_list[rmp].split()
       for mem in jnk:
        if "." in mem and "," in mem:
           vir = mem.split(",")
           nok = vir[0].split(".")
           try:
             if len(vir[1]) > 3: 
                ce.append(rmp + 1)
             if len(nok) == 2:
                nok[0] = nok[0].lstrip("-")
                if len(nok[1]) != 3 and len(nok[0]) > 0:
                   ce.append(rmp + 1)
           except: None
        if "." in mem and "," not in mem:
           nok = mem.split(".")
           nok[0] = nok[0].lstrip("-")
           if nok[0].isdigit() and nok[1].isdigit():
              if len(nok[1]) != 3 and len(nok[0]) > 0:
                 ce.append( rmp + 1)
        if "," in mem and "." not in mem:
           vir = mem.split(",")
           if len(vir[1]) > 3:
              ce.append(rmp + 1)

    


    for m in range(len(welcome_list)):
      processed_text = []
      for i in range(len(welcome_list[m])):
         if (welcome_list[m][i] == '.' and i > 0 and i < len(welcome_list[m]) - 1 and welcome_list[m][i-1].isdigit() and welcome_list[m][i+1].isdigit()):
            continue
         processed_text.append(welcome_list[m][i])
      result += ''.join(processed_text) + '\n' 
    result = result.strip()
    
    welcome_list = result.split("\n")
    rte = []
    temp_sözlük = {}
    sözlük = {}
    işlem = [ "çarp",  "bölü", "artı", "eksi"]
    alphabet = ["a", "b", "c", "ç", "d", "e", "f", "g" ,"ğ", 
                "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r"
                "s", "ş", "t", "u", "ü", "v", "y", "z"]
    tür = ["metin", "reel-sayı", "tam-sayı"]
    sabit = ["bir", "değeri", "olsun", "zıpla", "yazdır", "programı", "bitir", "başlat", "artı", "eksi", "çarp", "bölü", "satıra"]
    tam = []
    reel = []
    metin = []
    toplam = []
    tip_ce = []

    for i in range(len(welcome_list)):
     row = welcome_list[i].split()
     nk = welcome_list[i].split("!")

     

     if "değeri" in row and "olsun." not in row:
        ce.append(i+ 1)
        
     if "  " in welcome_list[i]:
      if len(nk) == 3:
         if "  " in nk[0] or "  " in nk[2]:
          ce.append(i + 1)
         elif len(nk) > 3:
            for i in range(len(nk)):
               if i % 2 == 0:
                  if "  " in nk[i]:
                     ce.append(i + 1)
      elif len(nk) == 0:
         ce.append(i + 1)

     try:

      if row[-1] == "olsun." and row[1] == "bir" :
         if True == True:
            for lmk in list(row[0]):
               if lmk not in alphabet:
                  if lmk != "r" and lmk!= "s":
                   ce.append(i + 1) 
         if row[2] not in tür:
            ce.append(i + 1)

         if row[0] in sabit:
            ce.append(i + 1)

         if len(list(row[0])) > 20:
            ce.append(i + 1)
          
     except: None

     try:
      if row[2] == "tam-sayı":
        tam.append(row[0])
        if row[0] in metin:
           metin.remove(row[0]) 
        elif row[0] in reel:
           reel.remove(row[0])
      if row[2] == "reel-sayı":
        reel.append(row[0])
        if row[0] in metin:
           metin.remove(row[0]) 
        elif row[0] in tam:
           tam.remove(row[0])
      if row[2] == "metin":
        metin.append(row[0])
        if row[0] in reel:
           reel.remove(row[0]) 
        elif row[0] in tam:
           tam.remove(row[0])
     except:
        None
        
     try: 
         if row[-1] == "yazdır.":
            if "değeri" in row or "olsun." in row or "zıpla." in row or "bir" in row:
               ce.append(i + 1)
            for jk in range(len(row)):
               if row[jk] in işlem:
                if "," in row[jk - 1] and "," not in row[jk + 1]:
                  ce.append(i + 1)
                elif "," not in row[jk - 1] and "," in row[jk + 1]:
                  ce.append(i + 1)
     except: None


     if row[1] == "değeri" and row[-1] == "olsun.":
        if len(row) == 4 and len(nk) < 4:
           if row[0] in tam:
              if "," in row[2]:
                ce.append( i + 1)
              
              try:
                 if len(row[2]) > 5: 
                     ce.append(i + 1)
              except:
                 None
              

           if row[0] in reel:
              if "," not in row[2] :
                 try:
                    float(row[2])
                    ce.append(i + 1)
                 except: None
              try:
                before_dot, _, after_dot = row[2].partition(",")
                if len(before_dot) > 5 or len(after_dot) > 3 :
                     ce.append(i + 1)
              except: None

           if row[0] in metin and ("artı" not in row and "eksi" not in row and "çarp" not in row and "bölü" not in row):
              m = welcome_list[i].split("!")
              try:
               if len(m) != 3:
                  ce.append(i + 1)
               if len(m[1].strip("!")) > 20:
                 ce.append(i + 1)
              except:None


        elif len(row) > 4 and row[0] not in metin and (row[0] in tam or row[0] in reel) :  
          if "artı" not in row and "eksi" not in row and "çarp" not in row and "bölü" not in row:
             ce.append(i + 1)
          ok = 0
          for uu in row:
            if uu in işlem:
                ok = ok + 1
          ok = 4 + 2*ok
          if len(row) != ok:
            ce.append(i + 1)

          if row[0] in tam :
              for nn in range(len(row)):
                 if row[nn] in işlem:
                    if ("," in row[nn - 1] and "!" not in row[nn -1 ]) or ("," in row[nn + 1] and "!" not in row[nn + 1]):
                      ce.append(i + 1)

          if row[0] in reel :
             for mm in range(len(row)):
                if row[mm] in işlem:
                    try:
                       float(row[mm - 1].replace(",", "."))
                       float(row[mm + 1].replace(",", "."))
                       if "," not in row[mm - 1] or "," not in row[mm + 1]:
                         ce.append(i + 1)
                       aa = row[mm - 1].replace(",", ".")
                       ab = row[mm + 1].replace(",", ".")
                       try:
                         float(aa)
                         float(ab)
                       except:
                         ce.append(i + 1)
                    except:None

        if row[0] in metin:
            b = []
            a = welcome_list[i].split("!")
            for an in range(len(a)):
               if an % 2 == 1:
                  b.append(a[an])
               else:
                  y = a[an].split()
                  b.extend(y)

            bam = 0
            nam = 0
            for kk in range(len(b)):
                if b[kk] == "artı" or b[kk] == "eksi" : 
                   bam += 1  
                if b[kk] == "bölü":
                   ce.append(i + 1)
            bam = 2 + 2*bam
            if len(row) > 4 and len(nk) >= 3 :
             for km in list(code):
                if "!" == km:
                  nam += 1
            if nam != bam and nam != 0:
               ce.append(i + 1)


     if row[-1] == "olsun.":
        if "bir" not in row and "değeri" not in row:
            ce.append(i + 1)
     if row[-1] == "zıpla.":
        if row[-2] != "satıra" or "." not in row[-3]:
            ce.append(i + 1)
        for com in row:
           if "," in com:
              ce.append(i + 1)
              
     for h in range(len(row)):
      if row[0] != "metin":
        if h in işlem:
            try:
             float(row[h - 1].replace(",", "."))
             re = True
            except:
             re = False
            try:
             float(row[h + 1].replace(",", "."))
             ra = True
            except:
             ra = False
             if ra != re:
              ce.append(i + 1)
      else:
         if row[0] == "metin":
            if h == "artı" or h == "eksi":
             if "!" in row[h - 1]:
                if "!" not in row[h + 1]:
                    ce.append(i + 1)
                if "!" not in row[h + 1]:
                    ce.append(i + 1)

                elif "!" not in row[ h - 1]:
                 if "!" in row[h + 1]:
                    ce.append(i + 1)

                elif "!" not in row[h - 1] and "!" not in row[h + 1]:
                 try:
                    float(row[h - 1].replace(",", "."))
                    rem = True
                 except:
                    rem = False
                 try:
                    float(row[h + 1].replace(",", "."))
                    ram = True
                 except:
                    ram = False
                 if ram != rem:
                    ce.append(i + 1)
     
                    

                  

    def virgül(y):
        return [i.replace(",", ".") for i in y]
    def nokta(y):
        return [i.replace(".", "") for i in y]
    
    def işle_float(y, exp, sözlük):
      if y[exp - 1] in sözlük:
         first_operand = Decimal(sözlük[y[exp - 1]])
      else:
         first_operand = Decimal(y[exp - 1])
    
      if y[exp + 1] in sözlük:
          second_operand = Decimal(sözlük[y[exp + 1]])
      else:
         second_operand = Decimal(y[exp + 1])
    
      return first_operand, second_operand
    
    def işle_int(y, exp, sözlük):
      if y[exp - 1] in sözlük:
         first_operand = int(sözlük[y[exp - 1]])
      else:
         first_operand = int(y[exp - 1])
    
      if y[exp + 1] in sözlük:
          second_operand = int(sözlük[y[exp + 1]])
      else:
         second_operand = int(y[exp + 1])
    
      return first_operand, second_operand
    
    def işle_string(y, exp, sözlük):
      
      if y[exp - 1] in sözlük:
         first_operand = str(sözlük[y[exp - 1]])
      else:
         first_operand = str(y[exp - 1]).strip("!")
    
      if y[exp + 1] in sözlük:
          second_operand = str(sözlük[y[exp + 1]])
      else:
         second_operand = str(y[exp + 1]).strip("!")
    
      return first_operand, second_operand
    
    def format_number(input_value):
       number_str = str(input_value)
       if not any(c.isdigit() or c == '.' for c in number_str):
         return input_value
 
       number_str = number_str.replace('.', ',')

       if ',' in number_str:
         before_comma, after_comma = number_str.split(',')
       else:
         before_comma, after_comma = number_str, ""

       reversed_before = before_comma[::-1]
       grouped = '.'.join([reversed_before[i:i+3] for i in range(0, len(reversed_before), 3)])
       formatted_before = grouped[::-1]

       if after_comma:
         return f"{formatted_before},{after_comma}"
       else:
         return formatted_before
       
    def digit_control(sayi,i):
     try:
        # Sayıyı stringe çevir
        sayi_str = str(sayi)

        # Nokta ile ayır ve tam kısmı ve kesir kısmını al
        tam_kisim, kesir_kisim = (sayi_str.split('.') + [""])[:2]  # Kesir yoksa boş dizi ekle

        # Tam kısmın uzunluğunu kontrol et (negatif işareti varsa çıkar)
        tam_kisim = tam_kisim.lstrip('-')  # Negatif işareti kaldır
        if len(tam_kisim) > 5:
            rte.append(i + 1)
            return  False # Tam kısım 5 basamaktan uzun olmamalı

        # Kesir kısmın uzunluğunu kontrol et
        if len(kesir_kisim) > 3:
            rte.append(i + 1)
            return False  # Kesir kısım 3 basamaktan uzun olmamalı

        return True
     except Exception as e:
         rte.append(i + 1)
         return False


    
    i = 0
    while i < len(welcome_list):
        
        if ce:
          min_value = min(ce)
          output += f"Compile error at line {min_value}.\n"
          break
        

        if welcome_list[0] != "programı başlat.":
               output += "Compile error at line 1."
               break
        elif welcome_list[-1] != "programı bitir.":
             output += f"Compile error at line {len(welcome_list) - 1}.\n"
             break
        else:
             y = welcome_list[i].split()
             if y[0] in temp_sözlük and temp_sözlük[y[0]] == "float" and y[-1] != "zıpla." and y[-1] != "yazdır.":
                if ((("çarp" in y) or ("bölü" in y) or ("artı" in y) or ("eksi" in y))):
                    result = 0
                    y = virgül(y)
                    y = [item.strip('!') for item in y]
                    for exp in range(len(y)):
                        if y[exp] in sözlük:
                              y[exp] = sözlük[y[exp]]
                    for exp in range(len(y)):
                        mer = y[2:-1]
                        for hj in range(len(mer)):
                         if "," not in str(mer[hj]) and "." not in str(mer[hj]) and hj%2 == 0:
                            rte.append(i + 1)
                            break
                        if y[exp] in işlem:
                            try:
                                first_operand, second_operand = işle_float(y, exp, sözlük)
                                if y[exp] == "çarp":
                                    result = float(first_operand * second_operand)
                                    tam_kisim, kesir_kisim = (str(result).split('.') + [""])[:2]
                                    if len(kesir_kisim) > 3:
                                       rte.append(i + 1)
                                    if not -10001 < result < 10001:
                                       rte.append(i + 1)
                                elif y[exp] == "bölü":
                                    result = float(first_operand / second_operand)
                                    tam_kisim, kesir_kisim = (str(result).split('.') + [""])[:2]
                                    if len(kesir_kisim) > 3:
                                       rte.append(i + 1)
                                    if not -10001 < result < 10001:
                                       rte.append(i + 1)
                                elif y[exp] == "artı":
                                    result = float(first_operand + second_operand)
                                    tam_kisim, kesir_kisim = (str(result).split('.') + [""])[:2]
                                    if len(kesir_kisim) > 3:
                                       rte.append(i + 1)
                                    if not -10001 < result < 10001:
                                       rte.append(i + 1)
                                elif y[exp] == "eksi":
                                    result = float(first_operand - second_operand)
                                    tam_kisim, kesir_kisim = (str(result).split('.') + [""])[:2]
                                    if len(kesir_kisim) > 3:
                                       rte.append(i + 1)
                                    if not -10001 < result < 10001:
                                       rte.append(i + 1)
                                y[exp + 1] = result
                            except:
                                continue
                    sözlük[y[0]] = result
                    if "yazdır." in y:
                       output += f"{result}\n"

             if y[0] in temp_sözlük and temp_sözlük[y[0]] == "int" and y[-1] != "zıpla." and y[-1] != "yazdır.":
                if ((("çarp" in y) or ("bölü" in y) or ("artı" in y) or ("eksi" in y))):
                    result = 0
                    y = [item.strip('!') for item in y]
                    
                    for exp in range(len(y)):
                        if y[exp] in sözlük:
                           y[exp] = sözlük[y[exp]]
                    for exp in range(len(y)):
                        if y[exp] in işlem: 
                           try:
                                first_operand, second_operand = işle_int(y, exp, sözlük)
                                if y[exp] == "çarp":
                                    result = first_operand * second_operand
                                    result = float(result)
                                    if not -10000 <= result <= 10000:
                                       rte.append(i + 1)
                                elif y[exp] == "bölü":
                                    result = first_operand / second_operand
                                    if not -10000 <= result <= 10000:
                                       rte.append(i + 1)
                                elif y[exp] == "artı":
                                    result = first_operand + second_operand
                                    if not -10000 <= result <= 10000:
                                       rte.append(i + 1)
                                elif y[exp] == "eksi":
                                    result = first_operand - second_operand
                                    if not -10000 <= result <= 10000:
                                       rte.append(i +1)
                                y[exp + 1] = result
                           except: 
                              continue
                    sözlük[y[0]] = result

             if y[0] in temp_sözlük and temp_sözlük[y[0]] == "string" and y[-1] != "zıpla.":
                if ("artı" in y) or ("eksi" in y) or ("çarp" in y) :
                    result = ""
                    if row[0] in metin:
                       b = []
                       a = welcome_list[i].split("!")
                       for an in range(len(a)):
                          if an % 2 == 1:
                            b.append(a[an])
                          else:
                            y = a[an].split()
                            b.extend(y)
                    y = b
                    for exp in range(len(y)):
                        if y[exp] in işlem:
                            if y[exp] in sözlük:
                                y[exp] = sözlük[y[exp-1]] + sözlük[y[exp+1]]
                            try:
                                first_operand, second_operand = işle_string(y, exp, sözlük)
                                if y[exp] == "artı":
                                    result = first_operand + second_operand
                                elif y[exp] == "eksi":
                                    a = first_operand
                                    b = second_operand
                                    for z in b:
                                        a = a.replace(z, "")
                                    result = a
                                elif y[exp] == "çarp":
                                   for rakam in rakamlar:
                                    if rakam in y[exp - 1]:
                                      result = int(y[(exp - 1)]) * second_operand
                                    elif rakam in y[exp + 1]:
                                        result = first_operand * int(y[exp + 1])
                                y[exp + 1] = result
                            except: 
                                continue
                    sözlük[y[0]] = result
                    if len(list(result)) > 50:
                       rte.append(i + 1)


             if "tam-sayı" in y and len(y) <= 4:
                temp_sözlük[y[0]] = "int"

             elif "reel-sayı" in y and len(y) <= 4 :
                temp_sözlük[y[0]] = "float"
             
             elif "metin" in y and len(y) <= 4:
                temp_sözlük[y[0]] = "string"

             elif "olsun." in y  and "tam-sayı" not in y and "reel-sayı" not in y and "metin" not in y and "artı" not in y and "eksi" not in y and "çarp" not in y and "bölü" not in y :
                    if y[0] in temp_sözlük:
                    # Eğer temp_sözlük'te tür bilgisi varsa, önceki türü kontrol et
                     tür = temp_sözlük[y[0]]
                     if tür == "int":
                        sözlük[y[0]] = int(y[2])
                     elif tür == "float":
                        try:
                         sözlük[y[0]] = float(Decimal(y[2].replace(",", ".")))
                        except:
                           output += f"Runtime error at line {i + 1}.\n"
                           break
                     elif tür == "string":
                        temp_list = welcome_list[i].split("!")
                        try:
                         sözlük[y[0]] = str(temp_list[1])
                        except:
                          None
                    else:
                       try:
                          sözlük[y[0]] = float(Decimal(y[2]))
                       except:
                           sözlük[y[0]] = str(y[2])


             elif "zıpla." in y:
               if len(y) == 3:
                 if str(y[-3]).replace(".", "") in sözlük.keys():
                     try:
                        if int(sözlük[str(y[-3]).replace(".", "")]) == float(sözlük[str(y[-3]).replace(".", "")]):
                           a = int(sözlük[str(y[-3]).replace(".", "")])
                     except:
                        output += f"Runtime error at line {i + 1}.\n"
                        break
                     try:
                      if a > len(welcome_list) and int(a) == float(a):
                         output += f"Runtime error at line {i + 1}.\n"
                         break
                      else:
                         i = a - 2
                     except:
                        output += f"Runtime error at line {i + 1}.\n"
                        break

                 else:
                  a = int(str(y[-3]).replace(".", ""))
                  if a > len(welcome_list):
                        output += f"Runtime error at line {i + 1}.\n"
                        break
                  else:
                        i = a - 2
               
               if len(y) > 3:
                    result_m = 0
                    y = virgül(y)
                    y = [item.strip('!') for item in y]
                    y = nokta(y)
                    for exp in range(len(y)):
                        if y[exp] in sözlük:
                              y[exp] = sözlük[y[exp]]
                    for exp in range(len(y)):
                        if "." not in str(y[exp]):
                           rte.append(i + 1)
                        if y[exp] in işlem:
                            try:
                                first_operand, second_operand = işle_float(y, exp, sözlük)
                                if y[exp] == "çarp":
                                    result_m = first_operand * second_operand
                                    tam_kisim, kesir_kisim = (str(result_m).split('.') + [""])[:2]
                                    if len(kesir_kisim) > 3:
                                       rte.append(i + 1)
                                    if not -10001 < result_m < 10001:
                                       rte.append(i + 1)
                                elif y[exp] == "bölü":
                                    result_m = first_operand / second_operand
                                    tam_kisim, kesir_kisim = (str(result_m).split('.') + [""])[:2]
                                    if len(kesir_kisim) > 3:
                                       rte.append(i + 1)
                                    if not -10001 < result_m < 10001:
                                       rte.append(i + 1)
                                elif y[exp] == "artı":
                                    result_m = first_operand + second_operand
                                    tam_kisim, kesir_kisim = (str(result_m).split('.') + [""])[:2]
                                    if len(kesir_kisim) > 3:
                                       rte.append(i + 1)
                                    if not -10001 < result_m < 10001:
                                      rte.append(i + 1)
                                elif y[exp] == "eksi":
                                    result_m = first_operand - second_operand
                                    tam_kisim, kesir_kisim = (str(result_m).split('.') + [""])[:2]
                                    if len(kesir_kisim) > 3:
                                       rte.append(i + 1)
                                    if not -10001 < result_m < 10001:
                                       rte.append(i + 1)
                                    y[exp + 1] = result_m
                                result_final = result_m
                            except:
                                continue
                            if result_final > len(welcome_list):
                                output += f"Runtime error at line {i}.\n"
                                break
                            elif True == True:
                                 try:
                                   if int(result_final) == float(result_final):
                                      i = int(result_final) - 2
                                 except:
                                    output += f"Runtime error at line {i + 1}.\n"
                                    break
                            else:
                                 i = int(result_final) - 2  
            
             elif "yazdır." in y and len(y) <= 2:
               if y[0] in sözlük.keys():
                   tp_a = sözlük[y[0]]
                   tpm = str(format_number(tp_a))
                   output += f"{tpm}\n"
               else:
                   tp_a = y[0]
                   tpm = format_number(tp_a)
                   output += f"{tpm}\n"

             elif "yazdır." in y and len(y) > 2:
                    a = ""
                    result_p = 0    
                    y = [item.strip('!') for item in y]
                    y = nokta(y)
                    for exp in range(len(y)):
                        if y[exp] in sözlük:
                              y[exp] = str(sözlük[y[exp]]).replace(".", ",")
                    for exp in range(len(y)):
                           if y[exp] in işlem:
                            if not (y[exp-1].isdigit() and y[exp + 1].isdigit()):
                               if y[exp] == "bölü":
                                  rte.append(i+ 1)
                                  break
                               else:
                                    b = []
                                    a = welcome_list[i].split("!")
                                    for an in range(len(a)):
                                       if an % 2 == 1:
                                          b.append(a[an])
                                       else:
                                          y = a[an].split()
                                          b.extend(y)
                                    y = b
                                    for exp in range(len(y)):
                                          if y[exp] in işlem:
                                             if y[exp] in sözlük:
                                                y[exp] = sözlük[y[exp-1]] + sözlük[y[exp+1]]
                                             try:
                                                first_operand, second_operand = işle_string(y, exp, sözlük)
                                                if y[exp] == "artı":
                                                      result = first_operand + second_operand
                                                elif y[exp] == "eksi":
                                                      a = first_operand
                                                      b = second_operand
                                                      for z in b:
                                                         a = a.replace(z, "")
                                                      result = a
                                                elif y[exp] == "çarp":
                                                   for rakam in rakamlar:
                                                      if rakam in y[exp - 1]:
                                                         result = int(y[(exp - 1)]) * second_operand
                                                      elif rakam in y[exp + 1]:
                                                         result = first_operand * int(y[exp + 1])
                                                y[exp + 1] = result
                                             except: 
                                                continue
                                    sözlük[y[0]] = result
                                    if len(list(result)) > 50:
                                       rte.append(i + 1)
                                   

                            try:
                             if "," not in str(y[exp -1]) and "," not in str(y[exp + 1]):
                                 a = "tam"
                            except:None
                            try:
                                y = virgül(y)
                                first_operand, second_operand = işle_float(y, exp, sözlük)
                                if y[exp] == "çarp":
                                    result_p = first_operand * second_operand
                                    tam_kisim, kesir_kisim = (str(result_p).split('.') + [""])[:2]
                                    if len(kesir_kisim) > 3:
                                       rte.append(i + 1)
                                    if not -10001 < result_p < 10001:
                                       rte.append(i + 1)
                                elif y[exp] == "bölü":
                                    result_p = first_operand / second_operand
                                    tam_kisim, kesir_kisim = (str(result_p).split('.') + [""])[:2]
                                    if len(kesir_kisim) > 3:
                                       rte.append(i + 1)
                                    if not -10001 < result_p < 10001:
                                       rte.append(i + 1)
                                elif y[exp] == "artı":
                                    result_p = first_operand + second_operand
                                    tam_kisim, kesir_kisim = (str(result_p).split('.') + [""])[:2]
                                    if len(kesir_kisim) > 3:
                                       rte.append(i + 1)
                                    if not -10001 < result_p < 10001:
                                       rte.append(i + 1)
                                elif y[exp] == "eksi":
                                    result_p = first_operand - second_operand
                                    tam_kisim, kesir_kisim = (str(result_p).split('.') + [""])[:2]
                                    if len(kesir_kisim) > 3:
                                       rte.append(i + 1)
                                    if not -10001 < result_p < 10001:
                                       rte.append(i + 1)
                                    y[exp + 1] = result_p
                                result_final_p = result_p
                            except:
                                continue
                            if a == "tam":
                               result_pt = str(format_number(int(result_final_p)))
                               output += f"{result_pt}\n"
                            else:
                               result_ptt = str(format_number(result_final_p))
                               output += f"{result_ptt}\n"

        try:
        
         for key in temp_sözlük:
            if key in temp_sözlük and sözlük[key] is None:
               rte.append(i + 1)
        except: None
        
        if rte:
           output += f"Runtime error at line {i + 1}.\n"
           break
        
           
              
        i += 1

             

    # DO NOT CHANGE
    handle = open('output.txt','w')
    handle.write(output)
    handle.close()
    return sözlük

main()




    



