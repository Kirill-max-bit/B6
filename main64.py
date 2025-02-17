def есть_мощные_автомобили(мощности):
    """
    Проверяет наличие автомобилей с мощностью двигателя более 200 л.с.
    
    Args:
        мощности: список из 30 целых чисел (мощности двигателей)
        
    Returns:
        bool: True если есть автомобиль с мощностью > 200 л.с., False если нет
    """
    return any(мощность > 200 for мощность in мощности)

# Примеры использования
примеры = [
    [150, 160, 170, 180, 190, 200, 150, 160, 170, 180, 190, 200, 150, 160, 170, 180, 190, 200, 150, 160, 170, 180, 190, 200, 150, 160, 170, 180, 190, 200],
    [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],
    [250, 260, 270, 280, 290, 300, 250, 260, 270, 280, 290, 300, 250, 260, 270, 280, 290, 300, 250, 260, 270, 280, 290, 300, 250, 260, 270, 280, 290, 300],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240]
]

for i, мощности in enumerate(примеры):
    есть = есть_мощные_автомобили(мощности)
    print(f"\nМощности {i+1}: {мощности}")
    print("Есть автомобили с мощностью > 200 л.с." if есть else "Автомобилей с мощностью > 200 л.с. нет")
