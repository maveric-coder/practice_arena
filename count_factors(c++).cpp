#include <iostream>

using namespace std;
int printDivisors(int n){
	int c=0;
	int i=1;
	while (i*i<=n){
		if (n%i==0)
	        c+=2;
	   	if (i*i==n)
	       c-=1;
	   	i+=1;

	}
	   
	return c;
}
int main(){
	int n;
	cin>>n;	
	while(n--){
		int zz=0;
		cin>>zz;
		cout<<(printDivisors(zz))<<"\n";
	}
}
