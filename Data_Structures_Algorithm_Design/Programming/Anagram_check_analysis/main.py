def anagram(str1,str2):
    group_letters={}
    for i in str1:
        if i in group_letters:
            group_letters[i]+=1
        else:
            group_letters[i]=1
    for i in str2:
        if i in group_letters:
            group_letters[i]-=1
        else:
            group_letters[i]=1
    for j in group_letters:
        if group_letters[j]!=0:
            return False
    return True
  
  string1=input("Enter the first string: ")
string1=string1.replace(" ","").lower()
string2=input("Enter the first string: ")
string2=string2.replace(" ","").lower()
var=anagram(string1,string2)
if(var):
    print("The entered strings are anagram")
else:
    print("The entered strings are not anagram")
