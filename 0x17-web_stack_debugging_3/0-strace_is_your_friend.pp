# Fix 500 error when a GET HTTP method is required to Apache web Server

exec { 'sed':
	command => 'sed -i "s|.phpp|.php|" /var/www/html/wp-settings.php',
	path 	=> '/bin/
}
