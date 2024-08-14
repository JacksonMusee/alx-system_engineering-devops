# Fixing wrong extension of wp-settings.phpp to `wp-settings.php`

exec { 'fix-extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
