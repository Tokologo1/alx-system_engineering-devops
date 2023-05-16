#Correct the amount of failed request.

exec { 'fix--for-nginx':
  command => "sed -i 's/worker_processess 4;/worker_processess 7;/g' /ect/nginx/nginx.conf; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}  
