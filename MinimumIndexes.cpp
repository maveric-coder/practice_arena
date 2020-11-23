/*
// Sample code to perform I/O:

#include <iostream>

using namespace std;

int main() {
	int num;
	cin >> num;										// Reading input from STDIN
	cout << "Input number is " << num << endl;		// Writing output to STDOUT
}

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here

#include <iostream>
#include<bits/stdc++.h>
#define ll long long
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL);    
using namespace std;
int sum_dig(int n){
    int s=0;
    while (n)
    {
        
  
        s+=n%10;
        n/=10;
    }
    return s;
}
int main() {
    fast;
    ll n,q,a,x;
    cin>>n>>q;
	vector<ll> v;
	for(int i=0;i<n;i++)

        {

            cin>>a;

            v.push_back(a);

        }
	//q-=1;
	

	while (q--){
		
		cin>>x;
		
		if (x==n){
			cout<<"-1"<<"\n";

		}
        
    	else{

		

        a=v[x-1];
        ll b=0;
        ll j=x;
        int f=1;
        while (f==1 && j<n){
            if (a<v[j]){
                if (sum_dig(a)>sum_dig(v[j])){
                    f=0;
                    cout<<j+1<<"\n";
                    break;
				}
                else{
					j++;
				}
                    
			 }
            else{ 
				j++;
			}
        }
        if (f==1 ){
			cout<<"-1"<<"\n";
		}
         
		
	}

	}
    

    
    return 0;
}
