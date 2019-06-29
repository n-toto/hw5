# Homework 5 Template

## ご注意 Important notes!

1. Using Google AppEngine runtime environments other than `go` or `python27` (or
   technically `java8` and `php55` -- but we don't recommend them)
   requires the use of [Cloud Build](https://cloud.google.com/cloud-build/)
   which is [free for the first 120 minutes of build time per
   day](https://cloud.google.com/cloud-build/#cloud-build-pricing), but still
   requires a billing account to be active on a project to in order to be
   used. 120 minutes of build time is a lot, so most students probably won't go
   over this limit if you want to try this.

1. For most users we recommend using just `go` or `python27`.

    -  For python users, this may mean taking some extra care to make sure that
       executing `python` is executing the right version (python 2.7). Check
       with `python --version`.

## Getting started

1.  Fork a repository for yourself with the github `Fork` button.

1.  Clone your repository to your local machine.

1.  If command line utility `gcloud` is not available, download and install
    [Google Cloud SDK](https://cloud.google.com/sdk/docs/quickstarts) ([日本語も
    あります](https://cloud.google.com/sdk/docs/quickstarts?hl=ja)). **If you're
    using the STEP Virtual Machine, it's already installed so you can skip this
    step!**

    -   Then install App Engine components for the programming language of your
        choice.
        -   Go: `gcloud components install app-engine-go`
        -   Python: `gcloud components install app-engine-python
            app-engine-python-extras`
        -   Java: `gcloud components install app-engine-java`
    -   Run `gcloud init` to initialize the SDK and create a new Cloud Platform
        project. This newly created Cloud Platform project will allow you to try
        many Google Cloud Platform products, but we will only use Google App
        Engine for this homework.
    -   If you already have Google Cloud SDK installed, run `gcloud components
        update` to update to the latest version.

1.  For first time setup, make a new Google Cloud project by running: `gcloud
    projects create [COOL NAME FOR YOUR PROJECT] --set-as-default`.

1.  Start a local App Engine server with `dev_appserver.py go/` or or
    `dev_appserver.py python27` or `dev_appserver.py python3/` (depending on
    whether you're using Go, Python2.7, or Python3).
    
    -  The `go-hello` and `python27-hello` and `python3-hello` directories
       contain simpler "hello world" apps which you might want to try first.

1.  Add functionality and test your app by viewing the local instance at
    http://localhost:8080 .

1.  Deploy your app to App Engine with `gcloud app deploy go/` or `gcloud app
    deploy python-flask/`.

    -   The first time you deploy an App Engine app to your Cloud Platform
        project, you will be asked to select a region for the location of your
        App Engine app. Select `asia-northeast1` (Tokyo), `asia-northeast2`
        (Osaka) or
        [a region](https://cloud.google.com/compute/docs/regions-zones/) that is
        close to you.

1.  To stream production server logs in the command prompt console, run `gcloud
    app logs tail -s default`. You can also use
    [the web console](https://console.cloud.google.com/logs/viewer) to
    view/stream server logs for debugging and troubleshooting.
    
    - In theory `dev_appserver.py` acts just like production, and will show you
      any logs locally, but if you find something that behaves differently, you
      can use these logs to help figure out why!

1.  `git add .` and `git commit` and `git push` to upload your changes to your
    GitHub repository.

1.  Send email to the STEP mailing list to show everyone your awesome app!

Feel free to repeat steps 5-10 as much as you like!

To learn more about AppEngine, visit the [AppEngine
Documentation](https://cloud.google.com/appengine/docs/). We strongly recommend
sticking to the [Standard Environment
runtimes](https://cloud.google.com/appengine/docs/standard/runtimes), and for
the purposes of this homework you should be able to do everything in the "Always
Free" tier without ever setting up a billing account or entering any credit card
numbers etc.
