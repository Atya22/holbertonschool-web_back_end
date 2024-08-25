#!/usr/bin/env python3
"""Module for logging stats"""
from pymongo import MongoClient, errors

def log_stats():
    """Function that retrieves logs stats from MongoDB."""
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client.logs
        collection = db.nginx

        # Count total logs
        total_logs = collection.count_documents({})
        print(f"{total_logs} logs")

        # Count methods
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        print("Methods:")
        for method in methods:
            count = collection.count_documents({"method": method})
            print(f"\tmethod {method}: {count}")

        # Count specific query
        status_check = collection.count_documents({"method": "GET", "path": "/status"})
        print(f"{status_check} status check")

    except errors.ServerSelectionTimeoutError as err:
        print(f"Could not connect to MongoDB: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    log_stats()
