def check_power_over_200(hp_list):

    return any(hp > 200 for hp in hp_list)

# Пример использования
powers = [120, 150, 180, 220, 160, 140, 170, 190, 210, 130, 
          155, 175, 145, 165, 185, 125, 135, 195, 215, 225,
          110, 115, 125, 135, 145, 155, 165, 175, 185, 195]

has_over_200 = check_power_over_200(powers)

if has_over_200:
    print("Есть автомобили с мощностью двигателя более 200 л.с.")
else:
    print("Автомобилей с мощностью двигателя более 200 л.с. нет")
