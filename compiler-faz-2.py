import re

patt1=r"chap|agar|begir|ashar"
patt2=r"[0-9a-zA-Z][a-zA-Z0-9_]*"
patt3=r"[-+*/]"
patt4=r" \d+"
patt5=r"\(| \) |,| , |;| \ {|}"
patt6=r"/\*.+"
patt8=r"(.*)\*/"
patt7=r'\"[^"]*\"'
repeat=["chap","agar","begir","ashar"]
reapeat_comment=[]
repeat_str=[]
repeat_num=["1","2","3","4","5","6","7","8","9"]
#-------for faz 2

KEYWORD=[]
COMMENT=[]
STRING=[]
IDENTIFIER=[]
OPERATOR=[]
NUMBER=[]
DELIMITER=[]

with open("Simple.txt") as r:
    read=r.readlines()
    for i in read:
        if re.findall(patt1,i):
            o=re.findall(patt1,i)
            for j in o:
                print("KEYWORD",j)
                KEYWORD.append(j)
        if re.findall(patt6,i):
            o6=re.findall(patt6,i) 
            for j5 in o6:
                reapeat_comment.append(j5[2:])
                print("COMMENT",j5[2:])
                COMMENT.append(j5[2:])
        if re.findall(patt8,i):
            o8=re.findall(patt8,i) 
            for j7 in o8:
                print("COMMENT",j7)
                COMMENT.append(j7)
                reapeat_comment.append(j7)
        if re.findall(patt7,i):
            o7=re.findall(patt7,i)
            for j6 in o7:
                print("STRING",j6)
                for unic in j6[1:-1].split(" "):
                    repeat_str.append(unic)
                    STRING.append(unic)
        if re.findall(patt4,i):
            o4=re.findall(patt4,i)
            for j3 in o4:
                print("NUMBER",j3)
                NUMBER.append(j3)
        if re.findall(patt2,i) :
            o1=re.findall(patt2,i)
            for j1 in o1:
                if j1 not in repeat  :
                    if j1 not in repeat_num:
                        if j1 not  in reapeat_comment:
                            if j1 not in repeat_str:                            
                                 print("IDENTIFIER",j1)
                                 IDENTIFIER.append(j1)
        if re.findall(patt3,i):
            o3=re.findall(patt3,i)
            for j2 in o3:
                print("OPERATOR",j2)
                OPERATOR.append(j2)

        if re.findall(patt5,i):
            o5=re.findall(patt5,i)
            for j4 in o5:
                print("DELIMITER",j4)
                DELIMITER.append(j4)


#------------------------------------------------------------------------------------------ faz 1 finish--------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------az inja be bad estefade az token hast----------------------------------------------------------------------

print("#-----------------------------------------------------------------------------------------------start next faz---------------------------------------------------------------------------")

''' #test
print(KEYWORD)
print(COMMENT)
print(STRING)
print(IDENTIFIER)
print(OPERATOR)
print(NUMBER)
print(DELIMITER)
'''

KEYWORD_correct=["chap","agar","begir","ashar","void","class"]
KEYWORD_not_correct=["cha","aga",'begi',"asha","voi","clas","hap","gar","egir","shar","oid","lass","cap","aar","bgir","ahar","vid","cass","chap","aar","beir","ashr","vod","clas"]
IDENTIFIER_syn=["1","2","3","4","5","6","7","8","9","!","@","$"]

for q in  KEYWORD:
    if q in KEYWORD_correct:
        print(q,"   correct Syntax")           
for q1 in  IDENTIFIER:
    if q1 in KEYWORD_not_correct:
        print(q1,"   SyntaxError")
        IDENTIFIER.remove(q1)
        
for q2 in COMMENT:
    print(q2,"    COMMENT for explanation")

for q3 in STRING:
    print(q3,"  correct string value")
    

with open("Simple.txt") as r:
    for l in r:
        count=l.count('"')
        if count==2:
            f=l.find('"')
            f1=l.rfind('"')
            if l[f+1:f1] in IDENTIFIER:
                IDENTIFIER.remove(l[f+1:f1])
            print(l[f+1:f1],"   correct string")
        if count ==1:
            f2=l.find('"')
            f3=l.find(')')
            if l[f2+1:f3] in IDENTIFIER:
                IDENTIFIER.remove(l[f2+1:f3])
            print(l[f2+1:f3],"   String Error")
        if count ==0:
            pass

    
for q4 in IDENTIFIER:
    if q4.startswith("1") or q4.startswith("2") or q4.startswith("3") or q4.startswith("4") or q4.startswith("5") or q4.startswith("6") or q4.startswith("7") or q4.startswith("8") or q4.startswith("9") :
        print(q4 ,"    IDENTIFIER Error")
    else:
        print(q4 ," correct IDENTIFIER")


for q5 in OPERATOR:
    if q5=="*":
        print(q5,"   star correct OPERATOR")
    if q5=="/":
        print(q5,"   backslash correct OPERATOR")
    if q5=="+":
        print(q5,"   addition correct OPERATOR")
    if q5=="-":
        print(q5,"   subtraction correct OPERATOR")


for q6 in NUMBER:
    print(q6,"  number value integer")

print("--------------------------------")

check_b=[]
check_com=[]

with open("Simple.txt") as y:
    for li in y:
        if li.endswith(';'):
            print(li,"the line  has ;")
        count_p=li.count("(")
        count_p1=li.count(")")
        if count_p==count_p1:
            print(li ,"  correct ( ) ")
        else:
            print(li ,"  Error  ( ) ")
        if li.find('{') > 0:
            check_b.append(li[li.find('{')])
        if li.find('}') > 0:
            check_b.append(li[li.find('}')])
            
        if li.startswith('/') :
            check_com.append(li[li.find('/')])
            
        if li.endswith('/') or li[li.find('/')]==li[-2] :
            check_com.append(li[li.find('/')])
            
if len(check_b)%2==0:
    print("{ } in program correct")
else:
    ("{ } in program Error")
    
if len(check_com)%2==0:
    print("comment in program Error")


#---------------------------------------------------finish faz 2-------------------------------------------------------------------------------------------







