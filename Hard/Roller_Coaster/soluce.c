int main(){
    long long L,C,N,a,j;
    scanf("%lu%lu%lu", &L, &C, &N);
    int t[N];
    int c[N];
    for (int i=0;i<N;i++) {
        scanf("%lu",&(t[i]));
        c[i]=0;
    }
    long long r=0;
    int i=0; 
    int s[N];
    for (int z=0;z<C;z++){
        a=0;j=0;
        int x=i;
        if (c[i] == 0){
            while ( a + t[i] <= L && j<N ) {
                a+=t[i];
                i+=1;
                i= i % N;
                j+=1;
            }
            c[x] = a;
            s[x] = i;
        } else{
            a = c[i];
            i = s[i];
        }
        r+=a;
    }
printf("%lu\n",r);
}



