for _ in range(int(input())):
    programmers, mathematician = list(map(int, input().split()))
    low = 1
    high = (programmers + mathematician)//4
    ans = 0
    while high >= low:
        mid = (low+high)//2
        if mid > min(programmers, mathematician):
            high = mid - 1
        else:
            ans = mid
            low = mid + 1
    print(ans)
