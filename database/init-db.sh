#!/bin/bash
# init-db.sh - 數據庫初始化腳本

# Initialize the database
psql -U postgres -d mydatabase -f /path/to/schema.sql
