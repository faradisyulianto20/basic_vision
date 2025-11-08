import math

def hitung_jarak_jatuh_balistik():
    """
    Menghitung jarak horizontal (lead distance) yang diperlukan untuk 
    menjatuhkan paket agar tepat sasaran, berdasarkan prinsip 
    gerak jatuh bebas parabolik (mengabaikan hambatan udara).
    
    Versi ini menerima input dari pengguna.
    """

    # --- 1. KONSTANTA FISIKA ---
    g = 9.81  # Percepatan gravitasi (m/s^2)

    # --- 2. INPUT DARI PENGGUNA ---
    try:
        print("--- Masukkan Data Penerbangan (dalam satuan SI: meter, m/s) ---")
        
        # Meminta data penerbangan
        ketinggian_pesawat = float(input("Masukkan Ketinggian Pesawat (h): "))
        v_pesawat = float(input("Masukkan Kecepatan Horizontal Pesawat (v): "))
        
        print("\n--- Masukkan Data Posisi ---")
        # Meminta data posisi pesawat
        posisi_pesawat_X = float(input("Posisi X Pesawat Saat Ini: "))
        posisi_pesawat_Y = float(input("Posisi Y Pesawat Saat Ini: "))
        
        # Meminta data posisi target
        posisi_target_X = float(input("Posisi X Target: "))
        posisi_target_Y = float(input("Posisi Y Target: "))

        # Validasi input sederhana
        if ketinggian_pesawat <= 0:
            print("\nError: Ketinggian harus angka positif.")
            return
        if v_pesawat < 0:
            print("\nError: Kecepatan tidak boleh negatif.")
            return

    except ValueError:
        print("\nError: Input tidak valid. Harap masukkan angka.")
        return
    except Exception as e:
        print(f"Terjadi error: {e}")
        return

    # --- 3. PERHITUNGAN ---

    # Langkah A: Hitung Waktu Jatuh (Time of Flight)
    # Kita gunakan rumus gerak jatuh bebas vertikal:
    # h = (1/2) * g * t^2
    # Kita cari t: t = sqrt( (2 * h) / g )
    waktu_jatuh = math.sqrt((2 * ketinggian_pesawat) / g)

    # Langkah B: Hitung Jarak Horizontal (Drop Distance)
    # Ini adalah jarak yang akan ditempuh paket secara horizontal
    # selama ia jatuh. Paket mewarisi kecepatan horizontal pesawat.
    # d = v * t
    jarak_horizontal_jatuh = v_pesawat * waktu_jatuh

    # Langkah C: Hitung Jarak Aktual Pesawat ke Target
    # Menggunakan rumus jarak Euclidean (Pythagoras) di peta 2D.
    jarak_ke_target = math.sqrt(
        math.pow(posisi_target_X - posisi_pesawat_X, 2) +
        math.pow(posisi_target_Y - posisi_pesawat_Y, 2)
    )

    # --- 4. OUTPUT DAN KEPUTUSAN ---
    print("\n--- KALKULATOR DROP BALISTIK (IDEAL) ---")
    print(f"Input Ketinggian (h):      {ketinggian_pesawat:.2f} m")
    print(f"Input Kecepatan (v):       {v_pesawat:.2f} m/s")
    print(f"Waktu Jatuh (t) Terhitung: {waktu_jatuh:.2f} detik")
    print("---------------------------------------------")
    print(f"JARAK JATUH (d) YANG DIBUTUHKAN: {jarak_horizontal_jatuh:.2f} meter")
    print(f"Jarak Aktual ke Target:       {jarak_ke_target:.2f} meter")
    print("---------------------------------------------")

    # Logika keputusan rilis
    if jarak_ke_target <= jarak_horizontal_jatuh:
        print("KEPUTUSAN: LEPASKAN PAKET SEKARANG!")
    else:
        sisa_jarak = jarak_ke_target - jarak_horizontal_jatuh
        print(f"KEPUTUSAN: TAHAN. Maju {sisa_jarak:.2f} meter lagi.")


# Menjalankan program utama
if __name__ == "__main__":
    hitung_jarak_jatuh_balistik()