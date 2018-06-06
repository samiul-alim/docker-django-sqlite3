FROM python:3.5-slim
ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
RUN mkdir -p /var/log/platform_admin
COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
