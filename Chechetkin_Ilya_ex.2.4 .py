first_list =['инженер-конструктор Игорь',
             'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
for w in first_list:
    true_name = w.split()[-1].title()
    print(f'Привет, {true_name}!')