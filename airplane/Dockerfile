FROM python:3.6-alpine

COPY app /app

RUN apk --update add openssh bash \
  && rm -rf /var/cache/apk/* \
  && adduser -S -h /app/ -g "" -s /app/app.py game \
  && bash -c "echo \"game:hardtosolve\" | chpasswd" \
  && ssh-keygen -A

WORKDIR /app

CMD ["/bin/bash", "-c", "/usr/sbin/sshd -D -e \"$@\""]
