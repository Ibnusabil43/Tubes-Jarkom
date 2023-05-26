from socket import *
import os

# Alamat Server
HOST = '127.0.0.1'

# Port Server
PORT = 6604

# base directory folder
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


# http response
def http_response(file):
    response = ''  # inisisasi response

    # mengambil filename dari request dengan metode split
    filename = file.split(' ')[1]

    # menentukan filepath dengan menggabungkan base directory dengan filename menggunakan metode join
    if filename == "/":  # Jika memasukkan url tanpa filename maka akan membuka file_html.html
        filename = "/index.html"
    filepath = DIRECTORY + filename
    try:  # pengkondisian jika file ditemukan

        # membuka file dengan metode read binary
        content = open(filepath, 'rb').read()

        # Response message jika file ditemukan dan dapat dibuka
        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(content)}\r\n\r\n".encode(
            'utf-8')
        response += content

    except FileNotFoundError or IndexError:  # pengkondisian jika file tidak ditemukan

        # Response message jika file tidak ditemukan atau file tidak dapat dibuka
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode(
            'utf-8')
        response += "<h1>404 Not Found</h1>".encode('utf-8')
    return response


# Buat TCP Scoket
server_socket = socket(AF_INET, SOCK_STREAM)

# bind alamat dan port tertentu
server_socket.bind((HOST, PORT))

# Tunggu Koneksi masuk
server_socket.listen(2)

# Pesan konfirmasi bahwa server telah berjalan
print(f"Server berjalan di {HOST} port {PORT} (http://{HOST}:{PORT})......")

# Perulangan agar web server dapat selalu melayani client
while True:
   # Terima koneksi server
    connnectionSocket, addr = server_socket.accept()

    # Baca data yang dikirimkan client (parsing)
    file = connnectionSocket.recv(102400).decode()

    # memanggil fungsi http response untuk menampilkan http respons
    http_respons = http_response(file)

    # print method path dan protocol yang terdapat pada variabel request
    method, path, protocol = file.split('\n')[0].split()

    # pesan konfirmasi bahwa file berhasil dibuka
    print("FILE BERHASIL DIBUKA !!")
    print('Method :', method)
    filepath = os.path.join(DIRECTORY, file.split()[1][1:])
    print("Directory File .py : ", DIRECTORY)
    print('Path :', filepath)
    print('Protocol: ', protocol)

    # kirim response ke client
    connnectionSocket.sendall(http_respons)

    # tutup koneksi
    connnectionSocket.close()
