N, M = map(int, input().split())

u_list = []
v_list = []
for i in range(M):
    u, v = map(int, input().split())
    u_list.append(u)
    v_list.append(v)

edges = [[u_list[i], v_list[i]] for i in range(M)]

print(edges)
check = sorted(edges)

if N != M + 1:
    print("No")
else:
    for i in range(M):
        check[i]

# def is_path_graph(N, M, edges):
#     if N != M + 1:
#         return False
#     for i in range(N-1):
#         found = False
#         for edge in edges:
#             if i in edge:
#                 found = True
#                 break
#         if not found:
#             return False
#     return True
#
# if is_path_graph(N, M, edges):
#     print("Yes")
# else:
#     print("No")
