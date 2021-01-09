file1 = open('test1.txt')
file2 = open('test2.txt')
alma = 0
count = 0



to_check = []
orginal_file = []
found_txt = []
not_found = []






f = open("outfile", "w")
for line in file1:
    #bla =  line.split(":",1)[1]
    if ("\n" in line):
        ading = line[:-1]
    else:
        ading = line
    to_check.append(ading)

for line in file2:
    if ("\n" in line):
        ading = line[:-1]
    else:
        ading = line
    orginal_file.append(ading)



x = len(to_check)
d = len(orginal_file)
print("1. Lenght ",d)
print("2. Lenght ",d)
i = 0
found = 0
not_fu = 0

while( i < x):
    f = open("list.txt","a+")
    #print(to_check[i-1])
    alma = (to_check[i-1])
    a = 0
    for a in range(d+1):
        og = orginal_file[a-1]
        
        if (alma ==  og):
            print("[!]FOUND  ----- ", alma , ":", og)
            f.write(alma)
            f.write("\n")
            found_txt.append(alma)
            found = found + 1
            i = i + 1
        else:
            not_found.append(alma)


            
        #print("To find: ", alma, " | IN TXT : ", og ) 
        if (a == d):
            f.close() 
            to_check.remove(alma)
            i = i + 1
            print(i, " OF ", x, " END OF ")
           

        
     
    

file1.close()
file2.close()
print("\n \n File 1 | \n ", to_check)
print("\n \n File 2 | \n ", orginal_file)


print("\n \n Found: \n ",found_txt)
print("\n \n Not found: ")
print(found_txt)
