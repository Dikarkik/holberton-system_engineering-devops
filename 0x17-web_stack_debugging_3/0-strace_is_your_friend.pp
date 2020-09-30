# Fix typo on file /var/www/html/wp-settings.php line 137
exec { 'fix typo':
  onlyif  => 'test -e /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
