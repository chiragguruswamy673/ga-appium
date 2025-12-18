# ga/chromosome.py
import random

ACTIONS = [
    ("input", "com.example.demoapp:id/username", ["alice", "bob", "charlie"]),
    ("input", "com.example.demoapp:id/password", ["pass", "1234", "letmein"]),
    ("tap", "com.example.demoapp:id/submit"),
    ("tap", "com.example.demoapp:id/cart"),
    ("tap", "com.example.demoapp:id/checkout"),
    ("swipe", None),
]

def random_gene():
    gene = random.choice(ACTIONS)
    if gene[0] == "input":
        action, rid, choices = gene
        return (action, rid, random.choice(choices))
    else:
        return gene

def random_chromosome(length=10):
    return [random_gene() for _ in range(length)]
