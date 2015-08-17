#!/usr/bin/env python2

from functools import partial
import types
from mpd import MPDClient, ConnectionError

host = "bluesnogbox.duckdns.org"
port = 6600

class DummyClient(object):
    def connect(self, *a, **kw): print 'connecting %r %r' % (a, kw)
    def play(self):
        print 'playing'
        MPDClient.play(0)
    def stop(self): print 'stopping'

class PersistentMPDClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = DummyClient()
        self.client.connect(self.host, self.port)

    def __getattr__(self, attr, *args):
        cmd = getattr(self.client, attr, *args)
        if isinstance(cmd, types.MethodType):
            # a method -- wrap
            return lambda *a, **kw: self.command(attr, *a, **kw)
        else:
            # anything else -- return unchanged
            return cmd

    def command(self, cmd, *args, **kwargs):
        command_callable = partial(self.client.__getattribute__(cmd), *args, **kwargs)
        try:
            return command_callable()
        except ConnectionError:
            # Mopidy drops our connection after a while, so reconnect to send the command
            self.client._soc = None
            self.client.connect(self.host, self.port)
            return command_callable()

c = PersistentMPDClient(host, port)
c.play()
#c.stop()
