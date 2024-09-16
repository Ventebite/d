'''В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один
родитель.
Даны два элемента в дереве. Определите, является ли один из них потомком другого.'''
def read_input():
    n = int(input())
    parent_dict = {}
    for _ in range(n - 1):
        child, parent = input().split()
        parent_dict[child] = parent
    k = int(input())
    queries = []
    for _ in range(k):
        queries.append(input().split())
    return parent_dict, queries
def find_ancestors(person, parent_dict):
    ancestors = set()
    while person in parent_dict:
        parent = parent_dict[person]
        ancestors.add(parent)
        person = parent
    return ancestors
def process_queries(parent_dict, queries):
    results = []
    for a, b in queries:
        ancestors_a = find_ancestors(a, parent_dict)
        ancestors_b = find_ancestors(b, parent_dict)
        if a in ancestors_b:
            results.append(1)
        elif b in ancestors_a:
            results.append(2)
        else:
            results.append(0)
def process_queries(parent_dict, queries):
    results = []
    for a, b in queries:
        ancestors_a = find_ancestors(a, parent_dict)
        ancestors_b = find_ancestors(b, parent_dict)
        if a in ancestors_b:
            results.append(1)
        elif b in ancestors_a:
            results.append(2)
        else:
            results.append(0)
    return results
def main():
    parent_dict, queries = read_input()
    results = process_queries(parent_dict, queries)
    for result in results:
        print(result)
if __name__ == "__main__":
    main()