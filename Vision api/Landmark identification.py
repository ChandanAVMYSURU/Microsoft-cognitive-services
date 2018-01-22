import httplib, urllib, base64, json

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = 'd7da93391f0740f894ae07d2436a9739'

uri_base = 'westcentralus.api.cognitive.microsoft.com'

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.urlencode({
    # Request parameters. Use 'model': 'celebrities' to use the Celebrities model.
    'model': 'celebrities',
})

# The URL of a JPEG image containing a landmark.
body = "{'url':'https://lh3.googleusercontent.com/-h1qGkmP4Xpg/Wdbf9slJsMI/AAAAAAAADPk/kgAkt-B73Yg8w7GrT6fK7mnaj8vcG5SogCHMYCw/s640/rajakumara-image1-22-1498119991.jpg'}"

try:
    # Execute the REST API call and get the response.
    conn = httplib.HTTPSConnection(uri_base)

    # Change "landmarks" to "celebrities" in the url to use the Celebrities model.
    conn.request("POST", "/vision/v1.0/models/landmarks/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()

except Exception as e:
    print('Error:')
    print(e)
