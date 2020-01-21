#!/usr/bin/env python
"""
Snipped to dowload current IKEA ZLL OTA files into ~/otau
Requires python 2.7, not compatible with python 3.
"""

import os
import json
import urllib

f = urllib.urlopen("http://fw.ota.homesmart.ikea.net/feed/version_info.json")
data = f.read()

arr = json.loads(data)

otapath = '/srv/deconz/otau'

if not os.path.exists(otapath):
        os.makedirs(otapath)

for i in arr:
        if 'fw_binary_url' in i:
                url = i['fw_binary_url']
                ls = url.split('/')
                fname = ls[len(ls) - 1]
                path = '%s/%s' % (otapath, fname)

                if not os.path.isfile(path):
                        urllib.urlretrieve(url, path)
                        print(path)
                else:
                    print('%s already exists' % fname)

