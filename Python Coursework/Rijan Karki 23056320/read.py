#read.py
#open and read the furniture details of a file
def fileopen():
    fileopen = open("furnituredetails.txt", "r")
    #print(fileopen.read())
    fileopen.close()
#fileopen()
#read the furniture details and converting into a list
def listt():
    fileopen = open("furnituredetails.txt", "r")
    rec = []
    for hello in fileopen:
        b = hello.replace("\n","")
        rec.append(b.split(","))
    fileopen.close()
    return rec
#print(listt())



    

    
    




        
        



    


