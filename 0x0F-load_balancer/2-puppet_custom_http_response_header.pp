# Install NGINX and add a custom header

exec {'update':
  provider => shell,
  command  => 'sudo apt update -y',
  before   => Exec['install Nginx'],
}

exec {'install nginx':
  provider => shell,
  command  => 'sudo apt install nginx -y',
}

exec { 'header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header \
  X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
}

exec { 'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
