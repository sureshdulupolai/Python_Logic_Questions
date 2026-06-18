"""
Question:
Write a function that validates whether a given string is alphanumeric.

Conditions:
- The string must contain at least one character.
- Only uppercase letters (A-Z), lowercase letters (a-z), and digits (0-9) are allowed.
- No spaces, underscores (_), or special characters are allowed.

Return:
- True if the string is alphanumeric.
- False otherwise.
"""


def alphanumeric(password: str) -> bool:
    
    if password:

        for i in password:
            if not 97 <= ord(i) <= 122 and not 65 <= ord(i) <= 90 and not 48 <= ord(i) <= 57:
                return False

        return True
    
    return False

# tests = [
#     ("hello world_", False),
#     ("PassW0rd", True),
#     ("     ", False)
# ]
# for s, b in tests:
#     print(alphanumeric(s), b)


"""
Question:
Recover the original secret string using a collection of ordered triplets.

Each triplet represents the correct relative order of three characters in the final string. 
Every character appears only once, and the given triplets contain enough information to reconstruct 
the complete string.

Example:

Input:
[
  ['w', 'h', 'i'],
  ['a', 't', 's'],
  ['t', 'i', 's'],
  ['t', 'u', 'p'],
  ['h', 'a', 'p']
]

Meaning:
w comes before h, h before i
a comes before t, t before s
t comes before i, i before s
t comes before u, u before p
h comes before a, a before p

Output:
"whatisup"
"""

from collections import defaultdict, deque

def recover_secret(triplets):
    graph = defaultdict(set)
    indegree = {}

    # nodes collect + indegree init
    for triplet in triplets:
        for ch in triplet:
            indegree[ch] = 0

    # build graph
    for triplet in triplets:
        a, b, c = triplet

        if b not in graph[a]:
            graph[a].add(b)
            indegree[b] += 1

        if c not in graph[b]:
            graph[b].add(c)
            indegree[c] += 1

    # queue for zero indegree
    q = deque([node for node in indegree if indegree[node] == 0])

    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return "".join(result)

