#!/bin/bash
sed -i '/^<\/manifest>/i PLACEHOLDER' default.xml
sed -i '/PLACEHOLDER/r additional_repo' default.xml
sed -i '/PLACEHOLDER/d' default.xml
