# non logging stuff
bind = "0.0.0.0:5003"
#number of workers to spawn
workers = 3
#access log-reports incoming  HTTP requests
accesslog = "/tmp/airbnb-access.log"
#error log - records any error
errorlog = "/tmp/airbnb-error.log"
#whether to send flask output to the error log
capture_output = True
#verbosity of gunicorn error logs
loglevel = "info"
