from os import getenv

user = getenv("JUPYTERHUB_USER", "deimox")

c = get_config()
c.JupyterHub.bind_url = 'http://:8000'
c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'

c.Authenticator.allowed_users = {user}
c.Authenticator.admin_users = {user}

c.Spawner.http_timeout = 60