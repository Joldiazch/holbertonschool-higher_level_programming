#include "lists.h"
/**
* add_nodeint - print all elements of a list staring in head.
* @head: pointer for head of lements.
* @n: integer of new node.
* Return: pointer to new node.
*
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *temp;

	temp = malloc(sizeof(listint_t));
	if (!temp) /* if temp == NULL */
	{
		return (NULL);
	}
	temp->n = n;
	temp->next = (*head);
	/* To the "previus" head, becouse temp will be the new head */
	(*head) = temp;
	/* new head is temp */
	return (temp);
}
/**
* is_palindrome -  checks if a singly linked list is a palindrome
* @head: pointer for head of lements.
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*
*/
int is_palindrome(listint_t **head)
{
	listint_t *rev, *tem;
	int cont = 0, i;

	if (head)
	{
		if (!(*head))
			return (1);
		tem = *head;
		rev = NULL;
		while (tem)
		{
			cont++;
			add_nodeint(&rev, tem->n);
			tem = tem->next;
		}
		cont++;
		for (i = 1; i <= cont / 2; i++)
		{
			if (rev->n != (*head)->n)
			{
				free_listint(rev);
				return (0);
			}
			rev = rev->next;
			*head = (*head)->next;
		}
		free_listint(rev);
		return (1);
	}
	return (0);
}
