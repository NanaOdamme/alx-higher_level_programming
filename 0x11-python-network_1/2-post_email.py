#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given email.
Displays the body of the response (decoded in utf-8).
Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    """Encode the email parameter"""
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    """ Make the POST request using urllib"""
    with urllib.request.urlopen(url, data=data) as response:
        """ Read and decode the response body"""
        body_content = response.read().decode('utf-8')

        """Display the decoded response body"""
        print(body_content)
