FROM ubuntu:20.04 as base_container

RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install ipykernel
RUN pip3 install jupyter

WORKDIR /app
ADD . /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
