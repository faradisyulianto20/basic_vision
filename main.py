import cv2
import numpy as np

# Baca gambar
img = cv2.imread('apple.png')

# Ubah ke ruang warna HSV (lebih mudah buat deteksi warna)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# --- Threshold warna apel (contoh: apel merah) ---
# catatan: bisa diubah sesuai warna apel kamu (merah, hijau, kuning)
lower_red1 = np.array([0, 100, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 50])
upper_red2 = np.array([180, 255, 255])

# Bikin mask dari dua rentang merah
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

# Bersihkan sedikit noise kecil
mask = cv2.medianBlur(mask, 5)

# Simpan hasil
cv2.imwrite('mask_apel.png', mask)

# (Opsional) tampilkan
cv2.imshow('Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()