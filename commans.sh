# shellcheck disable=SC1073

[ Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[ Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/project/Job_Portal
ExecStart=/home/ubuntu/project/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          job_portal.wsgi:application

[ Install]
WantedBy=multi-user.target