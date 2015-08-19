#!/usr/bin/env python

from mpd import MPDClient
client = MPDClient()
client.timeout = 10
client.idletimeout = None
client.connect("localhost", 6600)

result = client.search('any', 'Led Zeppelin')
res_list = set()
for i in result:
        if 'artist' in i:
            res_list.add(i['artist'])
for item in sorted(list(res_list)):
    print(item)                            
#print(result)
client.close
client.disconnect
