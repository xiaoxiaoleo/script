from urllib import request
import re
import http.client

urllist=[]
def Readurl(filename,listurl):
    f = open(filename)
    for line in f:
        line = line.split('\n')
        #print(line[0])
        listurl.append(line[0])
        
        #Judges(line[0])
    f.close()
    print(listurl)

def Judges(url,test):
    
    if 'http:' in url:
        pass
    else:
        url='http://'+url
    print(url)
    try:
        r = request.urlopen(url)
        bytecode = r.read()
        htmlstr = bytecode.decode()
        if test in htmlstr:
            return 1
        else:
            return 0
    except:
        return 0

def getResponseCode(url,xx):
    if 'http:' in url:
        url= url[7:]
    print(url)
        
    conn = http.client.HTTPConnection(url,80,timeout=10)
    
    try:
        conn.request("GET", xx)
        r1 = conn.getresponse()
        if r1.status==200:
            return 1
        else:
            return 0
    except:
        return 0

    
    


#Judges('http://baidu.com','test')
Readurl('url.txt',urllist)


for i in urllist:
    if(Judges(i,'WordPress') or Judges(i+'/robots.txt','wp') or getResponseCode(i,'\wp-login.php')  or getResponseCode(i,'\wp-login.php')):
        print('wordpress'+i)
    else:
        print(i)
