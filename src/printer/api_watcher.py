#!/usr/bin/python

import time
import http.client

class PPAPAPIWatcher:
    API_HOST = 'yhack-ppap17.mybluemix.net'
    API_ENTRY_POINT = '/api/ppapcode'

    def run(self):
        while True:
            time.sleep(1)
            conn = http.client.HTTPConnection(self.API_HOST)
            conn.request('GET', self.API_ENTRY_POINT)

            print conn.getresponse()


watcher = PPAPAPIWatcher()
watcher.run()
