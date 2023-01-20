#!/bin/bash
set -e

# run db migrations (retry on error)
while ! /opt/peering-manager/manage.py migrate 2>&1; do
    sleep 5
done

# create superuser silently
# 作成に失敗するので、「sudo docker-compose exec peering-manager bash」より、
# →「python manage.py createsuperuser」を実行
if [[ -z ${SUPERUSER_NAME} || -z ${SUPERUSER_EMAIL} || -z ${SUPERUSER_PASSWORD} ]]; then
        SUPERUSER_NAME='admin'
        SUPERUSER_EMAIL='admin@example.com'
        SUPERUSER_PASSWORD='admin'
        echo "Using defaults: Username: ${SUPERUSER_NAME}, E-Mail: ${SUPERUSER_EMAIL}, Password: ${SUPERUSER_PASSWORD}"
fi
echo "Username: ${SUPERUSER_NAME}, E-Mail: ${SUPERUSER_EMAIL}, Password: ${SUPERUSER_PASSWORD}"
python /opt/peering-manager/manage.py createsuperuser

# copy static files
/opt/peering-manager/manage.py collectstatic --no-input

# start unicorn
gunicorn --log-level debug --error-logfile /dev/stderr --log-file /dev/stdout -c /opt/peering-manager/gunicorn.py peering_manager.wsgi
