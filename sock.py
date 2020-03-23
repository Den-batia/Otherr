
import socket
import select

tasks = []
to_read = {}
to_write = {}

serv_sock = socket.socket()
serv_sock.bind(('', 9000))
serv_sock.listen()


def server():
    while True:
        yield ('r', serv_sock)
        conn, adrr = serv_sock.accept()
        tasks.append(client(conn))


def client(conn):
    while True:
        yield ('r', conn)
        data = conn.recv(1024)
        if not data:
            break
        else:
             yield ('w', conn)
             conn.send(data.upper())

    conn.close()

tasks.append(server())

def loop():
    while True:
        while not tasks:
            r_to_r, r_to_w, _ = select.select(to_read, to_write, ())
            for i in r_to_r:
                tasks.append(to_read.pop(i))
            for i in r_to_w:
                tasks.append(to_write.pop(i))


        gen = tasks.pop(0)
        mask, conn = next(gen)
        if (mask == 'r'):
            to_read[conn] = gen
        if (mask == 'w'):
            to_write[conn] = gen

        # except Exception as e:
        #     print(e)





if __name__ == '__main__':
    loop()