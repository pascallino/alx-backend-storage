#!/usr/bin/env python3
"""
using the aggregate function to project all documents and calculate the
average score of all documents and store it in a new key average score
also using the name of the collection to reference the items within it
topic.score
sorting in decending order {sort: {item: -1}}
"""


def top_students(mongo_collection):
    """ students by score """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
