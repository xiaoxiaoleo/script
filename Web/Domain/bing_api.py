import urllib2, socket,sys,base64
from xml.dom.minidom import parse, parseString


def showhelp():
        print """------------"""
 

def bing(account_key,ip):
    sites = []
    skip = 0
    top = 50

    while skip < 200:
          url = "https://api.datamarket.azure.com/Data.ashx/Bing/Search/v1/Web?Query='ip:%s'&$top=%s&$skip=%s&$format=Atom"%(ip,top,skip)
          request = urllib2.Request(url)
          auth = base64.encodestring("%s:%s" % (account_key, account_key)).replace("\n", "")
          request.add_header("Authorization", "Basic %s" % auth)
          res = urllib2.urlopen(request)
          data = res.read()

          xmldoc = parseString(data)
          site_list = xmldoc.getElementsByTagName('d:Url')
          for site in site_list:
              domain = site.childNodes[0].nodeValue
              domain = domain.split("/")[2]
              if domain not in sites:
                 sites.append(domain)

          skip += 50
    #print "######################################"
    print "%s : %s" %(ip,len(sites))
    for site in sites:
        print '    '+site
	return sites
    #print "######################################"


def options(arguments):
   try:
    count = 0
    ip = ""
    account_key = "gQxNd7GPn2yASnBDHWJqRZWe5cKrlqo257yf/LdKOII"
    for arg in arguments:
        if arg == "-ip":
           ip = arguments[count+1]
        elif arg == "-domain":
           ip = socket.gethostbyname(arguments[count+1])
        elif arg == "-key":
           account_key = arguments[count+1]
        count = count+1
    bing(account_key,ip)
   except:
    print "something went wrong"

if __name__ == "__main__":
   if len(sys.argv) <= 3 or "-key" not in sys.argv:
      showhelp()
      bing("gQxNd7GPn2yASnBDHWJqRZWe5cKrlqo257yf/",'x.x.x.x')
      sys.exit()
   else:
      options(sys.argv)
