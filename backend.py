#!/usr/bin/python

import urllib

link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTTZB5iGDBTZLEUxtpXQ9dK1ZGcAcrY3VDJZcn1w0Aal_JyXU9-_sZOzIf24lnp09_L9N9lOR0mJm9o/pub?gid=0&single=true&output=csv"
f = urllib.urlopen(link)
myfile = f.read()

# Http headers when outputting JSON
# Yes, you need the empty print statement or it won't work...
print "Content-Type: text/html"
print ""
print myfile
