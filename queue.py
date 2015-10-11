#!/Python27/python
import cgi
import cgitb
import re

cgitb.enable()

nameCounts = {}


breads = ["Italian", "sourdough", "honey wheat", "dill rye", "light rye", "gluten-free"]
breads.sort()
cheeses = ["pepper jack", "colby jack", "white cheddar", "swiss", "muenster", "mozzarella", "smoked provolone", "asiago"]
cheeses.sort()
toppings = ["avocado", "dill pickles", "creamy horseradish", "yellow mustard", "mayo", "horseradish mustard", "bell peppers", "sunflower seeds", "tomatoes", "ham", "bologna", "chicken", "roast beef", "turkey"]
toppings.sort()

names = ["Pia", "Hazel", "Genevieve", "Annabella", "Chris", "Mike", "Jenny", "John", "Marie", "Lynn", "Jacob", "Vickie", "Jason", "Amber", "Han", "Corrie", "Brad"]
names.sort()

def makeTableLines(dataList, allowMark=False):
    output = ''
    for line in dataList:
#        if allowMark:
#            output += "<tr>\n <td>{}</td>\n <td>{}</td>\n <td>{}</td>\n <td>{}</td>\n<td>".format(line[0], line[1], line[2], line[3])
#            output += "<FORM method=\"post\" action=\"/cgi-bin/grilledCheese/complete.py\"><INPUT type=\"hidden\" name=\"line\" value=\"{}\">"
#            output += "</td></tr>\n"
#        else:
        output += "<tr>\n <td>{}</td>\n <td>{}</td>\n <td>{}</td>\n <td>{}</td>\n</tr>\n".format(line[0], line[1], line[2], line[3])
        lName = line[0].lower()
        nameCount = 1
        if (lName in nameCounts):
            nameCount = nameCounts[lName] + 1
        nameCounts[lName] = nameCount
        line.append(nameCount)
    return output

def queueSort(one, two):
    #the number for the person is stored on the 5th item, order time on the 4th
    retVal = one[5] - two[5]
    if retVal == 0:
        retVal = int(one[4]) - int(two[4])
    return retVal

print "Content-Type: text/html"
print "Cache-control: no-cache"
print

print '<HTML><head><title>Sandwich Queue!</title><!--meta http-equiv="refresh" content="5" --></head>\n<body>\n<H3>Sandwich Queue!</H3>\n'

#layout of queue "database" <name> | <bread> | <cheese, comma sep> | <toppings, comma sep> | unixTime of order\n
#There will be 3 queue "database" files, completed, in progress, and queue
#.lock files will exist for each "database" file

sanatizer = re.compile('[^a-zA-Z0-9_ ,\\|]')

queue = [sanatizer.sub('', line.strip()).split('|') for line in open('E:\\WebData\\queue.txt', "r")]
completed = [sanatizer.sub('', line.strip()).split('|') for line in open('E:\\WebData\\completed.txt', "r")]
#inprogress = [sanatizer.sub('', line.strip()).split('|') for line in open('E:\\WebData\\inprogress.txt', "r")]

queue = [x for x in queue if len(x) == 5]
completed = [x for x in completed if len(x) == 5]
#inprogress = [x for x in inprogress if len(x) == 5]



completedTable = makeTableLines(completed)
#inprogressTable = makeTableLines(inprogress)
makeTableLines(queue)

queue.sort(queueSort)

def columnCheckTable(name, options, cols=2):
    i = 0
    print '   <table>\n    <tr><td>'
    for option in options:
        print '   <INPUT type="checkbox" name="{}" value="{}"> {} '.format(name, option, option)
        i += 1
        if i % ((len(options)+cols -1)/cols) == 0:
            print '     </td><td>'
        elif i != len(options):
            print '     <br>'
    print '     </td></tr></table>'
    

def columnRadioTable(name, options, cols=2):
    i = 0
    print '   <table>\n    <tr><td>'
    for option in options:
        print '   <INPUT type="radio" name="{}" value="{}"> {} '.format(name, option, option)
        i += 1
        if i % ((len(options)+cols -1)/cols) == 0:
            print '     </td><td>'
        elif i != len(options):
            print '     <br>'
    print '     </td></tr></table>'

#file = open("JacobList.txt", "r")

print '<table style="width:100%" border="1">'
#print '<tr>\n <th colspan="4"> In Progress </th></tr>'
#print "<tr>\n <th>Name</th>\n <th>Bread</th>\n <th>Cheese</th>\n <th>Toppings</th>\n</tr>"
#print inprogressTable
print '<tr>\n <th colspan="4"> Queue </th></tr>'
print "<tr>\n <th>Name</th>\n <th>Bread</th>\n <th>Cheese</th>\n <th>Toppings</th>\n</tr>"
print makeTableLines(queue, True)
print '<tr>\n <th colspan="4"> Completed </th></tr>'
print "<tr>\n <th>Name</th>\n <th>Bread</th>\n <th>Cheese</th>\n <th>Toppings</th>\n</tr>"
print completedTable
print '</table>'

print '<h3>Request a sandwich!</h3>'
print '<FORM method="post" action="/cgi-bin/grilledCheese/order.py">'
print '<table border="1">\n <tr>\n  <th>Bread</th>\n  <th>Cheese (up to 2)</th>\n  <th>Toppings</th>\n </tr>'
print '  <td>'
columnRadioTable("bread", breads)
print '  </td>'
print '  <td>'
columnCheckTable("cheese", cheeses)
print '  </td>'
print '  <td>'
columnCheckTable("toppings", toppings, 3)
print '   Custom: <input type="text" name=toppings>'
print '  </td></tr>'
print '  <tr>'
print '   <td colspan="3"> Name: '
print '    <select name="name">'
for name in names:
    print '<option value="{}" >{}</option>'.format(name, name)
print '    </select>'
print '    <input type="submit" value="SUBMIT!!" style="float: right;"></td></tr>'
print ' </table>'
print ' '
print '</body>'


# cpy-paste form example
#        print ("<FORM method=\"post\" action=\"/cgi-bin/jPurchased.py\">{}<INPUT type=\"hidden\" name=\"line\" value=\"{}\">"
#              "<INPUT type=\"submit\" value=\"Mark as purchased\"></FORM>\n").format(m.group(1), i)


