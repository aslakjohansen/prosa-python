from os import environ

for key in environ:
  print("%s -> %s" % (key, environ[key]))
