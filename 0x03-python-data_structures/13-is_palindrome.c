#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1; // An empty list or a list with a single element is a palindrome

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    // Find the middle of the list using the two-pointer approach
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        // Reverse the first half of the list
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    // If the list has an odd number of elements, skip the middle element
    if (fast != NULL)
        slow = slow->next;

    // Compare the reversed first half with the second half
    while (slow != NULL)
    {
        if (prev->n != slow->n)
            return 0; // Not a palindrome

        prev = prev->next;
        slow = slow->next;
    }

    return 1; // Palindrome
}

int main(void)
{
    listint_t *head = NULL;

    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);

    print_listint(head);

    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);

    return 0;
}
