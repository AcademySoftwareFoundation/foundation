#!/usr/bin/env python3
#
# Copyright this project and it's contributors
# SPDX-License-Identifier: Apache-2.0
#
# encoding=utf8

import requests
import os
from urllib.parse import urlparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--slug", help="Umbrella Foundation slug")
args = parser.parse_args()

endpointURL = 'https://api-gw.platform.linuxfoundation.org/project-service/v1/public/projects?$filter=parentSlug%20eq%20{}&pageSize=2000&orderBy=name'

with requests.get(endpointURL.format(args.slug)) as response:
    projectList = response.json()
    for record in projectList['Data']:
        if record.get('CharterURL'):
            if record.get('CharterURL').startswith('https://github.com'):
                record['CharterURL'] = record['CharterURL'].replace("/blob/","/raw/")
            print("Getting file {}...".format(record.get('CharterURL')))
            try:
                with requests.get(record['CharterURL'],stream=False) as contents:
                    root, extension = os.path.splitext(urlparse(record['CharterURL']).path)
                    with open("{}_charter{}".format(record['Slug'],extension), 'wb') as f:
                        print("Writing file {}...".format(f.name))
                        f.write(contents.content)
            except:
                print("Error getting file")
