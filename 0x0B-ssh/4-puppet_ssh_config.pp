# 4. Client configuration file (w/ Puppet)
# make changes to our configuration file
# configured to use the private key ~/.ssh/holberton
# configured to refuse to authenticate using a password

file_line { 'conf PasswordAuthentication':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => '^PasswordAuthentication'
}

file_line { 'conf IdentityFile' :
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/holberton',
    match  => '^IdentityFile',
}
