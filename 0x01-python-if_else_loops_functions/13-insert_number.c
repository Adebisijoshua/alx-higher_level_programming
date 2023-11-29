/* File name : 13_insert_numbers
 * Author : Adekunle Joshua Adebisi
 * Gmail :Adekunle8k@gmail.com
*/


#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - put node in mode to linkedlist
 * @head: head
 * @number: num that will be added
 * Return: the address for the new code
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *actual = *head;

	if (!new)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n > number)/* If condition */
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (actual->next)/* while condition */
	{
		if ((actual->next)->n >= number)
		{
			new->next = actual->next;
			actual->next = new;
			return (new);
		}
		actual = actual->next;
	}

	new->next = NULL;
	actual->next = new;

	return (new);/* return */
}
