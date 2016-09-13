#! /bin/bash
echo "Content-type: text/html"
echo

cat output.html
echo "Hello Comp 490 - (Garret Richardson)<br>"
if [ -z "${QUERY_STRING}" ] ; then
        echo "No file in query string. Try either comp490.cgi?1 or comp490.cgi?2"
	elif [ "${QUERY_STRING}" -eq 1 ]
	then echo "<img src=\"test.gif\" alt=\"crappy gif animation\" height=\"240\" width=\"320\">"
	elif [ "${QUERY_STRING}" -eq 2 ]
	then echo "<img src=\"test2.gif\" alt=\"crappy gif animation 2\" height=\"240\" width=\"320\">"
	else echo "Invalid query string. Try either comp490.cgi?1 or comp490.cgi?2"
	fi
	
	echo "<hr>"
	/usr/bin/curl -s "https://github.com/gRichardson108"
exit 0

