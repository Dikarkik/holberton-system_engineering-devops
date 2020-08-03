# 2. Execute a command
exec { 'killmenow':
    path     => '/usr/bin',
    provider => 'shell',
    command  => 'pkill -f ./killmenow',
}
