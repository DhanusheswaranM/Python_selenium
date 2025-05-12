import re
# text="Hi i am dhanush . Good morining welcome to coimbatore and i am graduate"
# res=re.search("^Hi.*graduate$",text)
# print("----------------------search functions")
# if res:
#     print("We have match")
# else:
#     print("we haven't match")

# print("----------------------findall functions")
# res2=re.findall('am',text)
# print("Result :{}".format(res2))

# print("--------------------------------")
# res3=re.search('z',text)
# print(res3)
# # print("Result :{} and start and end position:{}".format(res3,res3.span()))

# print("----------------------sub functions")
# res1=re.sub('am','amm',text)
# print("result:{}".format(res1))

# print("----------------------split functions")
# split=re.split('a',text)
# print("result :",format(split))

# result=re.search('^Hi.*graduate$',text)
# if result:
#     print("We have match")
# else:
#     print("we haven't match")

# print("--------------------------------")

# res4=re.sub(r'\bd.*h\b','soundar',text)
# print(res4)

print("******************************************")

text="Alan Turing was born on 23 June 1912 in London"
res=re.findall('\AAlan',text)
print("Result of \A :",res)
print("-"*79)

res1=re.findall(r'\bLon',text)
print("Rsult of \bLon :",res1)
print("-"*79)

res2=re.findall(r'ring\b',text)
print("Rsult of ring\b :",res2)
print("-"*79)

res2=re.findall('\Bon',text)
print("Rsult of \Bon :",res2)
print("-"*79)

res2=re.findall('\d',text)
print("Rsult of \d :",res2)
print("-"*79)

res2=re.findall('\D',text)
print("Rsult of \D :",res2)
print("-"*79)

res2=re.findall('\s',text)
print("Rsult of \s :",res2)
print("-"*79)

res2=re.findall('\S',text)
print("Rsult of \S :",res2)
print("-"*79)

res2=re.findall('\W',text)
print("Rsult of \W :",res2)
print("-"*79)

res2=re.findall('\w',text)
print("Rsult of \w :",res2)
print("-"*79)

res2=re.findall('London\Z',text)
print("Rsult of \Z :",res2)
print("-"*79)

email_pattern=r'\b([A-Za-z0-9._%+-]+)(@[A-Za-z0-9.-]+)(\.[A-Z|a-z]{2,})\b'
email="2k21eee09@kiot.ac.in"
res=re.findall(email_pattern,email)
# print(res.group(1))
# print(res.group(2))
# print(res.group(3))
if res:
    print(res)
else:
    print("Not found")