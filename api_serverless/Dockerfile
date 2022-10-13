# Starting from an official AWS image
# Keep any dependencies and versions in this file aligned with the environment.yml and Makefile
FROM public.ecr.aws/lambda/python:3.7

# Install Python dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip==22.1.2
RUN yum update -y
RUN yum install -y glibc-static libstdc++-static
RUN yum install -y gcc gcc-c++
RUN yum install -y bzip2
RUN yum install -y wget
RUN yum install -y libarchive
RUN wget http://packages.eu-central-1.amazonaws.com/2018.03/main/c31535f74c6e/x86_64/Packages/cmake-2.8.12.2-4.25.amzn1.x86_64.rpm
RUN rpm -ivh cmake-2.8.12.2-4.25.amzn1.x86_64.rpm
RUN pip install -U pip wheel cmake
RUN pip install -r requirements.txt

# Copy only the relevant directories and files
#   note that we use a .dockerignore file to avoid copying logs etc.
COPY emotion_synthesizer/ ./emotion_synthesizer
COPY api_serverless/api.py ./api.py

CMD ["api.handler"]