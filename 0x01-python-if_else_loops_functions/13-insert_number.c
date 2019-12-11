#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - add new node in sorted linked list
 * @head: pointer to head of list
 * @number: number for node
 * Return: point to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *slow_point, *fast_point, *new;

	new = malloc(sizeof(listint_t));
	if (!new && !head)
	{
		free(new);
		return (NULL);
	}
	if (*head == NULL)
		return (add_nodeint_end(head, number));
	if ((number < (*head)->n))
	{
		new->next = *head;
		new->n = number;
		*head = new;
		return (new);
	}
	slow_point = *head;
	fast_point = (*head)->next;
	while (slow_point->next)
	{
		if ((number > slow_point->n) && (number < fast_point->n))
		{
			slow_point->next = new;
			new->next = fast_point;
			new->n = number;
			return (new);
		}
		else if ((number == slow_point->n) || (number == fast_point->n))
		{
			slow_point->next = new;
			new->next = fast_point;
			new->n = number;
			return (new);
		}
		slow_point = slow_point->next;
		fast_point = fast_point->next;
	}
	free(new);
	return (add_nodeint_end(head, number));
}
