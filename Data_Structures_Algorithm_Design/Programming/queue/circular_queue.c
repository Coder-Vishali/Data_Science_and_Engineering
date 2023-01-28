//Program for Circular Queue implementation through Array
#include <stdio.h>
#include<ctype.h>
#include<stdlib.h>
#define MAXSIZE 5
int cq[MAXSIZE];
int front,rear;

int main()
{
	void add(int,int);
	void del(int);
	int choice,i,num;
	front = -1;
	rear = -1;
	
	printf("\nProgram for Circular Queue demonstration through array");
	while(1)
	{
		printf("\n\nMAIN MENU\n1.INSERTION\n2.DELETION\n3.EXIT");
		printf("\n\nENTER YOUR CHOICE : ");
		scanf("%d",&choice);
		switch(choice)
		{
		case 1:
			printf("\n\nENTER THE QUEUE ELEMENT : ");
			scanf("%d",&num);
			add(num,MAXSIZE);
			break;
		case 2:
			del(MAXSIZE);
			break;
		case 3:
		    exit(0);
			default: printf("\n\nInvalid Choice . ");
		}

} //end of  outer while
return 0;
}               //end of main
void add(int item,int MAX)
{
	
	if(front ==(rear+1)%MAX)
	{
	printf("\n\nCIRCULAR QUEUE IS OVERFLOW");
	}
	else
	{
	  if(front==-1)
	    front=rear=0;
	    else
	    rear=(rear+1)%MAX;
	    cq[rear]=item;
	    printf("\n\nRear = %d    Front = %d ",rear,front);
	}
}
void del(int MAX)
{
int a;
if(front == -1)
	{
	printf("\n\nCIRCULAR QUEUE IS UNDERFLOW");
	}
	else
	{
		a=cq[front];
		if(front==rear)
		 front=rear=-1;
		else
		  front = (front+1)%MAX;
                printf("\n\nDELETED ELEMENT FROM QUEUE IS : %d ",a);
		printf("\n\nRear = %d    Front = %d ",rear,front);

	}
}
