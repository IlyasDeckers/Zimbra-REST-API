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

#### List all accounts

```shell
GET /api/accounts
```

#### List accounts by domain

```shell
POST /api/accounts

    {
        "domain":"example.com"
    }
```
#### Create new account
```
POST /api/account/create

     {
        "account":"info@example.com", 
        "password": "PASSWORD"
     }

```
#### Delete account
```shell
POST /api/account/delete

    {
        "account":"info@example.com"
    }
```
#### Get account info
```shell
# Get account info
POST /api/account/info

    {
        "account":"info@example.com"
    }
    
    
```

## To-do
- create routes
  - account provisioning
  - migrate emails IMAP
  - add domains
  - update COS
- auth with tokens
- proxy server (nginx or standalone uwsi server)
- update installation
