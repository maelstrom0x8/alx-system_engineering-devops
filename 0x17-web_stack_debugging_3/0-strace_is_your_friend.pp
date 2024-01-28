# Apply a Puppet manifest to replace 'phpp' with 'php' in /var/www/html/wp-settings.php.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
