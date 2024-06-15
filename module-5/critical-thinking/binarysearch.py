import bisect

class BinarySearchArray:
    def __init__(self):
        self.users = []

    def _make_key(self, user):
        return f"{user.username}-{user.email}"

    def insert(self, user):
        # Create a key for sorting and searching
        key = self._make_key(user)
        # Insert user ensuring the list remains sorted by the key
        bisect.insort(self.users, (key, user))

    def find(self, username, email):
        # Create a search key
        search_key = f"{username}-{email}"
        # Perform binary search to find the user
        index = bisect.bisect_left(self.users, (search_key,))  # Ensure to pass a tuple for consistent comparison
        if index != len(self.users) and self.users[index][0] == search_key:
            return self.users[index][1]
        return None

    def delete(self, username, email):
        # Create a delete key
        delete_key = f"{username}-{email}"
        # Find and remove the user if exists
        index = bisect.bisect_left(self.users, (delete_key,))  # Again, pass a tuple
        if index != len(self.users) and self.users[index][0] == delete_key:
            del self.users[index]
            return True
        return False

    def display(self):
        # Display the contents of the array
        for key, user in self.users:
            print(f"User: {user.username}, Email: {user.email}, Location: {user.location}, Interests: {user.interests}")
