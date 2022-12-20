# OS
ARG VARIANT=bullseye
FROM --platform=linux/amd64 mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

# Desktop lite
COPY library-scripts/desktop-lite-debian.sh /tmp/library-scripts/
COPY fluxbox /home/vscode/.fluxbox/
RUN apt-get update \
    && bash /tmp/library-scripts/desktop-lite-debian.sh \
    && chown -R vscode /home/vscode
ENV DBUS_SESSION_BUS_ADDRESS="autolaunch:" \
    VNC_RESOLUTION="1440x768x16" \
    VNC_DPI="96" \
    VNC_PORT="5901" \
    NOVNC_PORT="6080" \
    DISPLAY=":1" \
    LANG="en_US.UTF-8" \
    LANGUAGE="en_US.UTF-8"
ENTRYPOINT ["/usr/local/share/desktop-init.sh"]
CMD ["sleep", "infinity"]