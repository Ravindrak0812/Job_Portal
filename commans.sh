# shellcheck disable=SC1073
# shellcheck disable=SC1035
# shellcheck disable=SC1072
# shellcheck disable=SC1020
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/project/Job_Portal
ExecStart=/home/ubuntu/project/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          job_portal.wsgi:application

 [Install]
WantedBy=multi-user.target