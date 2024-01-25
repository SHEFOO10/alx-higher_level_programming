#!/bin/bash
# sends a request to the give URL, and displays the size of the body of the response
curl -Is $1 | grep -Fi 'Content-Length:' | awk '{print $2}'
