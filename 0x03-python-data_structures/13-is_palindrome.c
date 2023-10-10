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
	listint_t *slow = *head, *fast = *head, *temp = *head, *reversed = NULL;

	if (head == NULL || *head == NULL)
		return (1);
	while (1)
	{
		reversed = fast->next;
		fast = fast->next->next;
		slow = slow->next;
		if (fast == NULL)
		{
			reversed_list(&slow);
			break;
		}
		if (fast->next == NULL)
		{
			reversed_list(&slow->next);
			reversed = fast;
			break;
		}
	}
	while (reversed != NULL)
	{
		if (reversed->n != temp->n)
			return (0);
		temp = temp->next;
		reversed = reversed->next;
	}
	return (1);
}

/**
 * reversed_list - reverse a singly linked list.
 *
 * @head: head of a linked list.
 *
 * Return: numbers.
 */

void reversed_list(listint_t **head)
{
	listint_t *current = *head;
	listint_t *previous = NULL;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
}
