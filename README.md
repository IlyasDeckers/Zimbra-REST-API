# Zimbra REST API
## Introduction

Work in progress

Ever felt in need of a simple API to provission Zimbra accounts and other tasks?  
This Python app provides an easy to use and understand wrapper around the Zibmra ecosystem

## Installation

```shell
$ cd /opt
$ sudo git clone https://github.com/IlyasDeckers/Zimbra-REST-API.git
$ cd Zimbra-REST-API
$ sh install.sh
$ sudo su zimbra
$ ./run.py
```

## Usage

### Endpoints

```
GET /api/accounts

    curl -i -u user:password -H "Content-Type: application/json" -X POST http://IP:5000/todo/api/account/create

POST /api/accounts

    curl -i -u user:password -H "Content-Type: application/json" -X POST -d "{"domain":"example.com"}" http://IP:5000/todo/api/account/create

POST /api/account/create

     curl -i -u user:password -H "Content-Type: application/json" -X POST -d "{"account":"info@example.com", "password": "PASSWORD"}" http://IP:5000/todo/api/account/create

# Delete account
POST /api/account/delete

    curl -i -u user:password -H "Content-Type: application/json" -X POST -d "{"account":"info@example.com"}" http://IP:5000/todo/api/account/delete

# Add a new domain
POST /api/account/info

    curl -i -u user:password -H "Content-Type: application/json" -X POST -d "{"account":"info@example.com"}" http://IP:5000/todo/api/account/info
```

## To-do
- create routes
- update auth system with tokens
- proxy server
- update installation
