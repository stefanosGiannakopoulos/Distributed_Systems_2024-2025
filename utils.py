import hashlib

MAX_NODES = 10

BOOTSTRAP_NODE_IP = "NOT_SET"


def hash_function(key: str) -> int:
    return int(hashlib.sha1(key.encode()).hexdigest(), 16) % MAX_NODES
    