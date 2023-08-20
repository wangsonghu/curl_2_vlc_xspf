FROM harbor.hosts.songhu.wang:8443/apps/python:alpine3.6_v2023-08-20

WORKDIR /work

COPY requirements.txt curl_list.py list.j2 ./
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "curl_list.py"]
CMD ["https://web-server.hosts.songhu.wang/study/%5B1.%5D%5Bipv6%5D/"]
