int size=10;
int q[size]; /array as a queue
int f=0,r=-1; //front and rear index variables

void insert(int ele) //
{
 	if(r==size-1)
	{
		print("Queue is full");
		return;
	}
    	q[++r] = ele;
}

int del()
{
	int ele;
	if(f>r) //
	{
		print("Queue is empty");
		return -1;
	}
	ele = q[f++];
	return ele;
}

void display()
{

	int i;
	if(f>r)
	{
		print("Queue is empty");
		return;
	}
	for(i=f;i<=r;i++)
	print(q[i]);
}
