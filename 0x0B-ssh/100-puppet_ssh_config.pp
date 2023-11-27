# Configuration for SSH Client

file { '/etc/ssh/ssh_config':
  ensure  => present,
  mode    => '0644',
  content => "\
Host alx
  HostName 52.203.135.95
  User ubuntu
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
}
