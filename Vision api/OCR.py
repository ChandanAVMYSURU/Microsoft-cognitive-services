########### Python 2.7 #############
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
    # Request parameters. The language setting "unk" means automatically detect the language.
    'language': 'unk',
    'detectOrientation ': 'true',
})

# The URL of a JPEG image containing text.
body = "{'url':'https://www.brainyquote.com/photos_tr/en/j/johnray/119945/johnray1-2x.jpg'}"

try:
    # Execute the REST API call and get the response.
    conn = httplib.HTTPSConnection(uri_base)
    conn.request("POST", "/vision/v1.0/ocr?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()
    for i in parsed["regions"][0]["lines"]:
        for j in i["words"]:
            print j["text"],
        print " "
except Exception as e:
    print('Error:')
    print(e)

####################################