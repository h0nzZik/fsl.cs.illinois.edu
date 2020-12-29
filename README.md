This directory is used to build the FSL static website.

# Installation (using Docker)

1. Install the `build-essential` package. 

```
$ sudo apt update
$ sudo apt install build-essential
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

Following these steps to publish the website. 

1. Run `./update-gh-pages`, which pushes your local edits to the branch `gh-pages` where the website is hosted. 

2. Run 

# Troubleshooting

1. Run `./build-in-docker.sh serve` and get the error message (or something similar)

```
Traceback (most recent call last):
  File "./bibtex2wiki/bibtex2wiki", line 64, in <module>
    with open('_papers/' + paper.id + '.md', 'w') as f:
IOError: [Errno 2] No such file or directory: '_papers/rosu-stefanescu-2012-oopsla.md'
```

**Solution**. Create an empty directory `fsl.cs.illinois.edu/_papers`. 


