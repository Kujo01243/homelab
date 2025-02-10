from os import environ

#############
# Docker
#############

# python-social-auth configuration
REMOTE_AUTH_ENABLED='true'
REMOTE_AUTH_BACKEND='social_core.backends.open_id_connect.OpenIdConnectAuth'
SOCIAL_AUTH_OIDC_ENDPOINT = environ.get('SOCIAL_AUTH_OIDC_ENDPOINT')
SOCIAL_AUTH_OIDC_KEY = environ.get('SOCIAL_AUTH_OIDC_KEY')
SOCIAL_AUTH_OIDC_SECRET = environ.get('SOCIAL_AUTH_OIDC_SECRET')
SOCIAL_AUTH_OIDC_SCOPE = ["openid", "profile", "email", "roles"]
LOGOUT_REDIRECT_URL = environ.get('LOGOUT_REDIRECT_URL')
