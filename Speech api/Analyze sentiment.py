# -*- coding: utf-8 -*-

import httplib, urllib
import json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the accessKey string value with your valid access key.
accessKey = '8f04b043e21c49f0ace423208725a522'
uri = 'westus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/sentiment'

def GetSentiment (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': 'I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable.' },
    { 'id': '2', 'language': 'es', 'text': 'Este ha sido un dia terrible, llegué tarde al trabajo debido a un accidente automobilistico.' }
]}

print 'Please wait a moment for the results to appear.\n'

result = GetSentiment (documents)
print (json.dumps(json.loads(result), indent=4))