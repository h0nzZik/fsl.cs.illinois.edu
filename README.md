This directory is used to build the FSL static website.

# Installation (using Docker)

1. Install the `build-essential` package. 

```
$ sudo apt update
$ sudo apt install build-essential ruby-bundler ruby-dev
```

2. Install Docker following https://docs.docker.com/engine/install/ubuntu/.

3. Make Docker work with non-root users following https://docs.docker.com/engine/install/linux-postinstall/. 

# Build (using Docker)

On your first build, run `./build-in-docker image` to create the Docker image. 

To build the website locally, run `./build-in-docker.sh serve`. If you see the following messages then the build is succesful:

```
 [ ... MORE MESSAGES ... ]
 Auto-regeneration: enabled for '/mnt/fsl/www/fsl.cs.illinois.edu'
    Server address: http://0.0.0.0:4000/fsl//
  Server running... press ctrl-c to stop.
```

You can access the website by visiting the server address http://0.0.0.0:4000/fsl// in a web browser. 

# Publish the Website

**Warning: Make sure the website is functioning before pushlishing it.**

Firstly, make sure that you have the branch `gh-pages` checked out in your local repository.

```
$ git checkout gh-pages
$ git checkout master
```

Following these steps to publish the website. 

1. Run `./update-gh-pages`, which generates the HTML files and pushes them to the branch `gh-pages` where the website is hosted. 

2. Checkout `gh-pages` branch by running `git checkout gh-pages`. 

3. Manually push the commit to the remote by running `git push`. 

4. Don't forget to return to the `master` branch by running `git checkout master`, which will take a while to finish.

# Troubleshooting

1. Run `./build-in-docker.sh serve` and get the following error message (or something similar)

```
Traceback (most recent call last):
  File "./bibtex2wiki/bibtex2wiki", line 64, in <module>
    with open('_papers/' + paper.id + '.md', 'w') as f:
IOError: [Errno 2] No such file or directory: '_papers/rosu-stefanescu-2012-oopsla.md'
```

**Solution**. Create an empty directory `fsl.cs.illinois.edu/_papers`. 


