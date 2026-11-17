"""Modul pelanggan: class Pelanggan beserta validasi datanya."""
from Exceptions import DataTidakValidError
from Penyewaan import Penyewaan


class Pelanggan:
    """Pelanggan rental. Atribut private dengan validasi lewat property."""

    def __init__(self, nama, id_pelanggan, no_sim):
        self.__nama = ""
        self.__id_pelanggan = ""
        self.__no_sim = ""
        self.__riwayat = []
        self.nama = nama
        self.id_pelanggan = id_pelanggan
        self.no_sim = no_sim

    # ---------------------------------------------------------- property
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nilai):
        nilai = str(nilai).strip()
        if len(nilai) < 2:
            raise DataTidakValidError("Nama pelanggan minimal 2 karakter.")
        self.__nama = nilai

    @property
    def id_pelanggan(self):
        return self.__id_pelanggan

    @id_pelanggan.setter
    def id_pelanggan(self, nilai):
        nilai = str(nilai).strip().upper()
        if not nilai or " " in nilai:
            raise DataTidakValidError(
                "ID pelanggan tidak boleh kosong atau mengandung spasi."
            )
        self.__id_pelanggan = nilai

    @property
    def no_sim(self):
        return self.__no_sim

    @no_sim.setter
    def no_sim(self, nilai):
        nilai = str(nilai).strip()
        if not nilai.isdigit() or not 8 <= len(nilai) <= 16:
            raise DataTidakValidError("Nomor SIM harus berupa 8 sampai 16 digit angka.")
        self.__no_sim = nilai

    @property
    def riwayat(self):
        """Daftar penyewaan milik pelanggan ini (salinan, agar tidak diubah dari luar)."""
        return list(self.__riwayat)

    # ------------------------------------------------------------ method
    def sewa_kendaraan(self, kendaraan, lama_sewa, tanggal_sewa=None):
        """Membuat dan memproses penyewaan; mengembalikan objek Penyewaan."""
        penyewaan = Penyewaan(self, kendaraan, lama_sewa, tanggal_sewa)
        penyewaan.proses_sewa()
        self.__riwayat.append(penyewaan)
        return penyewaan

    def kembalikan_kendaraan(self, penyewaan, tanggal_kembali=None):
        """Memproses pengembalian untuk penyewaan milik pelanggan ini."""
        if penyewaan.pelanggan is not self:
            raise DataTidakValidError("Penyewaan tersebut bukan milik pelanggan ini.")
        penyewaan.proses_pengembalian(tanggal_kembali)
        return penyewaan

    def __str__(self):
        return f"{self.id_pelanggan:<8} | {self.nama:<20} | SIM {self.no_sim}"