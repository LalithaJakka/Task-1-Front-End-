leadlist=input().split( )
dict1={}
for str1 in leadlist:
    company_name = str1.split("@")[1].split(".com")[0]
    if company_name not in dict1:
        dict1[company_name]=[str1]
    else:
        dict1[company_name]=dict1[company_name]+[str1]
print(dict1)
dict2 = {}
for key,value in dict1.items():
    dict2[key]=len(value)
print(dict2)