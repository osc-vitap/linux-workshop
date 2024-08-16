FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
		python3 \
    adduser \
    tini \
    vim \
    nano \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos "" appuser
RUN echo "root:admin123" | chpasswd

COPY ./game /home/appuser/

RUN chown -R appuser:appuser /home/appuser
RUN chown root:root /home/appuser/omega/bot

USER appuser

WORKDIR /home/appuser

CMD ["/bin/bash"]

ENTRYPOINT ["/usr/bin/tini", "--"]