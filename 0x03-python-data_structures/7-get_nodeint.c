#include "lists.h"
/**
* get_nodeint_at_index - return node in position inddex staring in 0.
* @head: pointer for head of lements.
* @index: index of node to get.
* Return: pointer to node.
*
*/
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int n;

	if (head)
	{
		for (n = 0; (n < index) && head; n++)
		{
			head = head->next;
		}
		return (head);
	}
	return (NULL);
}
