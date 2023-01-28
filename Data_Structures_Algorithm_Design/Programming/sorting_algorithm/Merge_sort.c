Example:  3  5  2  6  8

################################################################

here is the sequence of calls:
a[] = {3, 5, 2, 6, 8}
low = 0; high = 4;
mergesort(a, 0, 4) 
mid = 0 + 4 / 2 = 2
mergesort(a, 0, 2)
mergesort(a, 3, 4)
merge(a, 0, 4, 2)

So, each of the mergesort() calls will again go back and call mergesort() and merge(),
this goes on till: (low < high) is satisfied.

################################################################

mergesort(int a[], int low, int high)
{
int mid;
if(low<high)
{
mid=(low+high)/2;
mergesort(a,low,mid);
mergesort(a,mid+1,high);
merge(a,low,high,mid);
}
return(0);
}

merge(int a[], int low, int high, int mid)
{
int i, j, k, c[50];
i=low;
j=mid+1;
k=low;
while((i<=mid)&&(j<=high))
{
if(a[i]<a[j])
{
c[k]=a[i];
k++;
i++;
}
else
{
c[k]=a[j];
k++;
j++;
}
}
while(i<=mid)
{
c[k]=a[i];
k++;
i++;
}
while(j<=high)
{
c[k]=a[j];
k++;
j++;
}
for(i=low;i<k;i++)
{
a[i]=c[i];
}
} 
