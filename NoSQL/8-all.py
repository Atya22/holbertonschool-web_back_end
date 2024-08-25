#!/usr/bin/env python3
"""Module for list_all function"""


def list_all(mongo_collection):
    """ Lists all documents in a collection. 
    
    Args: mongo_collection: pymongo collection object
    
    Returns: list of documents
    """
    return list(mongo_collection.find())
