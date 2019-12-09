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
	listint_t *temp_lie;
	temp_lie = list->next->next;

	if (temp_lie == list)
		return (1);
	else if ( list == NULL || temp_lie == NULL)
		return (0);
	else
		check_cycle(list->next);
	return(0);
}
