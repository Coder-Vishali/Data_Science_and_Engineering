int size=10;
int arr[size]; //this will be considered stack container
int top=-1;

void push(int ele)
{
 if(top==size-1) // check it's full or not
 {
	print("Stack is full");
	return;
 }
 arr[++top] = ele;
}

int pop() //remove an ele from stack
{
 int ele;
 if(top==-1)
 {
	print("Stack is empty");
	return -999;
 }
 ele =  arr[top--];
 return ele;
}

void display() // Show list of elements in the stack
{

int ele;
 if(top==-1)
 {
	print("Stack is empty");
	return ;
 }
 for(ele=top;ele>=0;ele--)
 print(arr[ele]);
}
