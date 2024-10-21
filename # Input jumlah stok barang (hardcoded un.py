def pengelolaan_penjualan():
    stok = 100  # Misalkan stok awal adalah 100
    while True:
        jumlah_dijual = int(input("Masukkan jumlah barang yang ingin dijual (0 untuk keluar): "))
        if jumlah_dijual == 0:
            break  # Keluar dari loop jika input adalah 0
        if jumlah_dijual > stok:
            print("Stok tidak cukup.")
        else:
            stok -= jumlah_dijual
            print(f"Sisa stok: {stok}")

pengelolaan_penjualan()
