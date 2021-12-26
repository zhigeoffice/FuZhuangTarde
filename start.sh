#！ /bin/bash
source /home/ubuntu/env/fuZhuangTarde/bin/activate
gunicorn -c gunicorn.conf.py app_run:app