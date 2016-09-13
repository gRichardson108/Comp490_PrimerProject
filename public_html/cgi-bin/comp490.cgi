#! /bin/bash
echo "Content-type: text/html"
echo

echo "Hello Comp 490 - (Garret Richardson)"
/usr/bin/curl -s "http://stackoverflow.com"
echo "Test output" > output.html

exit 0
