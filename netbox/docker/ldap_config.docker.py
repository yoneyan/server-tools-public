import os
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

AUTH_LDAP_SERVER_URI = os.environ.get('AUTH_LDAP_SERVER_URI' , "ldaps://ad.example.com")

AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}

AUTH_LDAP_BIND_DN = os.environ.get('AUTH_LDAP_BIND_DN', "CN=NETBOXSA, OU=Service Accounts,DC=example,DC=com")
AUTH_LDAP_BIND_PASSWORD = os.environ.get('AUTH_LDAP_BIND_PASSWORD', "demo")

LDAP_IGNORE_CERT_ERRORS = os.environ.get('LDAP_IGNORE_CERT_ERRORS', True)

AUTH_LDAP_USER_SEARCH = LDAPSearch(os.environ.get('AUTH_LDAP_USER_SEARCH_BASE', "ou=Users,dc=example,dc=com"),
                                    ldap.SCOPE_SUBTREE,
                                    "(sAMAccountName=%(user)s)")

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": os.environ.get('AUTH_LDAP_USER_ATTR_MAP_FIRST_NAME', "givenName"),
    "last_name": os.environ.get('AUTH_LDAP_USER_ATTR_MAP_LAST_NAME', "sn"),
    "email": os.environ.get('AUTH_LDAP_USER_ATR_MAP_EMAIL', "mail")
}

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(os.environ.get('AUTH_LDAP_GROUP_SEARCH_BASE', "dc=example,dc=com"), ldap.SCOPE_SUBTREE, "(objectClass=group)")
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

AUTH_LDAP_REQUIRE_GROUP = os.environ.get('AUTH_LDAP_REQUIRE_GROUP', "CN=NETBOX_USERS,DC=example,DC=com")

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": os.environ.get('AUTH_LDAP_USER_FLAGS_BY_GROUP_ACTIVE', "cn=active,ou=groups,dc=example,dc=com"),
    "is_staff": os.environ.get('AUTH_LDAP_USER_FLAGS_BY_GROUP_STAFF', "cn=staff,ou=groups,dc=example,dc=com"),
    "is_superuser": os.environ.get('AUTH_LDAP_USER_FLAGS_BY_GROUP_SUPERUSER',"cn=superuser,ou=groups,dc=example,dc=com")
}

AUTH_LDAP_FIND_GROUP_PERMS = os.environ.get('AUTH_LDAP_FIND_GROUP_PERMS', True)

AUTH_LDAP_CACHE_GROUPS = os.environ.get('AUTH_LDAP_CACHE_GROUPS', True)
AUTH_LDAP_GROUP_CACHE_TIMEOUT = os.environ.get('AUTH_LDAP_GROUP_CACHE_TIMEOUT', 3600)
