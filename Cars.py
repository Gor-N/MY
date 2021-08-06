all_cars = ['Volvo', 'Volkswagen', 'Toyota', 'Tesla', 'Suzuki', 'Subaru', 'Bentley', 'Saturn', 'Saab', 'Rolls-Royce',\
            'Porsche', 'Nissan', 'Mitsubishi', 'Mini', 'Mercedes-Benz', 'Mazda', 'Lexus', 'Lincoln', 'Land Rover', \
            'Kia', 'Infiniti', 'Hyundai', 'Honda', 'Genesis', 'Ford', 'BMW', 'Audi', 'Acura']
japan_cars = ['Suzuki', 'Subaru', 'Nissan', 'Mitsubishi', 'Toyota', 'Mazda', 'Lexus', 'Acura', 'Honda']
german_cars = ['Volkswagen', 'Rolls-Royce', 'Porsche', 'Mini', 'Mercedes-Benz', 'BMW', 'Audi', 'Bentley', ]
usa_cars = ['Tesla', 'Saturn', 'Lincoln', 'Ford', ]
sweden_cars = ['Volvo', ]
korean_cars = ['Kia', 'Hyundai', 'Genesis', ]
toyota_mts = ['Toyota', 'Lexus']
volks_mtr = ['Volkswagen', 'Audi', 'Porsche', 'Bentley']
bmw = ['Mini', 'BMW', 'Rolls-Royce', ]
mers = ['Mercedes-Benz']
nissan = ['Nissan', 'Mitsubishi', 'Infiniti']
honda = ['Acura', 'Honda']
mazda = ['Mazda']
suzuki = ['Suzuki']
sub = ['Subaru']
for xxxx in all_cars:
    if xxxx in german_cars:
        if xxxx in volks_mtr:
            print(xxxx + " is a German car " + "made by " + "Volkswagen AG. ")
        elif xxxx in bmw:
            print(xxxx + " is a German car " + "made by " + " BMW Group ")
        elif xxxx in mers:
            print(xxxx + " is a German car " + "made by " + " Daimler AG ")

    if xxxx in japan_cars:
        if xxxx in toyota_mts:
            print(xxxx + " is a Japan car " + "made by " + "Toyota Motor Corp.")
        elif xxxx in nissan:
            print(xxxx + " is a Japan car " + "made by " + "Renault-Nissan-Mitsubishi Alliance")
        elif xxxx in honda:
            print(xxxx + " is a Japan car " + "made by " + " Honda Motor Co.")
        elif xxxx in mazda:
            print(xxxx + " is a Japan car " + "made by " + " Mazda Motor Corp.")
        elif xxxx in suzuki:
            print(xxxx + " is a Japan car " + "made by " + " Suzuki Motor Corp. Owns a small stake in Toyota")
        elif xxxx in sub:
            print(xxxx + " is a Japan car " + "made by " + " Subaru Corp.")

    if xxxx in usa_cars:
        print(xxxx + " is a USA car")
    if xxxx in sweden_cars:
        print(xxxx + " is a Sweden car")
    if xxxx in korean_cars:
        print(xxxx + " is a Korean car")
