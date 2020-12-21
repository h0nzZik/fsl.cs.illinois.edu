FROM jekyll/jekyll

RUN apk add --no-cache python2 py2-pip
RUN pip2 install pyyaml
