#!/usr/bin/env python
import cgi
import cgitb
import os
import datetime
import re

now = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')

cgitb.enable(display=0, logdir="/data/www/http_log/cgi_log")

form = cgi.FieldStorage()

f = open('/data/www/rdm-mdforms-data/sic_%s_%s.xml' % (os.environ['REMOTE_ADDR'],now),'w')
f.write(re.sub(r'\<sic\s+', '<sic xmlns:dc="http://purl.org/dc/elements/1.1/" ', form['xml'].value))
f.close()

print "Status: 200 OK"
print "Content-Type: application/json"
print