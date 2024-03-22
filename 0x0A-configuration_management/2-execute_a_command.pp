#Kills a process named killmenow

exec { 'killmenow':
    command     => 'pkill killmenow',
    refreshonly => true,
    onlyif      => 'pgrep killmenow'
}
