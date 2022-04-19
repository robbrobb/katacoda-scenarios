version: "2"
services:
  grafana:
    image: grafana/grafana
    container_name: grafana
    restart: always
    ports:
      - 3000:3000
    networks:
      - monitoring
    volumes:
      - grafana-volume:/containerhome/grafana
  influxdb:
    image: influxdb
    container_name: influxdb
    restart: always
    ports:
      - 8086:8086
    networks:
      - monitoring
    volumes:
      - influxdb-volume:/containerhome/influxdb
    environment:
      - INFLUXDB_DB=home
      - INFLUXDB_USER=admin
      - INFLUXDB_ADMIN_ENABLED=true

      - INFLUXDB_ADMIN_USER=admin
      - INFLUXDB_ADMIN_PASSWORD=password 
  telegraf:
    image: telegraf
    container_name: telegraf
    restart: always
    extra_hosts:
     - "influxdb:192.168.178.54"
    environment:
      HOST_PROC: /rootfs/proc
      HOST_SYS: /rootfs/sys
      HOST_ETC: /rootfs/etc
    volumes:
     - ./telegraf.conf:/etc/telegraf/telegraf.conf:ro
     - /var/run/docker.sock:/var/run/docker.sock:ro
     - /sys:/rootfs/sys:ro
     - /proc:/rootfs/proc:ro
     - /etc:/rootfs/etc:ro
networks:
  monitoring:
volumes:
  grafana-volume:
    external: true
  influxdb-volume:
    external: true
