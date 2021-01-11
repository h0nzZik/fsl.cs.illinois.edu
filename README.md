This directory is used to build the FSL static website.

# Installation (using Docker)

1.  Install Docker following https://docs.docker.com/engine/install/ubuntu/.

2.  Make Docker work with non-root users following
    https://docs.docker.com/engine/install/linux-postinstall/. You may need to
    reboot your machine.

3.  make sure that you have the branch `gh-pages` created.

    ```
    $ git branch gh-pages origin/gh-pages
    ```

# Build (using Docker)

On your first build, run `./build-in-docker image` to create the Docker image. 

To preview the website locally, run `./build-in-docker.sh serve`. If you see the following messages then the build is succesful:

```
 [ ... MORE MESSAGES ... ]
 Auto-regeneration: enabled for '/mnt/fsl/www/fsl.cs.illinois.edu'
    Server address: http://0.0.0.0:4000/fsl//
  Server running... press ctrl-c to stop.
```

You can access the website by visiting the server address http://0.0.0.0:4000/fsl/ in a web browser. 

# Publish


First, commit all changes to source files to git.

    git commit -a

Next, generate the html pages:

    ./build-in-docker build

Finally, commit the website build to the `gh-pages` branch, and push:

    ./commit
    git push origin gh-pages

