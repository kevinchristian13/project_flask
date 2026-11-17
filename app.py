from flask import Flask, render_template, redirect, url_for, flash
from forms import PemesananForm, ProdukForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "kunci-rahasia-tugas-7-flask"

# Penyimpanan data sementara di memori (list Python)
daftar_pesanan = []
daftar_produk = [
    {"nama": "Kopi Susu Gula Aren", "kategori": "minuman", "harga": 18000, "stok": 25, "deskripsi": "Espresso dengan susu segar dan gula aren."},
    {"nama": "Roti Bakar Cokelat", "kategori": "makanan", "harga": 15000, "stok": 10, "deskripsi": "Roti panggang renyah dengan selai cokelat lumer."}
]

@app.route("/", methods=["GET", "POST"])
def pesan():
    form = PemesananForm()
    if form.validate_on_submit():
        daftar_pesanan.append({
            "nama_pemesan": form.nama_pemesan.data,
            "email": form.email.data,
            "produk": dict(form.produk.choices).get(form.produk.data),
            "jumlah": form.jumlah.data,
            "catatan": form.catatan.data or "-"
        })
        flash(f"Pesanan atas nama {form.nama_pemesan.data} berhasil dikirim!", "success")
        return redirect(url_for("pesan"))  # Pola PRG

    return render_template("pesan.html", form=form, daftar_pesanan=daftar_pesanan)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    form = ProdukForm()
    if form.validate_on_submit():
        daftar_produk.append({
            "nama": form.nama.data,
            "kategori": form.kategori.data,
            "harga": form.harga.data,
            "stok": form.stok.data,
            "deskripsi": form.deskripsi.data or "-"
        })
        flash(f"Produk '{form.nama.data}' berhasil ditambahkan!", "success")
        return redirect(url_for("admin"))  # Pola PRG

    return render_template("admin.html", form=form, daftar_produk=daftar_produk)


if __name__ == "__main__":
    app.run(debug=True)