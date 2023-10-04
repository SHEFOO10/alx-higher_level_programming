#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - nserts a number into a sorted singly linked list.
 *
 * @head: head of the singly linked list.
 * @number: number value for new node.
 *
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNumber;
	listint_t *temp;

	temp = *head;
	newNumber = malloc(sizeof(listint_t));
	newNumber->n = number;

	if (*head == NULL)
		*head = newNumber;

	while (temp)
	{
		if (temp->next == NULL)
			add_nodeint_end(head, number);
		if (temp->n < number && temp->next->n > number)
		{
			newNumber->next = temp->next;
			temp->next = newNumber;
			break;
		}
		temp = temp->next;
	}
	return (newNumber);
}
