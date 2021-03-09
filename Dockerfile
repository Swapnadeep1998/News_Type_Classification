FROM continuumio/miniconda3
COPY . /app
WORKDIR /app
RUN conda env create -f environment.yml --force
SHELL ["conda", "run", "-n", "news_classification", "/bin/bash", "-c"]
RUN python -c "import tensorflow as tf"
EXPOSE 8000
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "news_classification", "python", "app.py"]
