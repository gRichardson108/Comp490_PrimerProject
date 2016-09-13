#! /bin/bash
echo "Content-type: text/html"
echo

cat output.html
echo "Hello Comp 490 - (Garret Richardson)<br>"
if [ -z "${QUERY_STRING}" ] ; then
        echo "No file in query string. Try either comp490.cgi?1 or comp490.cgi?2"
else echo "${QUERY_STRING}"
fi
exit 0

