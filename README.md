#What This Script Does

Creates three tables: User, Product, Order

Defines proper foreign keys and relationships

Inserts sample users, products, and orders

Demonstrates CRUD operations:

Create: via session.add_all()

Read: via .query()

Update: modifies a product price

Delete: removes a user

Bonus:

Adds status column (shipped or not)

Queries unshipped orders

Counts total orders per user

# SQLAlchemy Relational Database Practice

## Description
This project demonstrates how to create and manage a relational database using Python and SQLAlchemy with SQLite.

## Setup
1. Install dependencies:
   ```bash
   pip install SQLAlchemy

## Run the script:

python3 shop_database.py

## A file named shop.db will be created automatically in your directory.

## Features

Users, Products, and Orders tables

Relationships using foreign keys

CRUD operations (Create, Read, Update, Delete)

Bonus: shipped status and order count per user
