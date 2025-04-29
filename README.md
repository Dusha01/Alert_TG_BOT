# =================================================
# Настройка prometheuse && node exporter

1. Создание пользователя для Prometheus (опционально)
Рекомендуется запускать Prometheus под отдельным пользователем:

sudo useradd --no-create-home --shell /bin/false prometheus



2. Создание директорий для конфигурации и данных

sudo mkdir /etc/prometheus
sudo mkdir /var/lib/prometheus
sudo chown prometheus:prometheus /var/lib/prometheus



3. Загрузка и установка Prometheus
Скачивание последней версии
Найдите актуальную версию на официальном сайте, затем загрузите:

wget https://github.com/prometheus/prometheus/releases/download/v2.47.0/prometheus-2.47.0.linux-amd64.tar.gz


tar xvf prometheus-*.tar.gz
cd prometheus-*/
sudo mv prometheus promtool /usr/local/bin/
sudo mv consoles/ console_libraries/ /etc/prometheus/
sudo mv prometheus.yml /etc/prometheus/


4. Настройка конфигурации
Отредактируйте файл конфигурации:


sudo nano /etc/prometheus/prometheus.yml
Пример минимальной конфигурации:

yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']



5. Настройка сервиса для автоматического запуска
Создайте файл сервиса:


sudo nano /etc/systemd/system/prometheus.service
Добавьте конфигурацию:

ini
[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus \
    --config.file /etc/prometheus/prometheus.yml \
    --storage.tsdb.path /var/lib/prometheus/ \
    --web.console.templates=/etc/prometheus/consoles \
    --web.console.libraries=/etc/prometheus/console_libraries

[Install]
WantedBy=multi-user.target

Затем выполните:


sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl enable prometheus

6. Проверка работы
sudo systemctl status prometheus


7. Скачивание и распаковка
Найдите последнюю версию на официальной странице релизов и выполните:


wget https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz

Распакуйте архив:

tar xvf node_exporter-*.tar.gz
cd node_exporter-*/

Копирование бинарника в /usr/local/bin

sudo cp node_exporter /usr/local/bin/
sudo chown prometheus:prometheus /usr/local/bin/node_exporter



8. Настройка сервиса для автоматического запуска
Создайте файл сервиса:


sudo nano /etc/systemd/system/node_exporter.service
Добавьте конфигурацию:

ini
[Unit]
Description=Node Exporter
After=network.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
Затем:

bash
sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl enable node_exporter
Проверка работы
bash
sudo systemctl status node_exporter

Если всё работает, в логах будет:

level=info msg="Listening on :9100" source="node_exporter.go:111"

Проверить метрики можно вручную:


curl http://localhost:9100/metrics
3. Настройка Prometheus для сбора метрик с Node Exporter
Отредактируйте конфигурацию Prometheus:


sudo nano /etc/prometheus/prometheus.yml
Добавьте новый job в секцию scrape_configs:

yaml
scrape_configs:
  - job_name: 'node_exporter'
    static_configs:
      - targets: ['localhost:9100']

(Если Node Exporter работает на другом сервере, укажите его IP вместо localhost.)

sudo systemctl restart prometheus