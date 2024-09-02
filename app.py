import os

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    # Path ke file template
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    
    # Membaca isi template
    with open(template_path, 'r') as file:
        response_body = file.read()

    # Mengembalikan respon dengan template HTML
    return [response_body.encode('utf-8')]
