########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '6bfeaccedcd744aa833f673018afb3aa',
}

params = urllib.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = "{ 'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTq8gZbctL5MnZZTGCXOJsOoYnsxnYViNbKQ9K40Hx6TdaU6RJs' }"

try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
    #   URL below with "westcentralus".
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()
    l = list()
    for i in parsed[0]["scores"].values():
        l.append(i)
    l.sort(reverse=True)
    for key,value in parsed[0]["scores"].iteritems():
        if value == l[0]:
            print key
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
