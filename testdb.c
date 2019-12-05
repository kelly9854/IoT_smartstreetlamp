/*
 Pi_Serial_test.cpp - SerialProtocol library - demo
 Copyright (c) 2014 NicoHood.  All right reserved.
 Program to test serial communication

 Compile with:
 sudo gcc -o Pi_Serial_Test.o Pi_Serial_Test.cpp -lwiringPi -DRaspberryPi -pedantic -Wall
 sudo ./Pi_Serial_Test.o
 */

 // just that the Arduino IDE doesnt compile these files.
#ifdef RaspberryPi 

//include system librarys
#include "/usr/include/mariadb/mysql.h"
#include <stdio.h> //for printf
#include <stdint.h> //uint8_t definitions
#include <stdlib.h> //for exit(int);
#include <string.h> //for errno
#include <errno.h> //error output
#include <time.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

//wiring Pi
#include <wiringPi.h>
#include <wiringSerial.h>

#define PORT 8888

// Find Serial device on Raspberry with ~ls /dev/tty*
// ARDUINO_UNO "/dev/ttyACM0"
// FTDI_PROGRAMMER "/dev/ttyUSB0"
// HARDWARE_UART "/dev/ttyAMA0"
char device[] = "/dev/ttyACM0";
// filedescriptor
int fd;
unsigned long baud = 9600;
unsigned long ti = 0;

MYSQL *conn;
MYSQL_RES *res;
MYSQL_ROW row;

struct tm *t;
time_t timer;

char *serv = "localhost";
char *user = "root";
char *password = "ghqksdn";
char *database = "dustdb";
char str[100] = { 0 };
char buf1[100] = { 0 }, buf2[100] = { 0 }, buf3[2];
float num;
int i, len;
char ch;

int serverSock, clientSock;
struct sockaddr_in server, client;
int accp_sock, addrlen, bytes, dataSize, from_client, i;

//prototypes
int main(void);
void loop(void);
void setup(void);
void quit(char* msg, int retval);

void setup() {
   fflush(stdout);
   i = 0;

   addrlen = sizeof(client);

   if ((serverSock = socket(PF_INET, SOCK_STREAM, 0)) == -1) {
      quit("socket() failed", 1);
   }

   memset(&server, 0, sizeof(server));
   server.sin_family = AF_INET;
   server.sin_port = htons(PORT);
   server.sin_addr.s_addr = INADDR_ANY;

   if (bind(serverSock, (const void*)&server, sizeof(server)) == -1) {
      quit("bind() failed", 1);
   }

   if (listen(serverSock, 10) == -1) {
      quit("listen() failed.", 1);
   }

   accp_sock = accept(serverSock, (struct sockaddr*)&client, &addrlen);
   if (accp_sock < 0) {
      quit("accept() failed", 1);
   }

   //get filedescriptor
   if ((fd = serialOpen(device, baud)) < 0) {
      fprintf(stderr, "Unable to open serial device: %s\n", strerror(errno));
      exit(1); //error
   }

   //setup GPIO in wiringPi mode
   if (wiringPiSetup() == -1) {
      fprintf(stdout, "Unable to start wiringPi: %s\n", strerror(errno));
      exit(1); //error
   }

   conn = mysql_init(NULL);

   if (!mysql_real_connect(conn, serv, user, password, database, 0, NULL, 0)) {
      fprintf(stderr, "%s\n", mysql_error(conn));
      exit(1);
   }

   timer = time(NULL);
   t = localtime(&timer);

   sprintf(str, "create table dust%4d%02d%02d ( num float );", t->tm_year + 1900, t->tm_mon + 1, t->tm_mday);
   sprintf(buf1, "insert into dust%4d%02d%02d (num) values (", t->tm_year + 1900, t->tm_mon + 1, t->tm_mday);
   len = strlen(buf1);

   if (mysql_query(conn, str) != 0) {
      printf("query fail; err=%s\n", mysql_error(conn));
   }
}

void loop() {
   // Pong every 3 seconds
   if (millis() - ti >= 3000) {
      serialPuts(fd, "Pong!\n");
      // you can also write data from 0-255
      // 65 is in ASCII 'A'
      serialPutchar(fd, 65);
      ti = millis();
   }

   // read signal
   if (serialDataAvail(fd)) {
      char newChar = serialGetchar(fd);
      if (newChar == 13 || newChar == 10) {
         if (i > 0) {
            if (ch == 'p') {
               buf1[len] = 0;
               buf2[i] = ')';
               buf2[i + 1] = ';';
               buf2[i + 2] = 0;
               strcat(buf1, buf2);
               if (mysql_query(conn, buf1) != 0) {
                  printf("query fail; err=%s\n", mysql_error(conn));
               }
            }
            else if (ch == 'm') {
	       buf2[1] = 0;
               send(accp_sock, buf2, 1, 0);
            }
            i = 0;
         }
      }
      else {
         if (newChar != 'p' && newChar != 'm')
            buf2[i++] = newChar;
         else
            ch = newChar;

      }
      fflush(stdout);
   }

}

// main function for normal c++ programs on Raspberry
int main() {
   setup();
   while (1) loop();
   return 0;
}

void quit(char* msg, int retval) {
   if (retval == 0) {
      fprintf(stdout, (msg == NULL ? "" : msg));
      fprintf(stdout, "\n");
   }
   else {
      fprintf(stderr, (msg == NULL ? "" : msg));
      fprintf(stderr, "\n");
   }
}

#endif //#ifdef RaspberryPi
