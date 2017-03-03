import socket


sdata=[]
adata=''
print "prog starts"
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("127.0.0.1",8000))
sock.listen(2)
(client1,(ip1,port1))=sock.accept()
(client2,(ip2,port2))=sock.accept()
def rec():
    global sdata
    global adata
    try:
        rdata=''
        sdata[:]=[]
        client1.settimeout(1.0)
        rdata=client1.recv(2012)
        print rdata
        sdata=rdata.split(',')
        sdata.sort()
        for i in sdata:
            adata=adata+i+','
        adata=adata[:-1]
        client1.send(adata)
        rec()
    except:
        try:
            adata=''
            sdata[:]=[]
            client2.settimeout(1.0)
            rdata=client2.recv(2012)
            print rdata
            sdata=rdata.split(',')
            sdata.sort()
            for i in sdata:
                adata=adata+i+','
            adata=adata[:-1]
            client2.send(adata)
            rec()
        except:
            rec()
    rec()
   


rec()













