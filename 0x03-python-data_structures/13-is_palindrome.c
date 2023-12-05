#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of the linked list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
        if (head == NULL || *head == NULL)
                return (1);
        return (aux_palind(head, *head));
}

/**
 * aux_palind - auxiliary function to confirm if it is a palindrome
 * @head: pointer to the head of the linked list
 * @end: pointer to the end of the linked list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int aux_palind(listint_t **head, listint_t *end)
{
        if (end == NULL)
                return (1);

        if (aux_palind(head, end->next) && (*head)->n == end->n)
        {
                *head = (*head)->next;
                return (1);
        }

        return (0);
}
