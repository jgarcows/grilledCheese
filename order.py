#!/Python27/python
import cgi
import cgitb
import re
import time

cgitb.enable()



sep='|'

print "Content-Type: text/html"
print "Cache-control: no-cache"
print

print '<HTML><head><title>Sandwich Queue!</title><!--meta http-equiv="refresh" content="5" --></head>\n<body>\n<H3>Sandwich Queue!</H3>\n'

#layout of queue "database" <name> | <bread> | <cheese, comma sep> | <toppings, comma sep> | unixTime of order\n
#There will be 3 queue "database" files, completed, in progress, and queue
#.lock files will exist for each "database" file

sanatizer = re.compile('[^a-zA-Z0-9_ ,\\|]')



#values:bread, cheese, toppings, name


fs = cgi.FieldStorage()
name = fs['name'].value
bread = fs['bread'].value
cheese = fs.getlist('cheese')
toppings = fs.getlist('toppings')

print name
print bread
print cheese
print toppings
print time.time()

#file = open("JacobList.txt", "r")

# cpy-paste form example
#        print ("<FORM method=\"post\" action=\"/cgi-bin/jPurchased.py\">{}<INPUT type=\"hidden\" name=\"line\" value=\"{}\">"
#              "<INPUT type=\"submit\" value=\"Mark as purchased\"></FORM>\n").format(m.group(1), i)


