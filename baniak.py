current = "#26B"
ch = 1
cm = 18
cs = 0

episodes = list()
episodes.append(("#00", 1, 19, 10))
episodes.append(("#01", 2, 21, 29))
episodes.append(("#02", 3, 47, 40))
episodes.append(("#03A", 1, 1, 25))
episodes.append(("#03B", 2, 2, 11))
episodes.append(("#04A", 1, 43, 31))
episodes.append(("#04B", 1, 58, 2))
episodes.append(("#05A", 1, 53, 14))
episodes.append(("#05B", 2, 3, 56))
episodes.append(("#06A", 0, 52, 36))
episodes.append(("#06B", 0, 54, 35))
episodes.append(("#06C", 1, 56, 40))
episodes.append(("#07A", 1, 30, 2))
episodes.append(("#07B", 1, 51, 41))
episodes.append(("#08A", 1, 47, 28))
episodes.append(("#08B", 0, 52, 48))
episodes.append(("#09", 2, 28, 38))
episodes.append(("#10A", 1, 36, 2))
episodes.append(("#10B", 1, 5, 52))
episodes.append(("#11A", 1, 34, 59))
episodes.append(("#11B", 1, 48, 53))
episodes.append(("#12A", 0, 19, 14))
episodes.append(("#12B", 1, 25, 0))
episodes.append(("#12C", 2, 21, 31))
episodes.append(("#13A", 1, 23, 44))
episodes.append(("#13B", 2, 33, 53))
episodes.append(("#14A", 1, 50, 50))
episodes.append(("#14B", 0, 22, 22))
episodes.append(("#14C", 2, 7, 57))
episodes.append(("#15A", 1, 38, 9))
episodes.append(("#15B", 0, 40, 48))
episodes.append(("#16A", 1, 49, 40))
episodes.append(("#16B", 2, 22, 30))
episodes.append(("#17A", 1, 46, 48))
episodes.append(("#17B", 2, 33, 31))
episodes.append(("N#01", 0, 37, 1))
episodes.append(("#18A", 1, 48, 35))
episodes.append(("E#01", 0, 0, 19))
episodes.append(("#18B", 2, 34, 33))
episodes.append(("#19", 2, 50, 5))
episodes.append(("#20A", 1, 58, 18))
episodes.append(("#20B", 1, 19, 4))
episodes.append(("#21A", 1, 42, 18))
episodes.append(("N#Or", 0, 19, 20))
episodes.append(("#21B", 2, 11, 14))
episodes.append(("#22A", 2, 27, 5))
episodes.append(("#22B", 1, 55, 9))
episodes.append(("E#02", 0, 2, 46))
episodes.append(("N#02", 0, 41, 42))
episodes.append(("N#03", 0, 34, 29))
episodes.append(("E#03", 0, 43, 31))
episodes.append(("#23A", 1, 31, 12))
episodes.append(("#23B", 2, 26, 57))
episodes.append(("#23C", 2, 9, 4))
episodes.append(("E#04", 0, 1, 53))
episodes.append(("E#05", 0, 4, 48))
episodes.append(("#24A", 1, 54, 51))
episodes.append(("#24B", 2, 20, 24))
episodes.append(("#25A", 1, 43, 1))
episodes.append(("#25B", 0, 53, 23))
episodes.append(("#25C", 1, 40, 52))
episodes.append(("#26A", 2, 27, 2))
episodes.append(("#26B", 3, 22, 22))
episodes.append(("#27", 4, 42, 59))
episodes.append(("#28", 2, 52, 57))
episodes.append(("#29A", 2, 27, 2))
episodes.append(("#29B", 1, 22, 33))
episodes.append(("#30", 3, 22, 39))
episodes.append(("#31A", 2, 12, 1))
episodes.append(("#31B", 1, 43, 35))
episodes.append(("#32A", 1, 2, 47))
episodes.append(("#32B", 0, 51, 27))
episodes.append(("#32C", 0, 58, 48))
episodes.append(("#33", 4, 3, 5))
episodes.append(("#34", 2, 46, 30))

def m2s(m, s):
    return m * 60 + s

def s2m(s):
    m = 0
    while s > 59:
        s -= 60
        m += 1
    return m, s

def h2s(h, m, s):
    _m = h * 60 + m
    return m2s(_m, s)

def s2h(s):
    h = 0
    m, s = s2m(s)
    while m > 59:
        m -= 60
        h += 1
    return h, m, s

def s2d(s):
    d = 0
    h, m, s = s2h(s)
    while h > 23:
        h -= 24
        d += 1
    return d, h, m, s

done = 0
all = 0
before = True
for ep, h, m, s in episodes:
    if ep.startswith("#"):
        if ep == current:
            before = False
            if h2s(ch, cm, cs) > h2s(h, m, s):
                ch, cm, cs = h, m, s
            done += h2s(ch, cm, cs)
        if before:
            done += h2s(h, m, s)
        all += h2s(h, m, s)

print("{0}days{1:3}:{2:02d}:{3:02d}".format(*s2d(done)))
print("{0}days{1:3}:{2:02d}:{3:02d}".format(*s2d(all)))
print("{:13d}%".format(int(round((done/all) * 100, 0))))