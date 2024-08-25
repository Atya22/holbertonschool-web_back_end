#!/usr/bin/env python3
"""Module for schools_by_topic function."""


def schools_by_topic(mongo_collection, topic):
    """Get schools with specific topics
    
    Args:
    mongo_collection: pymongo collection object
    topic: topic to search
    
    Returns: cursor
    """
    return mongo_collection.find({"topics": topic})
