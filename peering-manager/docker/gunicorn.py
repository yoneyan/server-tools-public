command = '/usr/local/bin/gunicorn'
pythonpath = '/opt/peering-manager'
bind = '0.0.0.0:8001'
workers = 5
threads = 3
timeout = 300
max_requests = 5000
max_requests_jitter = 500
# user = 'root'
loglevel = 'debug'