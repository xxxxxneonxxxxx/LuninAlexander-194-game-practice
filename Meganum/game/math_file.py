import random

nah_zna = []


def chis(strok, stol, prav, lev):
    def stolb(s1, s2, s3, s4, s5, s6, s7, s8,
              stolb):
        stol = []
        for i in range(0, len(s1)):
            if stolb == 5: stol.append(s1[i] + s2[i] + s3[i] + s4[i] + s5[i])
            if stolb == 6: stol.append(s1[i] + s2[i] + s3[i] + s4[i] + s5[i] + s6[i])
            if stolb == 7: stol.append(s1[i] + s2[i] + s3[i] + s4[i] + s5[i] + s6[i] + s7[i])
            if stolb == 8: stol.append(s1[i] + s2[i] + s3[i] + s4[i] + s5[i] + s6[i] + s7[i] + s8[i])
        return stol

    def stroka(prav, lev, strok):
        chis = []
        if strok == 5:
            a1 = random.randint(prav, lev)
            a2 = random.randint(prav, lev)
            a3 = random.randint(prav, lev)
            chis.append(a3)
            chis.append(a1)
            chis.append(a2)
        if strok == 6 or strok == 7:
            a1 = random.randint(prav, lev)
            a2 = random.randint(prav, lev)
            a3 = random.randint(prav, lev)
            a4 = random.randint(prav, lev)
            chis.append(a3)
            chis.append(a4)
            chis.append(a1)
            chis.append(a2)
        if strok == 8:
            a1 = random.randint(prav, lev)
            a2 = random.randint(prav, lev)
            a3 = random.randint(prav, lev)
            a5 = random.randint(prav, lev)
            a4 = random.randint(prav, lev)
            chis.append(a4)
            chis.append(a3)
            chis.append(a5)
            chis.append(a1)
            chis.append(a2)
        for i in range(strok):
            if len(chis) != strok: chis.append(0)
        return chis

    def play(strok, prav, lev):
        chis = stroka(prav, lev, strok)
        for i in range(10):
            rand1 = random.randint(0, len(chis) - 1)
            rand2 = random.randint(0, len(chis) - 1)
            b = chis[rand1]
            chis[rand1] = chis[rand2]
            chis[rand2] = b
        return chis

    def random_stolb(s1, s2, s3, s4, s5, s6, s7, s8, stolb):
        for i in range(1, len(s1)):
            stol = []
            stol.append(s1[i])
            stol.append(s2[i])
            stol.append(s3[i])
            stol.append(s4[i])
            stol.append(s5[i])
            if stolb == 6: stol.append(s6[i])
            if stolb == 7: stol.append(s7[i])
            if stolb == 8: stol.append(s8[i])
            if stol.count(0) == 0:
                ran = random.randint(1, stolb)
                if ran == 1:
                    s1[i] = 0
                if ran == 2:
                    s2[i] = 0
                if ran == 3:
                    s3[i] = 0
                if ran == 4:
                    s4[i] = 0
                if ran == 5:
                    s5[i] = 0
                if ran == 6:
                    s6[i] = 0
                if ran == 7:
                    s7[i] = 0
                if ran == 8:
                    s8[i] = 0
        return s1, s2, s3, s4, s5, s6, s7, s8

    def random_0(s, prav, lev):
        c = 0
        for i in s:
            if i == 0:
                s[c] = random.randint(prav, lev)
            c += 1
        return s

    if stol == 5:
        a1 = (play(strok, prav, lev))
        a2 = (play(strok, prav, lev))
        a3 = (play(strok, prav, lev))
        a4 = (play(strok, prav, lev))
        a5 = (play(strok, prav, lev))
        a6 = None
        a7 = None
        a8 = None

        nah_zna = [a1.copy(), a2.copy(), a3.copy(), a4.copy(), a5.copy(), a6, a7, a8]
        a11 = (random_stolb(a1, a2, a3, a4, a5, a6, a7, a8, stol))

    if stol == 6:
        a1 = (play(6, prav, lev))
        a2 = (play(6, prav, lev))
        a3 = (play(6, prav, lev))
        a4 = (play(6, prav, lev))
        a5 = (play(6, prav, lev))
        a6 = (play(6, prav, lev))
        a7 = None
        a8 = None
        nah_zna = [a1.copy(), a2.copy(), a3.copy(), a4.copy(), a5.copy(), a6, a7, a8]

        a11 = (random_stolb(a1, a2, a3, a4, a5, a6, a7, a8, stol))

    if stol == 7:
        a1 = (play(7, prav, lev))
        a2 = (play(7, prav, lev))
        a3 = (play(7, prav, lev))
        a4 = (play(7, prav, lev))
        a5 = (play(7, prav, lev))
        a6 = (play(7, prav, lev))
        a7 = (play(7, prav, lev))
        a8 = None
        nah_zna = [a1.copy(), a2.copy(), a3.copy(), a4.copy(), a5.copy(), a6, a7, a8]

        a11 = (random_stolb(a1, a2, a3, a4, a5, a6, a7, a8, stol))

    if stol == 8:
        a1 = (play(8, prav, lev))
        a2 = (play(8, prav, lev))
        a3 = (play(8, prav, lev))
        a4 = (play(8, prav, lev))
        a5 = (play(8, prav, lev))
        a6 = (play(8, prav, lev))
        a7 = (play(8, prav, lev))
        a8 = (play(8, prav, lev))
        nah_zna = [a1.copy(), a2.copy(), a3.copy(), a4.copy(), a5.copy(), a6, a7, a8]

        a11 = (random_stolb(a1, a2, a3, a4, a5, a6, a7, a8, stol))

    for i in range(0, len(a11)):
        if i == 0: a1 = a11[i]
        if i == 1: a2 = a11[i]
        if i == 2: a3 = a11[i]
        if i == 3: a4 = a11[i]
        if i == 4: a5 = a11[i]
        if i == 5: a6 = a11[i]
        if i == 6: a7 = a11[i]
        if i == 7: a8 = a11[i]
        sum_col = (stolb(a1, a2, a3, a4, a5, a6, a7, a8, stol))
    g = []
    sum_str = []
    for i in a11:
        if i == None:
            continue
        sum_str.append(sum(i))
        g.append(random_0(i, prav, lev))
    for i in range(0, len(g)):
        if i == 1: a1 = g[i]
        if i == 2: a2 = g[i]
        if i == 3: a3 = g[i]
        if i == 4: a4 = g[i]
        if i == 5: a6 = g[i]
        if i == 7: a7 = g[i]
        if i == 8: a8 = g[i]
        sim_str1 = []
        for i in g:
            sim_str1.append(sum(i))
        sum_col1 = (stolb(a1, a2, a3, a4, a5, a6, a7, a8, stol))
    return [[sum_col1], [sim_str1], g, [sum_col], [sum_str], nah_zna]
