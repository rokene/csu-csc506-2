import random
from data import *

def generate_random_users(num_users):
    names = ["john", "jane", "alice", "bob", "carol", "david"]
    domains = ["example.com", "demo.com", "test.com"]
    interests = ["music", "travel", "books", "tech", "photography", "yoga"]
    users = []
    user_id = 1

    for _ in range(num_users):
        base_username = random.choice(names)
        unique_username = f"{base_username}{user_id}"
        email = unique_username + "@" + random.choice(domains)
        location = random.choice(["New York", "London", "Sydney", "Tokyo", "Paris", "Berlin", "Moscow"])
        user_interests = random.sample(interests, random.randint(1, 3))
        users.append(SocialMediaUser(user_id, unique_username, email, location, user_interests))
        user_id += 1

    return users
