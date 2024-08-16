FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    adduser \
    tini \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos "" appuser

USER appuser

WORKDIR /home/appuser

CMD ["/bin/bash"]

ENTRYPOINT ["/usr/bin/tini", "--"]