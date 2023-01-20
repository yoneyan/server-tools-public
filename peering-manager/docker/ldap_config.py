import ldap
from os import environ
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

AUTH_LDAP_SERVER_URI = environ.get('AUTH_LDAP_SERVER_URI', '')

AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}

AUTH_LDAP_BIND_DN = environ.get('AUTH_LDAP_BIND_DN', '')
AUTH_LDAP_BIND_PASSWORD = environ.get('AUTH_LDAP_BIND_PASSWORD', '')

LDAP_IGNORE_CERT_ERRORS = True

AUTH_LDAP_USER_SEARCH_BASEDN = environ.get('AUTH_LDAP_USER_SEARCH_BASEDN', '')
AUTH_LDAP_USER_SEARCH_ATTR = environ.get('AUTH_LDAP_USER_SEARCH_ATTR', 'sAMAccountName')
AUTH_LDAP_USER_SEARCH = LDAPSearch(AUTH_LDAP_USER_SEARCH_BASEDN,
                                    ldap.SCOPE_SUBTREE,
                                   "(" + AUTH_LDAP_USER_SEARCH_ATTR + "=%(user)s)")

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": environ.get('AUTH_LDAP_ATTR_FIRSTNAME', 'givenName'),
    "last_name": environ.get('AUTH_LDAP_ATTR_LASTNAME', 'sn'),
    "email": environ.get('AUTH_LDAP_ATTR_MAIL', 'mail')
}

AUTH_LDAP_GROUP_SEARCH_BASEDN = environ.get('AUTH_LDAP_GROUP_SEARCH_BASEDN', '')
AUTH_LDAP_GROUP_SEARCH_CLASS = environ.get('AUTH_LDAP_GROUP_SEARCH_CLASS', 'group')
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(AUTH_LDAP_GROUP_SEARCH_BASEDN, ldap.SCOPE_SUBTREE,
                                    "(objectClass=" + AUTH_LDAP_GROUP_SEARCH_CLASS + ")")
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

AUTH_LDAP_REQUIRE_GROUP = environ.get('AUTH_LDAP_REQUIRE_GROUP_DN')

if AUTH_LDAP_REQUIRE_GROUP is not None:
    AUTH_LDAP_USER_FLAGS_BY_GROUP = {
        "is_active": environ.get('AUTH_LDAP_REQUIRE_GROUP_DN', ''),
        "is_staff": environ.get('AUTH_LDAP_IS_ADMIN_DN', ''),
        "is_superuser": environ.get('AUTH_LDAP_IS_SUPERUSER_DN', '')
    }

# Map LDAP groups to Django groups
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache for an hour
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600
