#include<stdio.h>
#include<stdlib.h>

struct list // a node in the linked list
{
    int data;
    struct list *link;
};

struct list *first=NULL;

void insert_rear()
{

    struct list *temp,*cur,*prev;

    temp=(struct list*)malloc(sizeof(struct list));
    printf("\nEnter the data=");
    scanf("%d", &temp->data);
    temp->link=NULL;
    if(first==NULL)
    {
        first=temp;
        return;
    }
    if(first->link==NULL)
    {
        first->link=temp;
        return;
    }
    cur=first;
    
    while(cur->link!=NULL)
    {
        
        cur=cur->link;
    }
 cur->link=temp;
}

void remove_first()
{
    struct list *temp;

    if(first==NULL)
    {
        printf("\nList is empty");
        return ;
    }
    temp=first;
    first=first->link;
    printf("\nDeleted item=%d", temp->data);
    free(temp);
}


void remove_rear()
{

if(first==NULL)
    {
        printf("List is empty");
        return;
    }
    if(first->link==NULL)
    {
       temp = first;
	free(temp);
	first=NULL;
        return;
    }
    cur=first->link;
    prev=first;
    while(cur->link!=NULL)
    {
        prev=cur;
        cur=cur->link;
    }
prev->link=NULL;
free(cur);
}

void display()
{
    struct list *temp;

    if(first==NULL)
    {
        printf("\nList is empty");
        return ;
    }
    printf("\nList content....\n");
    temp=first;
    while(temp != NULL)
    {
        printf("%d ", temp->data);
        temp=temp->link;
    }
    printf("\n");
}

int main()
{
    int ch;

    for(;;)
    {
        printf("\n1.Insert\n2.Remove\n3.Display\n4.Exit");
        printf("\nEnter your choice=");
        scanf("%d", &ch);
        switch(ch)
        {
            case 1: insert_rear();
                    break;

            case 2: remove_first();
                    break;

            case 3: display();
                    break;

            case 4: exit(0);
        }
    }

        return 0;
}
