from random import randint, seed

seed(int(input("Entrez la seed: ")))

def pretty_time(time):
    return "{}:{}".format((time//60)+9, time%60)

def pretty(time, s):
    print("{}\t{}".format(pretty_time(time), format(s)))
    return " "

pretty(0, "Gaston arrive au bureau")
def loop(time=0, time_activity=0, prunelle=False, working=False, time_prunelle=0):
    return pretty(540, "Fin du service, dure journée") and 0 if time >= 540 else 1 + loop(time+1, time_activity-1, prunelle, True, time_prunelle-1) if time_activity > 0 and working else loop(time+1, time_activity-1, prunelle, False, time_prunelle-1) if time_activity > 0 and not working else pretty(time, "Prunelle est parti. \\O/") and loop(time, 0, False, False) if time_activity == 0 and working else pretty(time, "Il faut travailler. M'enfin.") and loop(time, time_prunelle + 90, prunelle, True, time_prunelle) if prunelle and time_prunelle < 20 else pretty(time, "C'est bon, encore le temps de faire une sieste. Zzz") and loop(time, 20, prunelle, False, time_prunelle) if prunelle and time_prunelle < 50 else pretty(time, "Pause de 50min") and loop(time, 50, prunelle, False, time_prunelle) if prunelle else pretty(time, "OK, Pause !") and ((lambda x: (pretty(time, "Attention, Prunelle arrive à {}".format(pretty_time(x+time+60))) if x+time+60 < 540 else " ") and loop(time, 50, True, False, x+60))(randint(0,50)) if randint(-1, 1) else loop(time, 50, False, False))
print(loop())
