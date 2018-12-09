## Kegiatan 1

##import socket
##
##hostname = 'localhost'
##pesan = ''
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.connect((hostname, 50001))
##print "Program Penjawab Data Diri"
##
##while pesan.lower() != 'q':
##    pesan = raw_input('perintah :')
##    s.send(pesan)
##    if pesan.lower() == 'keluar':
##        response = s.recv(1024)
##        print 'jawab', response
##        s.close()
##        break
##    elif pesan.lower() != 'keluar' :
##        response = s.recv(1024)
##        print 'jawab:', response
##s.close()
##

#Kegiatan 2

##import socket
##
##hostname = 'localhost'
##pesan = ''
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.connect((hostname, 50002))
##print "Program komunikasi server"
##
##while pesan.lower() != 'quit':
##    pesan = raw_input('komentar :')
##    s.send(pesan)
##    if pesan.lower() =='quit':
##        s.close()
##        break
##    elif pesan.lower() != 'quit':
##        response = s.recv(1024)
##        print 'Jawab: ', response
##        s.close()


# Kegiatan 3
import socket

hostname = 'localhost'
pesan =''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50004))
print "Menghitung Luas Bola"

while pesan != 'keluar' :
    pesan = raw_input('pesan: ')
    s.send(pesan)
    if pesan.lower() == 'keluar':
        response = s.recv(1024)
        print 'respon : '
        s.close()
        break
    elif pesan.lower() != 'keluar':
        response = s.recv(1024)
        print 'respon: ', response
s.close()
