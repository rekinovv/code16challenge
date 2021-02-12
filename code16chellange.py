macro = { 'kcal': 0, 'prot': 0, 'carb': 0, 'fats': 0 }
donuts = { 'donut': [198, 10.7, 23.3, 2.4] , 'pączek_z_lukrem' : [291, 5.3, 43.5, 10.9] , 'pączek_z_serem' : [184, 9.1, 17.4, 8.8] }
sports = { 'bieganie': 12, 'spacer': 4.2, 'rower': 11.6, 'odśnieżanie': 7,   }
while True:
    if input(' Czy chcesz dodać pączke ? (tak/nie) : ') == 'tak':
        name = input (' Wybierz pączka z listy : \n' + ' '.join(donuts.keys()) + '\n ~ ')
        i = 0
        for v in macro.keys():
            macro[v] += donuts[name][i]
            i += 1
    else: break

[print(k, ' - ', macro[k]) for k in macro.keys()]
sport = input(' Wybierz co chcesz zrobic aby spalić kalorie: \n' + ' '.join(sports.keys()) + '\n ~ ')
time_to_do = macro['kcal'] / sports[sport]
print(' Musisz robić to przez', time_to_do , 'minut')
