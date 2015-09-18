FROM python:wheezy

RUN mkdir -p /srv/resumator
COPY ./ /srv/resumator/
RUN pip install -r /srv/resumator/requirements.txt

CMD gunicorn --pythonpath /srv/resumator --bind 0.0.0.0 --log-level info --log-file - --access-logfile - manage:app
