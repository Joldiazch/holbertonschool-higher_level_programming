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
