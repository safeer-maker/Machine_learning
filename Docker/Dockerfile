FROM ubuntu

ARG WORKDIR=/root/ml

# ENV MODEL_PATH      = $WORKDIR/models
# ENV PATH_OF_DATASET = $WORKDIR/data


RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

COPY ml_files /root/ml

WORKDIR $WORKDIR

RUN pip3 install -r  requirements.txt --break-system-packages

# CMD ["python3", "model_training_inferancing.py"]
