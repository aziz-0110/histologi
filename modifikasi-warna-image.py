import cv2
import numpy as np

# Baca gambar input (grayscale atau biner)
img = cv2.imread('img_save/crop/img_crop_1_1.png', cv2.IMREAD_GRAYSCALE)

# Tentukan kernel untuk operasi morfologi
kernel = np.ones((5, 5), np.uint8)

# Lakukan operasi morfologi (misalnya opening)
morph_result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Konversi gambar hasil operasi morfologi ke BGR (warna)
morph_result_bgr = cv2.cvtColor(morph_result, cv2.COLOR_GRAY2BGR)
print(morph_result_bgr.shape)

# Tambahkan nilai warna pada setiap channel (B, G, R)
# Misalnya, tambahkan 100 ke channel biru (B)
morph_result_bgr[:, :, 0] = cv2.add(morph_result_bgr[:, :, 0], 10)  # Tambahkan ke channel biru
morph_result_bgr[:, :, 1] = cv2.add(morph_result_bgr[:, :, 1], 150)   # Tambahkan ke channel hijau
morph_result_bgr[:, :, 2] = cv2.add(morph_result_bgr[:, :, 2], 215)   # Tambahkan ke channel merah

# Tampilkan gambar hasil morfologi yang sudah diberi warna
cv2.imshow('Hasil Morfologi Berwarna', morph_result_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

