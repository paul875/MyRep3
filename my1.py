per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму"))
deposit = [0, 0, 0, 0]
deposit[0] = per_cent['ТКБ']*money/float(100)
deposit[1] = per_cent['СКБ']*money/float(100)
deposit[2] = per_cent['ВТБ']*money/float(100)
deposit[3] = per_cent['СБЕР']*money/float(100)

dep_max_val = max(deposit)
dep_max_ind = deposit.index(dep_max_val)

print("Максимальная сумма, которую вы можете заработать —", deposit[dep_max_ind])
