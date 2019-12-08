# two functions: name of all with length and student with longhest name
import math
import operator
def average():
    with open("SEclassnames.txt",'r') as names:
        content=names.readlines()
        
        clened_content=[]
        removed_space=[]
        total_students=len(content)
        for i in range(len(content)):
            clened_content.append(content[i].strip('\n'))
        for i in clened_content:
            
            removed_space.append(i.replace(" ", ""))
        new="".join(removed_space)
        total_length=len(new)
        average_length=round((total_length/(total_students)))
        return(" the average length is "+str(average_length))

def display_all():
    clened_content=[]
    clened_content_=[]
    removed_space=[]
    with open("SEclassnames.txt",'r') as names:
        content=names.readlines()
        for i in range(len(content)):
            clened_content.append(content[i].strip('\n'))
    
    for i in clened_content:
        removed_space.append(i.replace(" ", ""))
         
    for i in removed_space:
        clened_content_.append(str(i)+" has "+ str(len(i))+ " characters")
    return clened_content_

def longhest_name():
    clened_content=[]
    removed_space=[]
    with open("SEclassnames.txt",'r') as names:
        content=names.readlines()
        for i in range(len(content)):
            clened_content.append(content[i].strip('\n'))
    for i in clened_content:
        removed_space.append(i.replace(" ", ""))
    highest=1
    dictnames={}
    for i in removed_space:
        dictnames[i]=len(i)
    v=list(dictnames.values())
    k=list(dictnames.keys())
    
    return k[v.index(max(v))] + " has longhest characters: "+ str(max(v))


    # Additional three functionalities according to user story
    # for user story one, the user will enter the name and check if his name is present or not
    # for user story two, program should display the mode of the character length 
    # for user story three, program displays  names with lowest character length

with open("SEclassnames.txt",'r') as names:
    content=names.readlines()
    
    clened_content=[]
    removed_space=[]
    name_char_dict={}
    for i in range(len(content)):
        clened_content.append(content[i].strip('\n').lower())
    for i in clened_content:
            
        removed_space.append(i.replace(" ", ""))

    for k in removed_space:
        name_char_dict[k]=len(k)
    
def check_present(some_name):
    if some_name.lower() in clened_content:
        return (some_name+ " is presnt in this class")
    else:
        return ( some_name+ " is not present in this class")
         
#print(check_present( "sagar"))
# user story two additional functionalities: return mode of character length
record_each_length=[] 
for i in removed_space:
    record_each_length.append(len(i))
def calc_mode():
    frequency={}
    for i in record_each_length:
        if i not in frequency:
            frequency[i]=0
        else:
            frequency[i]+=1
    #print(record_each_length)
    mode=max(frequency.items(), key=operator.itemgetter(1))[0]
    return (" names having  " + str(mode)+ " character length appears higher times ")

def lowest_character_length_with_names():
    min_length=min(record_each_length)
     
    list_of_min_names=[]
    
    for key, value in name_char_dict.items():
        if min_length==value:
            list_of_min_names.append(key)
    list_of_min_names=str(list_of_min_names).strip('[]')
    return list_of_min_names, " has minimum length of "+ str(min_length)

 
            






