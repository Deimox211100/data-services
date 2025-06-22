FROM jupyterhub/jupyterhub:latest

USER root

# Recibe usuario y contraseña como argumentos
ARG JUPYTERHUB_USER
ARG JUPYTERHUB_PASS

# Instala lo necesario
RUN apt-get update && \
    apt-get install -y git python3-pip sudo && \
    pip install notebook

# Crea el usuario dinámicamente
RUN useradd -m -s /bin/bash $JUPYTERHUB_USER && \
    echo "$JUPYTERHUB_USER:$JUPYTERHUB_PASS" | chpasswd && \
    adduser $JUPYTERHUB_USER sudo

# Copia config
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

CMD ["jupyterhub", "--ip", "0.0.0.0", "--port", "8000"]