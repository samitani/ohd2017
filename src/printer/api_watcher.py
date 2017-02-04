#!/usr/bin/python

import time
import urllib2
import json


class PPAPAPIWatcher:
    API_HOST = 'yhack-ppap17.mybluemix.net'
    API_ENTRY_POINT = '/api/ppapcode'
    callback = ''

    def __init__(self, cb):
        self.callback = cb

    def run(self):
        while True:
            time.sleep(1)
            print "INFO: HTTP get..."
            response = urllib2.urlopen('http://' + self.API_HOST + self.API_ENTRY_POINT)
            body = response.read()

            jsondata = json.loads(body)

            if 'ppap' in jsondata and jsondata['ppap']:
                self.callback()

watcher = PPAPAPIWatcher(xyz)
watcher.run()
