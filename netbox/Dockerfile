FROM python:3.9.8-buster

WORKDIR /opt/netbox

ARG BRANCH=v3.4.10
#ARG BRANCH=v2.11.12
ARG URL=https://github.com/digitalocean/netbox.git
RUN git clone --depth 1 $URL -b $BRANCH .  && \
    apt-get update -qq && apt-get install -y libldap2-dev libsasl2-dev libssl-dev graphviz && \
	pip3 install django-auth-ldap && \
    pip3 install -r requirements.txt

ADD docker/docker-entrypoint.sh /docker-entrypoint.sh
# ADD netbox/netbox/configuration.docker.py /opt/netbox/netbox/netbox/configuration.py
ADD docker/configuration.py /opt/netbox/netbox/netbox/configuration.py
ADD docker/ldap_config.py /opt/netbox/netbox/netbox/ldap_config.py

ENTRYPOINT [ "/docker-entrypoint.sh" ]

ADD docker/gunicorn_config.py /opt/netbox/
ADD docker/nginx.conf /etc/netbox-nginx/
VOLUME ["/etc/netbox-nginx/"]
