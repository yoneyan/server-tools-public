FROM python:3.9.8-buster

WORKDIR /opt/peering-manager

ARG BRANCH=v1.7.3
# ARG BRANCH=v1.6.1
ARG URL=https://github.com/peering-manager/peering-manager.git
RUN git clone --depth 1 $URL -b $BRANCH .  && \
    apt-get update -qq && apt-get install -y python3-dev libldap2-dev libsasl2-dev libssl-dev graphviz bgpq3 libldap-2.4.2 && \
	pip3 install -r requirements.txt && \
    pip3 install django-auth-ldap && \
    pip3 install django-radius && \
    pip3 install gunicorn

ADD docker/docker-entrypoint.sh /docker-entrypoint.sh
ADD docker/configuration.py /opt/peering-manager/peering_manager/configuration.py
ADD docker/ldap_config.py /opt/peering-manager/peering_manager/ldap_config.py
RUN chmod 755 /docker-entrypoint.sh
ADD docker/gunicorn.py /opt/peering-manager/gunicorn.py

ENTRYPOINT [ "/docker-entrypoint.sh" ]

RUN mkdir static && chmod -R g+w static

ADD docker/nginx.conf /etc/peering-manager-nginx/nginx.conf
VOLUME ["/etc/peering-manager-nginx/"]
