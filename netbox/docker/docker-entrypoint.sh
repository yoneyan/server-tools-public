#!/bin/bash
set -e

# run db migrations (retry on error)
while ! /opt/netbox/netbox/manage.py migrate 2>&1; do
    sleep 5
done

# delete ldap configuration if AUTH_LDAP_SERVER_URL is not defined
if [[ -z "${AUTH_LDAP_SERVER_URI}" ]]; then
	rm /opt/netbox/netbox/ldap_config.py
fi

# create superuser silently
if [[ -z ${DJANGO_SUPERUSER_NAME} || -z ${DJANGO_SUPERUSER_EMAIL} || -z ${DJANGO_SUPERUSER_PASSWORD} ]]; then
        DJANGO_SUPERUSER_NAME='admin'
        DJANGO_SUPERUSER_EMAIL='admin@example.com'
        DJANGO_SUPERUSER_PASSWORD='admin'
        echo "Using defaults: Username: ${DJANGO_SUPERUSER_NAME}, E-Mail: ${DJANGO_SUPERUSER_EMAIL}, Password: ${DJANGO_SUPERUSER_PASSWORD}"
fi
echo "Username: ${DJANGO_SUPERUSER_NAME}, E-Mail: ${DJANGO_SUPERUSER_EMAIL}, Password: ${DJANGO_SUPERUSER_PASSWORD}"
python /opt/netbox/netbox/manage.py createsuperuser

#echo "from django.contrib.auth.models import User; User.objects.create_superuser('${SUPERUSER_NAME}', '${SUPERUSER_EMAIL}', '${SUPERUSER_PASSWORD}')" | python /opt/netbox/netbox/manage.py shell
#python netbox/manage.py shell --plain << END
#from django.contrib.auth.models import User
#if not User.objects.filter(username='${SUPERUSER_NAME}'):
#    User.objects.create_superuser('${SUPERUSER_NAME}', '${SUPERUSER_EMAIL}', '${SUPERUSER_PASSWORD}')
#END

# copy static files
/opt/netbox/netbox/manage.py collectstatic --no-input

# start unicorn
#gunicorn --log-level debug --debug --error-logfile /dev/stderr --log-file /dev/stdout -c /opt/netbox/gunicorn_config.py netbox.wsgi
gunicorn --log-level debug --error-logfile /dev/stderr --log-file /dev/stdout -c /opt/netbox/gunicorn_config.py netbox.wsgi