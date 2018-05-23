#!/bin/bash

# nicked from here https://github.com/18F/cf-cd-example/blob/master/deploy.sh

set -e

unamestr=`uname`

if ! hash cf 2>/dev/null; then
  echo "Installing Cloud Foundry CLI..."
  if [[ "$unamestr" == 'Darwin' ]]; then
    brew tap cloudfoundry/tap
    brew install cf-cli
  else
    mkdir -p tmp
    PATH=$PWD/tmp:$PATH
    curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar -zx -C tmp
  fi
fi


if [ -n "$CF_USERNAME" ] && [ -n "$CF_PASSWORD" ]; then
  cf login -a "$CF_API" -u "$CF_USERNAME" -p "$CF_PASSWORD"
fi

cf target -o "$ORG" -s "$SPACE"

cf push

cf run-task digital-land-explorer "flask db upgrade" --name db-upgrade

