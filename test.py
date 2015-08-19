#!/usr/bin/env python

from mpd import MPDClient
client = MPDClient()
client.timeout = 10
client.idletimeout = None
client.connect("localhost", 6600)

result = client.listfiles('/Cake')
res_list = set()
for i in result:
        if 'directory' in i:
                    res_list.add(i['directory'])
        for item in sorted(list(res_list)):
            print(item)                            
client.close
client.disconnect
