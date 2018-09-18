# Cookies experimentations with cross-domain requests

Showing the effect of SameSite parameter

## Steps
http://127.0.0.1:5000/get-cookies

http://127.0.0.1:5000/set-cookies


http://localhost:5001/

http://127.0.0.1:5000/get-cookies

In the request that is sent, only the one with SameScript unset is passed
Cookie: username=John