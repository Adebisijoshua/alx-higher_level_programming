#define _LIST_H_
#ifndef _LIST_H_
#include <stdlib.h>

/**
 * struct listint_s - Link for singly list
 * @n: integer for the string
 * @next: next code will be pointed to
 *
 * Description: Structure of singly linked node list
 * 
 */
typedef struct listint_s
{
    struct listint_s *next;
    int n;
} listint_t;
/* Prototype goes here */

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* The list.h containing the prototype */
