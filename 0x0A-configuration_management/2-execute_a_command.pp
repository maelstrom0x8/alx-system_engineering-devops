# Kill process with name 'killmenow'

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
