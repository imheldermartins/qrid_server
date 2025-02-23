import os

def get_secret(secret_id, backup=None):
    """get secret_env from .envfile"""
    return os.getenv(secret_id, backup)

if get_secret('PIPELINE') == 'production':
    from .production import *
else:
    from .local import *