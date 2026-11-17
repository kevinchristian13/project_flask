from flask_wtf import FlaskForm
from wtforms import (
    StringField, IntegerField, SelectField,
    TextAreaField, SubmitField
)
from wtforms.validators import (
    DataRequired, Length, Email, NumberRange, Optional
)

# Form 1: Form Pemesanan / Kontak (Halaman Publik)
class PemesananForm(FlaskForm):
    nama_pemesan = StringField("Nama Lengkap", validators=[
        DataRequired(message="Nama wajib diisi."),
        Length(min=3, max=50, message="Nama harus 3–50 karakter.")
    ])
    email = StringField("Email", validators=[
        DataRequired(message="Email wajib diisi."),
        Email(message="Format email tidak valid.")
    ])
    produk = SelectField("Pilih Produk", choices=[
        ("kopi-susu", "Kopi Susu Gula Aren"),
        ("matcha-latte", "Matcha Latte"),
        ("roti-bakar", "Roti Bakar Cokelat")
    ])
    jumlah = IntegerField("Jumlah Pesanan", validators=[
        DataRequired(message="Jumlah wajib diisi."),
        NumberRange(min=1, max=50, message="Jumlah minimal 1 dan maksimal 50.")
    ])
    catatan = TextAreaField("Catatan Tambahan (Opsional)", validators=[
        Optional(),
        Length(max=200, message="Catatan maksimal 200 karakter.")
    ])
    submit = SubmitField("Kirim Pesanan")


# Form 2: Form Tambah Produk (Dashboard Admin)
class ProdukForm(FlaskForm):
    nama = StringField("Nama Produk", validators=[
        DataRequired(message="Nama produk wajib diisi."),
        Length(min=3, max=50, message="Nama produk harus 3–50 karakter.")
    ])
    kategori = SelectField("Kategori", choices=[
        ("makanan", "Makanan"),
        ("minuman", "Minuman"),
        ("snack", "Snack")
    ])
    harga = IntegerField("Harga (Rp)", validators=[
        DataRequired(message="Harga wajib diisi."),
        NumberRange(min=1000, message="Harga minimal Rp 1.000.")
    ])
    stok = IntegerField("Stok", validators=[
        DataRequired(message="Stok wajib diisi."),
        NumberRange(min=0, message="Stok tidak boleh negatif.")
    ])
    deskripsi = TextAreaField("Deskripsi Produk", validators=[
        Optional(),
        Length(max=250, message="Deskripsi maksimal 250 karakter.")
    ])
    submit = SubmitField("Tambah Produk")