# Configuration for SSH Client

file { '/etc/ssh/ssh_config':
  ensure  => present,
  mode    => '0644',
  content => "\
Host alx
  HostName 100.25.160.191
  User ubuntu
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
}
