def correct(path):
    fin = open(path,"r")

    data = fin.read()

    data = data.replace("("," ")

    outdata = []
    array = data.split('\n')
    for n in array:
        if n != "":
            outdata.append("".join(["(" + n + "\n"]))


    fin.close()
    fout = open(path,"w")
    for line in outdata:
        fout.write(line)
    fout.close()

def correct_validation(data):
    
    
    data = data.replace("\n","\\n")
    data = data.replace(",","\n")
    
   
    
    return data
