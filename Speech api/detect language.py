# -*- coding: utf-8 -*-

import httplib, urllib
import json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the accessKey string value with your valid access key.
accessKey = 'eb32efc49b7f48a78180fbdc06d317d6'
uri = 'westus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/languages'

def GetLanguage (documents):
    "Detects the languages for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

documents = { 'documents': [
    { 'id': '1', 'text': 'This is a document written in English.' },
    { 'id': '2', 'text': 'Este es un document escrito en Español.' },
    { 'id': '3', 'text': '这是一个用中文写的文件' }
]}

print 'Please wait a moment for the results to appear.\n'

result = GetLanguage (documents)
print (json.dumps(json.loads(result), indent=4))