#Kills a process named killmenow

exec { 'killmenow':
    command     => '/usr/bin/pkill killmenow',
    refreshonly => true,
    onlyif      => '/usr/bin/pgrep killmenow'
}
