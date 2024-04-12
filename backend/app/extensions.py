from pymongo import MongoClient
from datetime import datetime, timezone, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

client = MongoClient(database_url)
db = client.webhook

def insert_event(data):
  event = {**data, "timestamp": datetime.now(timezone.utc)}
  result = db.events.insert_one(event)
  event["_id"] = str(result.inserted_id)
  return event

def get_all_events():
    pipeline = [
        {
            "$match": {
                "timestamp": {"$gte": datetime.now(timezone.utc) - timedelta(seconds=15)}
            }
        },
        {
        "$project": {
            "_id": 0,
            "request_id": 1,
            "description": {
                "$switch": {
                    "branches": [
                        {
                            "case": { "$eq": ["$action", "PUSH"] },
                            "then": {
                                "$concat": [
                                    "$author",
                                    " pushed to ",
                                    "$to_branch",
                                    " on ",
                                    {
                                        "$dateToString": {
                                            "format": "%d %B %Y - %H:%M UTC",
                                            "date": "$timestamp",
                                            "timezone": "UTC"
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "case": { "$eq": ["$action", "PULL_REQUEST"] },
                            "then": {
                                "$concat": [
                                    "$author",
                                    " submitted a pull request from ",
                                    "$from_branch",
                                    " to ",
                                    "$to_branch",
                                    " on ",
                                    {
                                        "$dateToString": {
                                            "format": "%d %B %Y - %H:%M UTC",
                                            "date": "$timestamp",
                                            "timezone": "UTC"
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "case": { "$eq": ["$action", "MERGE"] },
                            "then": {
                                "$concat": [
                                    "$author",
                                    " merged branch ",
                                    "$from_branch",
                                    " to ",
                                    "$to_branch",
                                    " on ",
                                    {
                                        "$dateToString": {
                                            "format": "%d %B %Y - %H:%M UTC",
                                            "date": "$timestamp",
                                            "timezone": "UTC"
                                        }
                                    }
                                ]
                            }
                        }
                    ],
                    "default": "Unknown action type"
                }
            }
        }
    }
    ]

    return list(db.events.aggregate(pipeline))
