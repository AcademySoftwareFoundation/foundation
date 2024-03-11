#!/usr/bin/env python3
#
# Copyright this project and it's contributors
# SPDX-License-Identifier: Apache-2.0
#
# encoding=utf8

from __future__ import print_function
import os.path
import requests

# The ID of a sample document.
documents = [
        {'id':'1NKy7Cdfh60YgDQMQxc3pB5UNM5SUd2kh','mimeType':'application/pdf','filename':'ASWF High Level Overview.pdf'},
        {'id':'1NKy7Cdfh60YgDQMQxc3pB5UNM5SUd2kh','mimeType':'application/vnd.openxmlformats-officedocument.presentationml.presentation','filename':'ASWF High Level Overview.pptx'},
        {'id':'1DymqK796EhxkLIchx7sNxJloovYLGJD8UDkOdkS42to','mimeType':'application/pdf','filename':'ASWF Governing Board Overview.pdf'},
        {'id':'1qY9DPLw4aucqIdqqB1_Pi-qKEyIg2V7q9B96-G1jhqE','mimeType':'application/pdf','filename':'ASWF TAC Overview.pdf'},
        {'id':'1p0FoFJ7-IdDejisJPUYdq_uApn3XW3wJ','mimeType':'application/pdf','filename':'ASWF Membership Overview.pdf'},
        ]

# Retrieve the documents contents from the Docs service.
for document in documents:
    print("Getting file {}...".format(document['filename']))
    try:
        match document['mimeType']:
            case 'application/pdf':
                exportFormat = 'pdf'
            case 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
                exportFormat = 'pptx'
            case _:
                continue
        contents = requests.get('https://docs.google.com/feeds/download/presentations/Export?id={docid}&exportFormat={exportFormat}'.format(docid=document['id'],exportFormat=exportFormat),stream=False)
        with open(document['filename'], 'wb') as f:
            f.write(contents.content)
    except HttpError as err:
        print(err.content)
