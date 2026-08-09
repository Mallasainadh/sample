#file handling
#write()
'''a=open("sai.txt","w")
a.write("codegnan")
a.close()'''

#append()
'''a=open("sai.txt","a")
a.write("\tdata science")
a.close()'''

'''a=open("sai.txt","w")
a.write(input("data"))
a.close()'''

'''a=open("sai.txt","w")
b=input("data")
a.write(b)
a.close()'''

#read()
'''a=open("sai.txt")
#print(a.read())#it will display entire content
#print(a.readline())#it will display first line
#print(a.readline())#it will display in list with\n
#print(a.readline(8))#it will display no.of characters
'''
#writelines()#it makes every object side by side
a=open("sai.txt","w")
b=["karthik","kiran","saiteja","kumar"]
a.writelines("\n".join(b))
a.close()

a=open("sample.py")
print(a.
