#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int infinite_while(void);

/**
 * main - function that creates 5 zombie processes
 * Return: Always 0 (Success)
 */

int main(void)
{
	int itr;
	pid_t zom_proc;

	for (itr = 1; itr <= 5; itr++)
	{
		zom_proc = fork();
		if (!zom_proc)
			return (0);
		printf("Zombie process created, PID: %d\n", zom_proc);
	}
	infinite_while();

	return (0);
}

/**
 * infinite_while - function that loops continually
 * Return: Always Success
 */

int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}
