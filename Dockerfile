FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
		python3 \
    adduser \
    tini \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos "" appuser
RUN echo "root:admin123" | chpasswd

USER appuser

WORKDIR /home/appuser

COPY ./game /home/appuser/

CMD ["/bin/bash"]

ENTRYPOINT ["/usr/bin/tini", "--"]