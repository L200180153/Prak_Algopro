# Kegiatan 1

##import socket
##
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.bind(("", 50001))
##s.listen(5)
##print "server sudah siap"
##data = ''
##kamus = {'Nama' : 'Anita Lusi Romadhon',
##         'NIM' : 'L200180153',
##         'Angkatan' : '2018',
##         'keluar' : 'siap!!!'}
##while data.lower() != 'keluar':
##    komm, addr =s.accept()
##    while data.lower() != 'keluar' :
##        data = komm.recv(1024)
##        print 'perintah:', data
##        if kamus.has_key(data):
##            komm.send(kamus[data])
##        else:
##            komm.send('Maaf, perintah tidak dimengerti')

### Kegiatan 2
##
##import socket
##import platform
##
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.bind(("", 50002))
##s.listen(5)
##print "server sudah siap"
##data = ''
##
##while data.lower() != 'quit':
##    komm, addr = s.accept()
##    while data.lower() != 'quit' :
##        data = komm.recv(1024)
##        print "komentar:", data
##        if data.lower() == 'machine':
##            respon = platform.machine()
##            komm.send(respon)
##        elif data.lower() == 'release' :
##            respon = platform.release()
##            komm.send(respon)
##        elif data.lower() == 'system':
##            respon = platform.system()
##            komm.send(respon)
##        elif data.lower() == 'version' :
##            respon = platform.version()
##            komm.send(respon)
##        elif data.lower() == 'node':
##            respon = platform.node()
##            komm.send(respon)
##        else :
##            komm.send('Tidak ada komentar')
####
### Kegiatan 3
    
import socket

def bola(r=0) :
    L = 4*3.14*r**2
    return L
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50004))
s.listen(5)
print "Server sudah siap"
data = ''

while 1 :
    komm, addr = s.accept()
    while data.lower() != 'keluar' :
        data = komm.recv(1024)
        print 'Pesan:', data
        if data.find("parameter") != -1 :
            param, value = data.split("=")
            if param == "parameter1":
                r = float(value)
                x = value
                komm.send("luas bola dengan jari-jari {} adalah {}".format(x,bola(r)))
            else:
                komm.send("Tidak ada")
