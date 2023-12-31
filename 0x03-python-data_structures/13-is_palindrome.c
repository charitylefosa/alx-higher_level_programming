#include "lists.h"
#include <stddef.h>
listint_t *reverse_listint(listint_t **head);
int its_palindrome(listint_t **head);
/**
* reverse_listint - reverses a linked list
* @head: pointer to pointer to the head of the list
* Return: pointer to reversed list
*/
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head;
	listint_t *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

/**
* is_palindrome-checks if a singly linked list is a palindrome
* @head: pointer to pointer to the head of the list
* Return: 1 if the list is a palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	size_t size = 0, i;
	listint_t *rev, *tmp, *mid;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}
	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;
	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);
	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);
	return (1);
}
