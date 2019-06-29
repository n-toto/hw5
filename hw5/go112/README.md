# 注意 Warning

Deploying apps using the go111 or go112 runtimes requires the use of [Cloud
Build](https://cloud.google.com/cloud-build/) which is [free for the first 120
minutes of build time per
day](https://cloud.google.com/cloud-build/#cloud-build-pricing), but still
requires a billing account to be active on a project to in order to be used. 120
minutes of build time is a lot, so most students probably won't go over this
limit if you want to try this.

## Other notes

The
[go111](https://cloud.google.com/appengine/docs/standard/go111/go-differences)
and
[go112](https://cloud.google.com/appengine/docs/standard/go112/go-differences)
runtimes for AppEngine change a lot of things.  Unlike earlier versions, running
via `dev_appserver.py` is not supported, so you have to run your app by
executing it directly. You can do this via

```sh
  cd go112
  go run .
```

You might also consider using [air](https://github.com/cosmtrek/air) to get automatic rebuilding similar to what `dev_appserver.py` used to provide, in which case you can run via:

```sh
  cd go112
  air
```

