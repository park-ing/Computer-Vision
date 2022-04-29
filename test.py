import collections


def solution(participant, completion):
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer.keys())
    return list(answer.keys())[0]

x = ['a','b','c','d','e']
t = ['b','e','a','c']
print(solution(x,t))

print()
print()
