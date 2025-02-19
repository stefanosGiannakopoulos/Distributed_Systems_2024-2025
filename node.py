from utils import hash_function,BOOTSTRAP_NODE_IP

""" 
Each Node is a FLASK server, so this Class Implements the Node as a unit of the DHT. The logic is implemented
in the API. From the API we know which nodes to reach out to ...
"""


class Node:
    def __init__(self,identifier: int,host,port,predecessor = {}, successor = {}, song_list = {}, replica_list = {}):
        self.identifier = identifier
        self.host = host
        self.port = port
        self._predecessor = predecessor
        self._successor = successor
        self._song_list = song_list
        self._replica_list = replica_list

    def insert(self, key, value):
        key = hash_function(key)
        if key not in self._song_list:
            self._song_list[key] = value
        else:
            self._song_list[key] += f", {value}"
        print(f"Song {value} added to {key}\n")
        
    
    def query(self,key):
        key = hash_function(key)
        if key == '*':
            return self._song_list
        else:
            key = hash_function(key)
            if key in self._song_list:
                print(f"Song found in this node {self.identifier}\n")
                return self._song_list[key]
            else:
                return None
    
    
    def delete(self,key):
        # We want to delete the key and its value from the song_list 
        key = hash_function(key)
        if key in self._song_list:
            del self._song_list[key]
            print(f"Song {key} deleted from this node {self.identifier}\n")
            return True
        else:
            print(f"Song not found in this node {self.identifier}\n")
            return False
           
        
    def set_predecessor(self,predecessor):
        self._predecessor = predecessor

    def set_successor(self,successor):
        self._successor = successor

    def set_song_to_song_list(self,key,value):
        self._song_list[key] = value

    # Replication Logic ...

    def set_replica_to_replica_list(self,key,value):
        self._replica_list[key] = value

    def get_predecessor(self):
        return self._predecessor

    def get_successor(self):
        return self._successor

    def get_song_list(self):
        return self._song_list

    def get_replica_list(self):
        return self._replica_list

    def delete_song_from_song_list(self,key):
        if key in self._song_list:                                 
            del self._song_list[key]
            return True
        return False

    def delete_replica_from_replica_list(self,key):
        if key in self._replica_list:
            del self._replica_list[key]
        return False

class BootstrapNode(Node):
    def __init__(self,identifier,host,port):
        super().__init__(identifier,host,port)
        self._predecessor = None
        self._successor = None
        self._song_list = {}
        self._replica_list = {}
        
        