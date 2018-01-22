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
    # Request parameters. The smartCropping flag is optional.
    'width': '150',
    'height': '100',
    'smartCropping': 'true',
})

# The URL of a JPEG image to use to create a thumbnail image.
body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/9/94/Bloodhound_Puppy.jpg'}"

try:
    # Execute the REST API call and get the response.
    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/generateThumbnail?%s" % params, body, headers)
    response = conn.getresponse()

    # Check for success.
    if response.status == 200:
        # Success. Use 'response.read()' to return the image data. 
        # Display the response headers.
        print ('Success.')
        print ('Response headers:')
        headers = response.getheaders()
        for field, value in headers:
            print ('  ' + field + ': ' + value)
    else:
        # Error. 'data' contains the JSON error data. Display the error data.
        data = response.read()
        parsed = json.loads(data)
        print ('Error:')
        print (json.dumps(parsed, sort_keys=True, indent=2))

    conn.close()

except Exception as e:
    print('Error:')
    print(e)

####################################