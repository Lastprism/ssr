#include<WINSOCK2.H>
#include<STDIO.H>
#include<iostream>
#include<cstring>
using namespace std;

#pragma comment(lib, "ws2_32.lib")

int client(const char* add,int port,string data1)
{
    WORD sockVersion = MAKEWORD(2, 2);
	WSADATA data;
	if(WSAStartup(sockVersion, &data)!=0)
	{
		return 0;
	}

	//
    SOCKET sclient = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if(sclient == INVALID_SOCKET)
    {
        printf("invalid socket!");
        return 0;
    }

    sockaddr_in serAddr;
    serAddr.sin_family = AF_INET;
    serAddr.sin_port = htons(port);
    serAddr.sin_addr.S_un.S_addr = inet_addr(add);
    if(connect(sclient, (sockaddr *)&serAddr, sizeof(serAddr)) == SOCKET_ERROR)
    {  //����ʧ��
        printf("connect error !");
        closesocket(sclient);
        return 0;
    }

    //string data1;
    //cin>>data;
    const char * sendData;
    sendData = data1.c_str();   //stringתconst char*
    //char * sendData = "��ã�TCP����ˣ����ǿͻ���\n";
    send(sclient, sendData, strlen(sendData), 0);
    //send()������������ָ����socket�����Է�����
    //int send(int s, const void * msg, int len, unsigned int flags)
    //sΪ�ѽ��������ӵ�socket��msgָ���������ݣ�len��Ϊ���ݳ��ȣ�����flagsһ����0
    //�ɹ��򷵻�ʵ�ʴ��ͳ�ȥ���ַ�����ʧ�ܷ���-1������ԭ�����error

    char recData[1024];
    int ret = recv(sclient, recData, 1024, 0);
    if(ret>0){
        recData[ret] = 0x00;
        printf(recData);
    }
    closesocket(sclient);
	WSACleanup();
}
int main()
{
    //cout<<"e"<<endl;
    client("101.200.42.79",10010,"1");
    system("pause");
	return 0;

}

