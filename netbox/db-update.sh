POSTGRES_USER="netbox"
POSTGRES_PASSWORD="PASSWORD"
USER_NAME="USERNAME"
OLD=9.6
NEW=14
OLD_DATA="/home/$USER_NAME/netbox/data/postgres-data"
NEW_DATA="/home/$USER_NAME/netbox/data/postgres-data-new"

sudo docker run --rm \
-e PGUSER="$POSTGRES_USER" \
-e POSTGRES_INITDB_ARGS="-U $POSTGRES_USER" \
-e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" \
-v "$OLD_DATA":"/var/lib/postgresql/$OLD/data" \
-v "$NEW_DATA":"/var/lib/postgresql/$NEW/data" \
"tianon/postgres-upgrade:$OLD-to-$NEW"
