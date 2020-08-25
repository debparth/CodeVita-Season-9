#include<iostream> 
#include<vector> 
#include<climits> 

using namespace std; 
int main()
{ int n; 
 cin>>n; 
 vector<int>oponents(n); 
 long int ans = INT_MIN; 
 for(int i=0;i<n;i++){ cin>>oponents[i]; } 
 for(int i = 0;i<n;i++)
 { long int temp = oponents[i];
  for(int j = 0;j<n;j++)
  {
    if(j<i)
    {
      if(j-1>=0)
      {
        temp+=(oponents[j]*oponents[i]+oponents[j-1]); }
      else temp+=(oponents[j]*oponents[i]); } 
    if(j>i)
    {
      if(j+1<n)
      {
        temp+=(oponents[j]*oponents[i]+oponents[j+1]); } 
      else temp+=(oponents[j]*oponents[i]); } 
  } 
  ans = max(ans,temp);  
 } 
 cout<<ans<<"\n"; 
 return 0; }