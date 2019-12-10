#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * cycle - prints all elements of a listint_t list
 * @tort: pointer to head of list
 * @lieb: pinter to tow step 
 * Return: 1 if is a cycle list o 0 in other case.
 */
int cycle(listint_t *tort, listint_t *lieb)
{
	if (lieb == tort)
		return (1);
	else if ( lieb == NULL || tort == NULL)
		return (0);
	else
		return (cycle(tort->next, lieb->next->next));	
}
/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: 1 if is a cycle list o 0 in other case.
 */
int check_cycle(listint_t *list)
{
	return (cycle(list, list->next->next));
}
