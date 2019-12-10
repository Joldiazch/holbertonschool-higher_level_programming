#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: 1 if is a cycle list o 0 in other case.
 */
int check_cycle(listint_t *list)
{
	listint_t *tort, *lieb;

	tort = list;
	lieb = list;
	if (list)
	{
		while (tort && tort->next && lieb && lieb->next)
		{
			tort = tort->next;
			lieb = lieb->next->next;
			if (lieb == tort)
				return (1);
		}
	}
	return (0);
}
