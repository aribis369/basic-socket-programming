import socket


sdata=[]
adata=''
print "prog starts"
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("127.0.0.1",8000))
sock.listen(2)
(client,(ip,port))=sock.accept()
def rec():
    global sdata
    global adata
    rdata=client.recv(2012)
    print rdata
    sdata=rdata.split(',')
    sdata.sort()
    for i in sdata:
        adata=adata+i+','
    adata=adata[:-1]
    client.send(adata)
    adata=''
    rec()
   


rec()













