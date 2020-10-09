# Update limit of open files for user 'holberton'
exec { 'update hard nofile limit':
  onlyif  => 'test -e /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 693000/' /etc/security/limits.conf",
}

exec { 'update soft nofile limit':
  onlyif  => 'test -e /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/holberton soft nofile 4/holberton soft nofile 693999/' /etc/security/limits.conf",
}
