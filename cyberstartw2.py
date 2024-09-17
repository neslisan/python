# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    # İki nokta arasındaki farkları hesapla
    x_farki = point2[0] - point1[0]
    y_farki = point2[1] - point1[1]
    
    # Farkların karelerini topla
    toplam = (x_farki * x_farki) + (y_farki * y_farki)
    
    # Karekök almak için üs alma işlemini kullan (toplamın 0.5 kuvveti)
    mesafe = toplam ** 0.5
    
    return mesafe

# 2D uzaydaki noktalar (x, y)
points = [(2, 3), (4, 5), (1, 1), (6, 7)]

# Mesafeleri saklayacağımız liste
distances = []

# Mesafeleri hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)

print("Minimum mesafe:", min_distance)
