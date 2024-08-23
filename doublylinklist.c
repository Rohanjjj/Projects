#include <stdio.h>
#include <stdlib.h>

struct node {
    int info;
    struct node *rlink;
    struct node *llink;
};

typedef struct node *NODE;

NODE getnode() {
    NODE x;
    x = (NODE)malloc(sizeof(struct node));
    if (x == NULL) {
        printf("Memory allocation failed\n");
        exit(0);
    }
    return x;
}

NODE In_f(int item, NODE first) {
    NODE temp = getnode();
    temp->info = item;
    temp->llink = NULL;
    temp->rlink = first;

    if (first != NULL) {
        first->llink = temp;
    }

    first = temp;
    return first;
}

NODE In_r(int item, NODE first) {
    NODE temp = getnode();
    temp->info = item;
    temp->rlink = NULL;

    if (first == NULL) {
        temp->llink = NULL;
        return temp;
    }

    NODE cur = first;
    while (cur->rlink != NULL) {
        cur = cur->rlink;
    }

    cur->rlink = temp;
    temp->llink = cur;
    return first;
}

NODE In_p(int item, NODE first, int pos) {
    NODE temp = getnode();
    temp->info = item;
    temp->rlink = NULL;
    temp->llink = NULL;

    if (pos == 1) {
        temp->rlink = first;
        if (first != NULL) {
            first->llink = temp;
        }
        return temp;
    }

    NODE cur = first;
    int count = 1;

    while (cur != NULL && count < pos - 1) {
        cur = cur->rlink;
        count++;
    }

    if (cur == NULL) {
        printf("Position out of range\n");
        return first;
    }

    temp->rlink = cur->rlink;
    if (cur->rlink != NULL) {
        cur->rlink->llink = temp;
    }
    cur->rlink = temp;
    temp->llink = cur;

    return first;
}

NODE del_f(NODE first) {
    NODE temp;
    if (first == NULL) {
        printf("List is empty\n");
        return NULL;
    }

    temp = first;
    first = first->rlink;
    if (first != NULL) {
        first->llink = NULL;
    }

    free(temp);
    return first;
}

NODE del_r(NODE first) {
    if (first == NULL) {
        printf("List is empty\n");
        return NULL;
    }

    NODE cur = first;
    while (cur->rlink != NULL) {
        cur = cur->rlink;
    }

    if (cur->llink != NULL) {
        cur->llink->rlink = NULL;
    } else {
        first = NULL;  // The list becomes empty
    }

    free(cur);
    return first;
}

NODE del_p(NODE first, int pos) {
    if (first == NULL) {
        printf("List is empty\n");
        return NULL;
    }

    NODE cur = first;

    if (pos == 1) {
        return del_f(first); 
    }

    int count = 1;
    while (cur != NULL && count < pos) {
        cur = cur->rlink;
        count++;
    }

    if (cur == NULL) {
        printf("Position out of range\n");
        return first;
    }

    if (cur->rlink != NULL) {
        cur->rlink->llink = cur->llink;
    }

    if (cur->llink != NULL) {
        cur->llink->rlink = cur->rlink;
    }

    free(cur);
    return first;
}

void print(NODE first) {
    NODE cur = first;
    if (cur == NULL) {
        printf("List is empty\n");
        return;
    }

    while (cur != NULL) {
        printf("%d ", cur->info);
        cur = cur->rlink;
    }
    printf("\n");
}

void main() {
    NODE first = NULL;
    int choice, item, pos;

    while (1) {
        printf("\n1. Insert at Front\n");
        printf("2. Insert at Rear\n");
        printf("3. Insert at Position\n");
        printf("4. Delete from Front\n");
        printf("5. Delete from Rear\n");
        printf("6. Delete from Position\n");
        printf("7. Print List\n");
        printf("8. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the item to insert at front: ");
                scanf("%d", &item);
                first = In_f(item, first);
                break;
            case 2:
                printf("Enter the item to insert at rear: ");
                scanf("%d", &item);
                first = In_r(item, first);
                break;
            case 3:
                printf("Enter the item to insert: ");
                scanf("%d", &item);
                printf("Enter the position to insert: ");
                scanf("%d", &pos);
                first = In_p(item, first, pos);
                break;
            case 4:
                first = del_f(first);
                break;
            case 5:
                first = del_r(first);
                break;
            case 6:
                printf("Enter the position to delete: ");
                scanf("%d", &pos);
                first = del_p(first, pos);
                break;
            case 7:
                print(first);
                break;
            case 8:
                printf("Thank you\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
}