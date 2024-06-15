class UserNode:
    """Node class for storing user data in the hashtable with chaining."""

    def __init__(self, user):
        self.user = user
        self.next = None


class UserHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash_function(self, username):
        return hash(username) % self.size

    def insert(self, user):
        index = self._hash_function(user.username)
        new_node = UserNode(user)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                if current.user.username == user.username:
                    current.user = user  # Update existing user
                    return
                current = current.next
            current.next = new_node

    def find(self, username, email):
        index = self._hash_function(username)
        current = self.table[index]
        while current:
            if current.user.username == username and current.user.email == email:
                return current.user
            current = current.next
        return None  # Username not found

    def delete(self, username, email):
        index = self._hash_function(username)
        current = self.table[index]
        previous = None
        while current:
            if current.user.username == username and current.user.email == email:
                if previous:
                    previous.next = current.next  # Bypass the current node
                else:
                    self.table[index] = current.next  # Reset the head of the chain
                return True  # User successfully deleted
            previous = current
            current = current.next
        return False  # User not found

    def display(self):
        # Print the contents of the hash table
        for i, node in enumerate(self.table):
            print(f"Bucket {i}: ", end="")
            current = node
            while current:
                print(f"({current.user.username}, {current.user.email}) -> ", end="")
                current = current.next
            print("None")

