# Python HTTP Requests README

This README provides a guide on how to fetch internet resources, decode responses, and manipulate data from external services using Python. We will cover the usage of two popular libraries, `urllib` and `requests`, for making HTTP requests.

## Table of Contents
1. [Fetching Internet Resources with urllib](#1-fetching-internet-resources-with-urllib)
2. [Decoding urllib Body Response](#2-decoding-urllib-body-response)
3. [Using the Python package requests](#3-using-the-python-package-requests)
    - [Requestsiswaysimplerthanurllib](#requestsiswaysimplerthanurllib)
4. [Making HTTP GET Request](#4-making-http-get-request)
5. [Making HTTP POST/PUT/etc. Request](#5-making-http-postputetc-request)
6. [Fetching JSON Resources](#6-fetching-json-resources)
7. [Manipulating Data from an External Service](#7-manipulating-data-from-an-external-service)

## 1. Fetching Internet Resources with urllib

```python
import urllib.request

url = 'https://example.com'
response = urllib.request.urlopen(url)
html_content = response.read()

print(html_content)
```

## 2. Decoding urllib Body Response

```python
import urllib.request

url = 'https://example.com'
response = urllib.request.urlopen(url)
body_content = response.read().decode('utf-8')

print(body_content)
```

## 3. Using the Python package requests

### Requestsiswaysimplerthanurllib

```python
import requests

url = 'https://example.com'
response = requests.get(url)
body_content = response.text

print(body_content)
```

## 4. Making HTTP GET Request

```python
import requests

url = 'https://api.example.com/data'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

## 5. Making HTTP POST/PUT/etc. Request

```python
import requests

url = 'https://api.example.com/resource'
data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post(url, json=data)

if response.status_code == 201:
    print("Resource created successfully.")
else:
    print(f"Error: {response.status_code}")
```

## 6. Fetching JSON Resources

```python
import requests

url = 'https://api.example.com/json_data'
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    print(json_data)
else:
    print(f"Error: {response.status_code}")
```

## 7. Manipulating Data from an External Service

```python
import requests

def fetch_and_process_data():
    url = 'https://api.example.com/data'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        processed_data = process_data(data)
        print(processed_data)
    else:
        print(f"Error: {response.status_code}")

def process_data(data):
    # Add your data manipulation logic here
    return data

fetch_and_process_data()
```
