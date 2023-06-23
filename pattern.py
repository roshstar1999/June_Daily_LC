class Solution {
  public:
    void printTriangle(int n) {
        for (int i=1;i<=n;i++){
            for (int j=1;j<=2*n;j++){
                if (j<=i or 2*n-j+1<=i){
                    cout<<"*";
                }
                else cout<<" ";
            }
            cout<<endl;
            
        }
        
        for (int i=n-1;i>=1;i--){
            for (int j=1;j<=2*n;j++){
                if (j<=i or 2*n-j+1<=i){
                    cout<<"*";
                }
                else cout<<" ";
            }
            cout<<endl;
            
        }


'''
#optimised solution
class Solution {
  public:
    void printTriangle(int n) {
        int spaces=2*n-2;
        for (int i=1;i<=2*n;i++){
            int stars=i;
            if (i>n) stars=2*n-i;
            
            //print stars
            for (int a=1;a<=stars;a++) cout<<"*";
            
            //print spaces
            for (int a=1;a<=spaces;a++) cout<<" ";
            
            
            //print stars
            for (int a=1;a<=stars;a++) cout<<"*";
            
            if (i>=n) spaces+=2;
            else spaces-=2;
            
            cout<<endl;

        '''
        
