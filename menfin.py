from random import randint, seed

seed(int(input("Entrez la seed: ")))

def pretty_time(time):
    return "{}:{}".format((time//60)+9, time%60)

def pretty(time, s):
    print("{}\t{}".format(pretty_time(time), format(s)))

pretty(0, "Gaston arrive au bureau")
def loop(time=0, time_activity=0, prunelle=False, working=False, time_prunelle=0):
    if time >= 540:
        pretty(540, "Fin du service, dure journée")
    else:
        if time_activity > 0:
            # working
            if working:
                return 1 + loop(time+1, time_activity-1, prunelle, True, time_prunelle-1)
            # pausing
            else:
                return loop(time+1, time_activity-1, prunelle, False, time_prunelle-1)
        # changing
        elif time_activity == 0:
            # was working
            if working:
                pretty(time, "Prunelle est parti. \\O/")
                return loop(time, 0, False, False)
            # begin pause
            else:
                if prunelle:
                    if time_prunelle < 20:
                        pretty(time, "Il faut travailler. M'enfin.")
                        return loop(time, time_prunelle + 90, prunelle, True, time_prunelle)
                    elif time_prunelle < 50:
                        pretty(time, "C'est bon, encore le temps de faire une sieste. Zzz")
                        return loop(time, 20, prunelle, False, time_prunelle)
                    else:
                        pretty(time, "Pause de 50min")
                        return loop(time, 50, prunelle, False, time_prunelle)

                else:
                    pretty(time, "OK, Pause !")
                    if randint(-1, 1):
                        x = time + randint(0,50) + 60
                        pretty(time, "Attention, Prunelle arrive à {}".format(pretty_time(x))) if x < 540 else None
                        return loop(time, 50, True, False, x-time)
                    else:
                        return loop(time, 50, False, False)
    return 0
print(loop())
