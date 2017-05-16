FROM alpine:3.5

COPY game /game

RUN apk --update add openssh bash \
  && adduser -S -h /game/ -s /bin/bash -g "" bash \
  && echo "bash:bash" | chpasswd \
  && rm /bin/cat /bin/grep /usr/bin/vi /usr/bin/less \
  && ssh-keygen -A

COPY motd /etc/motd

CMD ["bash", "-c", "exec /usr/sbin/sshd -D -e \"$@\""]

