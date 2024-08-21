#Solve too many files error
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
