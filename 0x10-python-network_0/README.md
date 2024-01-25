# 0x10. Python - Network #0

# Understanding Web Basics

## What is a URL?
A Uniform Resource Locator (URL) is a reference or address used to access resources on the internet. It typically consists of a protocol (such as HTTP or HTTPS), domain name, and additional path or parameters.

## What is HTTP?
Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the World Wide Web. It is a protocol for transmitting hypermedia documents, such as HTML. HTTP follows a client-server model, where the client sends requests, and the server responds with the requested resources.

## How to Read a URL
A URL is composed of several components, including the protocol, domain name, path, port, and query parameters. Understanding each part helps navigate and access specific resources on the internet.

## The Scheme for an HTTP URL
The scheme in an HTTP URL indicates the protocol used, such as "http" or "https." It specifies how the browser or client should communicate with the server to retrieve the requested resource.

## What is a Domain Name?
A domain name is a human-readable address that represents an IP address on the internet. It provides a way to identify and locate resources, like websites, without having to remember numerical IP addresses.

## What is a Sub-domain?
A sub-domain is a part of a larger domain and precedes the main domain name. It allows for the organization and categorization of content within a website. For example, "blog.example.com" is a sub-domain of "example.com."

## How to Define a Port Number in a URL
Port numbers in a URL specify the endpoint on the server that the client should connect to. If no port is specified, the default port for the given protocol is used (e.g., 80 for HTTP).

## What is a Query String?
A query string is a part of a URL that contains additional parameters for a resource request. It usually follows a "?" and includes key-value pairs that the server can use to customize the response.

## What is an HTTP Request?
An HTTP request is a message sent by a client to request a specific action or resource from a server. It includes information such as the requested method, headers, and, if applicable, a message body.

## What is an HTTP Response?
An HTTP response is the message sent by a server to fulfill a client's request. It contains information about the status of the request, along with the requested data (if applicable).

## What are HTTP Headers?
HTTP headers provide additional information about the request or response. They include details like content type, length, server information, and cookies. Headers are crucial for proper communication between clients and servers.

## What is the HTTP Message Body?
The HTTP message body contains the actual data being sent in the request or response. In requests, it may include form data or file uploads. In responses, it contains the requested resource or an error message.

## What is an HTTP Request Method?
HTTP request methods define the type of action the client wants to perform. Common methods include GET (retrieve data), POST (submit data), and DELETE (remove data).

## What is an HTTP Response Status Code?
HTTP response status codes indicate the outcome of the server's attempt to process the request. Codes range from informational (1xx) to successful (2xx), redirection (3xx), client errors (4xx), and server errors (5xx).

## What is an HTTP Cookie?
An HTTP cookie is a small piece of data stored on the user's device by the browser. Cookies are used to store information about user preferences, session state, or tracking information, facilitating a personalized browsing experience.

## How to Make a Request with cURL
cURL is a command-line tool for making HTTP requests. It allows users to interact with web services and test APIs directly from the terminal. Examples of cURL commands can demonstrate various HTTP methods and headers.

## What Happens When You Type google.com in Your Browser (Application Level)
When you type "google.com" in your browser, the application initiates a series of actions, including DNS resolution to find the IP address, establishing a TCP connection, performing a secure handshake (if using HTTPS), sending an HTTP request, and finally, receiving and rendering the HTTP response to display the Google homepage.
