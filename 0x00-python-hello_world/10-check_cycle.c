#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *pointer2;
	listint_t *previous;

	pointer2 = list;
	previous = list;
	while (list && pointer2 && pointer2->next)
	{
		list = list->next;
		pointer2 = pointer2->next->next;

		if (list == pointer2)
		{
			list = previous;
			previous =  pointer2;
			while (1)
			{
				pointer2 = previous;
				while (pointer2->next != list && pointer2->next != previous)
				{
					pointer2 = pointer2->next;
				}
				if (pointer2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}