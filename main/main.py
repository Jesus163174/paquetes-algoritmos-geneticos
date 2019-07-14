from geneticos import Geneticos
k          = 20
n_max      = 4
m          = 15
t_max      = 40
t_inicial  = 2
porcentaje = 90
cruza      = 1

geneticos = Geneticos(k,n_max,m,t_max,t_inicial,porcentaje,cruza)
geneticos.start()