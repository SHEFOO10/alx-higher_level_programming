#include "lists.h"

/**
 * is_palindrome - a function checks if a singly linked list is a palindrome.
 *
 * @head: head of the singly linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */


int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *head_nodes = *head;
	listint_t *list_reversed = NULL;
	unsigned int i = 0;

	if (*head == NULL)
		return (1);
	while (temp != NULL)
	{
		i++;
		temp = temp->next;
	}
	if (i % 2 != 0)
		return (0);
	reversed_list(head, NULL, &list_reversed);

	temp = list_reversed;
	while (temp != NULL)
	{
		if (temp->n != (head_nodes)->n)
			return (0);
		temp = temp->next;
		head_nodes = head_nodes->next;
	}
	free_listint(list_reversed);
	return (1);
}


int reversed_list(
	listint_t **head,
	listint_t *previous_node,
	listint_t **list_reversed)
{
	if (*head == NULL)
		return (1);

	listint_t *node = NULL;

	previous_node = *head;
	node = (*head)->next;
	reversed_list(&node, previous_node, list_reversed);
	add_nodeint_end(list_reversed, previous_node->n);
	return (0);
}
