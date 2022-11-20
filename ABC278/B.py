H, M = map(int, input().split())
h = [int(a) for a in str(H)]
m = [int(a) for a in str(M)]

if len(h) == 1:
    if h[0] == 1 or 2 or 3 or 4 or 5:
    # if h[0] == 6 or 7 or 8 or 9:
        h[0] = 10
        m[0] = 0
        m[1] = 0

if len(h) == 2:
    if h[0] == 1:
        if h[1] == 6 or 7 or 8 or 9:
            h[0] = 2
            h[1] = 0
            m[0] = 0
            m[1] = 0

    if h[0] == 2:
        if h[1] == 0:
            if m[0] == 4 or 5 or 6 or 7 or 8 or 9:
                h[0] = 2
                h[1] = 1
                m[0] = 0
                m[1] = 0

    if h[0] == 2:
        if h[1] == 1:
            if m[0] == 4 or 5 or 6 or 7 or 8 or 9:
                h[0] = 2
                h[1] = 2
                m[0] = 0
                m[1] = 0

    if h[0] == 2:
        if h[1] == 2:
            if m[0] == 4 or 5 or 6 or 7 or 8 or 9:
                h[0] = 2
                h[1] = 3
                m[0] = 0
                m[1] = 0

    if h[0] == 2:
        if h[1] == 3:
            if m[0] == 4 or 5 or 6 or 7 or 8 or 9:
                h[0] = 0
                h[1] = 0
                m[0] = 0
                m[1] = 0

h_ans = map(str, h)
m_ans = map(str, m)
print("".join(h_ans), "".join(m_ans))

