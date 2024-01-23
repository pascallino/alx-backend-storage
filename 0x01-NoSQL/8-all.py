#!/usr/bin/env python3
""" Write a Python function that
lists all documents in a collection: """


def list_all(mongo_collection):
    """ function to list school collection"""
    list = []
    if mongo_collection is not None:
        list = [item for item in mongo_collection.find()]
        return list
    else:
        return []
