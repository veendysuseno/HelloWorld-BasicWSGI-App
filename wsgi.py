from app import application

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server('localhost', 8000, application)
    print("Serving on http://localhost:8000")
    server.serve_forever()

# Cara menjalankannya : python wsgi.py --> Klik Server akan mulai berjalan pada http://localhost:8000.

# Notes:
# Ini adalah entry point untuk server WSGI seperti Gunicorn.
# Menggunakan wsgiref.simple_server
# wsgiref.simple_server adalah server WSGI sederhana yang disediakan oleh 
# Python untuk keperluan pengembangan dan pengujian.

# Perbedaan Gunicorn dan (vs) wsgiref.simple_server
# Anda dapat memilih metode yang paling sesuai dengan kebutuhan Anda. 
# Gunicorn adalah pilihan yang baik untuk produksi, 
# sementara wsgiref.simple_server lebih cocok untuk pengembangan dan pengujian.