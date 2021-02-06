FROM jekyll/jekyll

RUN apk add --no-cache python2 py2-pip
RUN pip2 install pyyaml

# Pre-install Gemfile dependencies to save time
COPY ./fsl.cs.illinois.edu/Gemfile      /tmp/default_gems/Gemfile
COPY ./fsl.cs.illinois.edu/Gemfile.lock /tmp/default_gems/Gemfile.lock
RUN chmod o+rw /tmp/default_gems/Gemfile*
RUN ls -l /github/workspace/www/fsl.cs.illinois.edu/
RUN cd /tmp/default_gems/ && bundle install
