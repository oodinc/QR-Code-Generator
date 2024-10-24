import qrcode

def generate_qr_code(url, output_file):
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="#000000", back_color="white")
    img.save(output_file)

if __name__ == "__main__":
    # Tautan Google Maps yang akan diubah menjadi QR Code
    link_url = "https://.."
    
    # Nama file output
    output_file = "qrcode.png"
    
    generate_qr_code(link_url, output_file)
    print(f"QR Code telah disimpan sebagai {output_file}")
