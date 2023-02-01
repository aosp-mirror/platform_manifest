#!/bin/bash
gob-curl --silent https://android.googlesource.com/platform/manifest/+/refs/heads/master/default.xml\?format\=TEXT | base64 --decode > default.xml
sed -i 's/<superproject \(.*\)\/>/<superproject \1 revision="main-cuttlefish-vendor-dev"\/>/' default.xml
