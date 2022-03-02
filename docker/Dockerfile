# USING ALPINE AS BASE
#
# BUILD AND RUN INSTRUCTIONS
#   docker build -f Dockerfile -t knowledge_seeker:staging .
#   docker run -it -p 5000:5000 -v <PATH_TO_KS_PROJECT>:/app --name knowledge_seeker knowledge_seeker:staging
#   docker start ansible29
#   docker attach ansible29

FROM alpine:3.15.0
LABEL maintainer="Liz Sugar <liz@lizsugar.me>"
EXPOSE 5000

#ARG USER=seeker

# INSTALL REQUISITE OS PACKAGES
RUN apk add py3-pip

# KNOWLEDGE SEEKER SET UP
# cd /app
# pip install .

# BUILD DATABASE
# FLASK_APP=knowledgeseeker flask read-library

# RUN DEV MODE
# FLASK_APP=knowledgeseeker FLASK_ENV=development flask run

# test
#RUN ls
CMD ["ash"]