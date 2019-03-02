import multiprocessing
num_workers = multiprocessing.cpu_count() * 2 + 1
command = '/usr/local/bin/gunicorn'
pythonpath = '/var/www/fcp'
bind = '0.0.0.0:8000'
workers = num_workers
timeout = 120
