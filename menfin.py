from random import randint, seed

seed(int(input("Entrez la seed: ")))

pretty_time = lambda time: "{}:{}".format((time//60)+9, time%60)

pretty = lambda time, s: print("{}\t{}".format(pretty_time(time), format(s))) or " "

(lambda h: print("Temps total travaillé : {} h {} min".format(h//60, h%60)))((lambda f: lambda a, b, c, d, e: f(f, a, b, c, d, e))(lambda loop, time, time_activity, prunelle, working, time_prunelle:
    pretty(0, "Gaston arrive au bureau") and pretty(540, "Fin du service, dure journée") and 0 if time >= 540 else 1 + loop(loop, time+1, time_activity-1, prunelle, True, time_prunelle-1) if time_activity > 0 and working else loop(loop, time+1, time_activity-1, prunelle, False, time_prunelle-1) if time_activity > 0 and not working else pretty(time, "Prunelle est parti. \\O/") and loop(loop, time, 0, False, False, 0) if time_activity == 0 and working else pretty(time, "Il faut travailler. M'enfin.") and loop(loop, time, time_prunelle + 90, prunelle, True, time_prunelle) if prunelle and time_prunelle < 20 else pretty(time, "C'est bon, encore le temps de faire une sieste. Zzz") and loop(loop, time, 20, prunelle, False, time_prunelle) if prunelle and time_prunelle < 50 else pretty(time, "Pause de 50min") and loop(loop, time, 50, prunelle, False, time_prunelle) if prunelle else pretty(time, "OK, Pause !") and ((lambda x: (pretty(time, "Attention, Prunelle arrive à {}".format(pretty_time(x+time+60))) if x+time+60 < 540 else " ") and loop(loop, time, 50, True, False, x+60))(randint(0,50)) if randint(-1, 1) else loop(loop, time, 50, False, False, 0)))(0, 0, False, False, 0))
