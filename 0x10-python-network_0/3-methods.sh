#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -sLI 0.0.0.0:5000/route_4 -i | grep "Allow:"|cut -d ' ' -f2
