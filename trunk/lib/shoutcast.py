#!/usr/bin/env python
import urllib2

class ShoutCastClient(object):
    """
        A Shoutcast client class
    """
    def __init__(self, host):
        self.host = host

        self.response =[]
        self.bytecount = 0

        self.headers = {}
        self.metadata = {}

    def getMetadata(self):
        return self.metadata

    def connect(self):
        """
            Connect to a Shoutcast server
        """

        #todo failure checking

        self.response = urllib2.urlopen(urllib2.Request(self.host, None, {'Icy-MetaData':'1'}))

        self.parseHeaders()


    def disconnect(self):
        """
            Disconect from Shoutcast server
        """
        if self.response:
            self.response.close()


    def parseHeaders(self):
        """
            Parse response headers and check for metadata interval
        """
        headers = []

        while True:
            line = self.readline().strip()
            if line:
                headers.append(line)
            else: break

        self.headers['original'] = headers

        for header in headers:
            items = header.split(':')
            if len(items) == 2:
                key, val = items
                self.headers[key] = val


    def parseMetadata(self):
        """
            Parse metadata according to interval value
        """
        length = ord(self._read(1))*16
        metadata = self._read(length).strip().split(';')[:-1]

        for item in metadata:
            items = item.split('=')
            if len(items) == 2:
                key, val = items
                self.metadata[key] = val[1:-1]


    def readline(self):
        """
            Read a single line from response object
        """
        return self.response.readline()

    def _read(self, size):
        """
            Read size bytes from response object
        """
        return self.response.read(size)

    def read(self, size=1):
        """
            Read 1 byte from response object, while keeping count
        """

        if size > 1:
            data = []
            for i in range(size):
                data.append(self.read())
            return ''.join(data)

        byte = self._read(1)
        self.bytecount += 1

        metaint = int(self.headers.get('icy-metaint', 0))

        if self.bytecount == metaint:
            self.parseMetadata()
            self.bytecount = 0

        return byte


if __name__ == '__main__':
    from pprint import pprint

    client = ShoutCastClient('http://scfire-chi0l-1.stream.aol.com/stream/1018')
    client.connect()

    pprint(client.headers)
    pprint(client.metadata)



