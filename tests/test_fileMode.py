#1/usr/bin/env python

from os import stat as os_stat
import stat
import re

file_stats = os_stat('crontabs/var/spool/cron/root/test_1')
octal_re = re.compile('^0o{0,1}')
octal = octal_re.sub('', oct( stat.S_IMODE(file_stats.st_mode) )).zfill(4)

print( octal )

#st_mode=33188

