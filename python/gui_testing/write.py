import sys
ar = sys.argv[0]
for i in range(9999999999):

    f = open("te.txt", 'w')
    data = "%s %%d" % i
    f.write(data)
    f.close()
