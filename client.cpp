#include<iostream>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<stdlib.h>
#include<unistd.h>
#include<netdb.h>


using namespace std;

int main()
{
  int client,server,len;
  int portnum=8000;
  int bufsize=2012;
  char buffer[bufsize];
  char ip[]="127.0.0.1";
  struct sockaddr_in server_addr;
  client=socket(AF_INET,SOCK_STREAM,0);
  server_addr.sin_family=AF_INET;
  server_addr.sin_port=htons(portnum);
  connect(client,(struct sockaddr*)&server_addr,sizeof(server_addr));
  while(1){
  cout<<"Enter DATA"<<endl;
  cin>>buffer;
  len=strlen(buffer);
  bufsize=len;
  cout<<len<<endl;
  cout<<"runs"<<endl;
  send(client,buffer,bufsize,0);
  recv(client,buffer,bufsize,0);
  cout<<buffer<<endl;
  }

}
