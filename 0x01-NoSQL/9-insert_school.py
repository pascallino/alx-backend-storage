#!/usr/bin/env python3
""" Write a Python function that
lists all documents in a collection: """


def insert_school(mongo_collection, **kwargs):
    """ Write a Python function that inserts a new document"""
    if mongo_collection is None:
        return
    if (not isinstance(kwargs, dict)) or kwargs is None:
        return
    newdocument = mongo_collection.insert_one(kwargs)
    return newdocument.inserted_id
