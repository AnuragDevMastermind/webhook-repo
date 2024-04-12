from flask import jsonify
from datetime import datetime, timezone, timedelta

def extract_event_from_response(data):
    if 'action' in data:
        if data['action'] == 'opened':
            return extract_event_pull_request(data)
        elif data['action'] == 'closed':
            return extract_event_merge_request(data)
    elif data.get('created', False) or len(data.get('commits', [])) == 1:
        return extract_event_push_request(data)

def extract_event_pull_request(data): 
    baseRef = data.get('pull_request', {}).get('base', {}).get('ref')
    fromBranch = data.get('pull_request',{}).get('head', {}).get('ref')
    author = data.get('pull_request',{}).get('head', {}).get('label').split(":")[0]
    requestId = data.get('pull_request',{}).get('head', {}).get('id')
    return {
        "request_id": requestId,
        "author": author,
        "action": "PULL_REQUEST",
        "from_branch": fromBranch,
        "to_branch": baseRef,
        "timestamp": datetime.now(timezone.utc)
    }

def extract_event_push_request(data): 
    commits = data.get('commits', [])
    author = [commit['author']['username'] for commit in commits if 'author' in commit and 'username' in commit['author']]
    headRef = data.get('ref')
    to_branch = headRef.split('/')[-1]
    requestId = commits[0]['id']
    return {
        "request_id": requestId,
        "author": author[0],
        "action": "PUSH",
        "from_branch": "",
        "to_branch": to_branch,
        "timestamp": datetime.now(timezone.utc)
    }

def extract_event_merge_request(data):
    requestId = data.get('pull_request',{}).get('merged_by', {}).get('id')
    author = data.get('pull_request',{}).get('merged_by', {}).get('login')
    fromBranch = data.get('pull_request',{}).get('head', {}).get('ref')
    toBranch = baseRef = data.get('pull_request', {}).get('base', {}).get('ref')

    return {
        "request_id": requestId,
        "author": author,
        "action": "MERGE",
        "from_branch": fromBranch,
        "to_branch": toBranch,
        "timestamp": datetime.now(timezone.utc)
    }