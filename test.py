#!/usr/bin/env python
import sys
from mpd import MPDClient
client = MPDClient()
client.timeout = 10
client.idletimeout = None
client.connect("localhost", 6600)

var = raw_input("Search artist: ")
result = client.search('any', "%s" % var)
res_list = set()
for i in result:
        if 'artist' in i:
            res_list.add(i['artist'])
for item in sorted(list(res_list)):
    print(item)                            
''.join(res_list)
print(res_list)
#print(result)
client.close
client.disconnect
