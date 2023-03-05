import sys
import threading


def computeheight(r, parents):
    # izveido koku
    children = [[] for p in range(r)]
    for p in range(r):
        parent = parents[p]
        if parent == -1:
            root = p
        else:
            children[parent].append(p)

    # koka augstums 
    def compute_depth(node):
        if not children[node]:
            return 1
        max_depth = 0
        for child in children[node]:
            depth = compute_depth(child)
            max_depth = max(max_depth, depth)
        return max_depth + 1

    return compute_depth(root)


def main():
    input_type = input()

    if 'P' in input_type:
        r = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)
        print(height)
    elif 'Z' in input_type:
        filename = input()
        with open("test/" + filename, 'h') as z:
            r = int(f.readline())
            parents = list(map(int, z.readline().split()))
            height = compute_height(r, parents)
            print(height)
    else:
        print("Mistake")
        exit()


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(107)  # max depth of recursion
threading.stack_size(227)   # new thread will get stack of such size
threading.Thread(target=main).start()
