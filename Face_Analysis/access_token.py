import urllib, urllib2, sys, json
import ssl
from urllib import urlencode


host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=QllhiPhbHXzHkhWz5oGXGecj&client_secret=DyuQtk6bYmeNekMpjNGdxc8VGtCxuVEL'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
content = json.loads(content)
key = content["access_token"]
print (key)