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
        