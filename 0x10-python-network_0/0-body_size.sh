#!/bin/bash
# This script takes a URL as an argument, sends a silent HTTP GET request using curl, and displays the size of the response body in bytes.
curl -s "$1" | wc -c
