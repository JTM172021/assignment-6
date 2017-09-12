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
str2='010'
for i in range(0,x1):
	if n_parity[i:i+3]==str2:
		n1_parity=n_parity[:i+3]+'0'+n_parity[i+4:]
#print n1_parity

	
