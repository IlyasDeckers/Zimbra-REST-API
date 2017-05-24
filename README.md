# Zimbra REST API
## Introduction

*** Work in progress

Ever felt in need of a simple API to provission Zimbra accounts and other tasks?  
This Python app provides an easy to use and understand wrapper around the Zibmra ecosystem

## Installation

Comming soom

## Usage

### Endpoints

```
GET /api/accounts

    curl -i -u user:password -H "Content-Type: application/json" -X POST http://IP:5000/todo/api/account/create

POST /api/account/create

     curl -i -u user:password -H "Content-Type: application/json" -X POST -d "{"domain":"example.com
"}" http://IP:5000/todo/api/account/create

# Get all domains
GET /api/domains

# Add a new domain
POST /api/domain/create
```
