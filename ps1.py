###### this is the ps1 .py file ###########
n=raw_input()
count=0
count1=0
x=len(n)
#to check even parity
for i in range(0,x):
	if n[i]=='1':
		count=count+1
#to concatinate 1 if even parity
if count%2==0:
	n_parity= n[:x]+'1'
#concatinate 0 if odd parity
else:
	n_parity= n[:x]+'0'
print n_parity

x1=len(n_parity)

#bit stuffing after 010

str2='010'
for i in range(0,x):
	if n_parity[i:i+3]==str2:
		index=i+3

	n1_parity=n_parity[:index]+'0'+n_parity[index+1:]

#print n1_parity

#to add 0 if the frame ends with 01

str1="01"
if n_parity[x1-2:]==str1:
	n1_parity=n1_parity[:len(n1_parity)]+'0'

#print n1_parity

#to add the flag at the end of frame

modified_string=n1_parity[:len(n1_parity)]+'0101'

print modified_string

