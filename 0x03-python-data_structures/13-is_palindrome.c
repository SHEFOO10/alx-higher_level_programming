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
	listint_t *temp = NULL;
	listint_t *head_nodes = *head;
	listint_t *list_reversed = NULL;

	if (*head == NULL)
		return (1);

	reversed_list(head, &list_reversed);
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

/**
 * reversed_list - reverse a singly linked list.
 *
 * @head: head of a linked list.
 * @list_reversed: empty list to be filled.
 *
 * Return: numbers.
 */

void reversed_list(listint_t **head, listint_t **list_reversed)
{
	listint_t *node;

	if (*head == NULL)
		return;
	node = (*head)->next;
	reversed_list(&node, list_reversed);
	add_nodeint_end(list_reversed, (*head)->n);
}
