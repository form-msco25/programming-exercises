"""Crie dois sets com números e mostre a união, interseção e diferença entre eles."""
set_a = {1, 3, 5, 7, 9}
set_b = {1, 2, 3, 4, 5}

uni_op = set_a | set_b
uni_func = set_a.union(set_b)
print(uni_op, uni_func)

inter_op = set_a & set_b
inter_func = set_a.intersection(set_b)
print(inter_op, inter_func)

dif_AB_op = set_a - set_b
dif_AB_func = set_a.difference(set_b)
print(dif_AB_op, dif_AB_func)

dif_BA_op = set_b - set_a
dif_BA_func = set_b.difference(set_a)
print(dif_BA_op, dif_BA_func)

dif_sim_op = set_a ^ set_b
dif_sim_func = set_a.symmetric_difference(set_b)
print(dif_sim_op, dif_sim_func)