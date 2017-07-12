FROM pypy:2
MAINTAINER Yu Yuan
RUN apt-get update && apt-get install -y --no-install-recommends \
		net-tools \
	&& rm -rf /var/lib/apt/lists/*
ENV APP_ROOT /code
WORKDIR ${APP_ROOT}
EXPOSE 5000
COPY . ${APP_ROOT}/
RUN pip install --no-cache-dir --trusted-host 10.46.175.61 -i http://10.46.175.61:8080/simple -r requirements.txt

