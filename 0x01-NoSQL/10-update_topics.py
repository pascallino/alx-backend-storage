#!/usr/bin/env python3
""" Write a Python function that updates topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """Updates topics of a school document based on the name."""
    # Update all documents with the given name
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
