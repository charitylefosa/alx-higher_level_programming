#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
*insert_node - insert int number into a sorted singly linked list
*@head: head of the list
*@number: number to be added
*
*Return: address of the new node
*	NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner;
	listint_t *new;

	runner = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (runner->next != NULL)
	{
		if ((runner->next)->n >= number)
		{
			new->next = runner->next;
			return (new);
		}
	}
	new->next = NULL;
	runner->next = new;
	return (new);
}
