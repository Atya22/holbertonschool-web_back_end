#!/usr/bin/env python3
"""Module for insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection
    
    Args:
    mongo_collection: pymongo collection object
    kwargs: dictionary with key-values to be inserted
    
    Returns: the new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
