#!/usr/bin/env python2

from mpd import MPDClient
client = MPDClient()
client.timeout = 10
client.idletimeout = None
client.connect("localhost", 6600)

result = client.listfiles('/Cake')
res_list = []
for i in result:
        if 'directory' in i:
                    res_list.append(i['directory'])
                    for item in res_list:
                            print(item)
client.close
client.disconnect
