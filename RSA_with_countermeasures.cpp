#include <bits/stdc++.h>
using namespace std;
long long time_count =0;
long long p, q, n, phi, enc_key[100], dec_key[100], enc_msg[100], msg_val[100];
char msg[100];
long long posKeysLen=0;

// Functions to find keys from given prime numbers
void find_key();
long long find_d(long long );

// Encryption and Decryption function for RSA algorithm
void encrypt();
void decrypt();

// Arithmatic operations with different latencies
long long opAdd(long long, long long);
long long opSub(long long, long long);
long long opMult(long long, long long);
long long opDiv(long long, long long);
long long opMod(long long,long long);

// Parallel compensation code and its fixed latency
void parallel_compensationCode();
long long fixed_latency = 15777857 ;

bool prime(long long);



int main()
{
    
    cout<<"\nENTER FIRST PRIME NUMBER :\n";
    cin >> p;
    bool flag =prime(p);
    if(flag ==false)
    {
        cout<<"\nWRONG INPUT\n";
        exit(1);
    }

    cout<<"\nENTER ANOTHER PRIME NUMBER :\n";
    cin>>q;
    flag = prime(q);
    if(flag ==false or p==q)
    {
        cout<<"\nWRONG INPUT\n";
        exit(1);
    }
    cout<<"\nENTER MESSAGE :\n";
    fflush(stdin);
    cin>> msg;
    for(long long i=0; msg[i] != '\0' ; i++)
    {
        msg_val[i] =  msg[i];
    }

    n = p*q;
    phi= (p-1)* (q-1);

    find_key();

    //cout<<"POSSIBLE VaLUES of e and d ARE\n";
    // for(long long i=0; i<posKeysLen; i++)
    // {
    //     cout<<enc_key[i]<<"\t"<<dec_key[i]<<endl;
    // }

    time_count=0;
    encrypt();

    time_count=0;
    decrypt();
    return 0;

}

void find_key()
{
    long long k;
    k=0;
    for(long long i=2; i< phi ;i++)
    {
        if( phi % i ==0 )continue;
        bool flag = prime(i);
        if(flag==true && i!= p && i!=q)
        {
            enc_key[k]=i;
            long long d = find_d(i);
            if(d>0 )
            {
                dec_key[k] = d;
                posKeysLen++;
                k++;
            }
            if(k==99)break;
        }
    }
}

long long find_d(long long e)
{
    long long k=1;
    while(1)
    {
        k=k+phi;
        if(k % e == 0)
        {
            return k/e;
        }
    }
}

void encrypt()
{
    long long key= enc_key[0];
    //cout<<"key "<<key<<endl;
    long long len= strlen(msg);
    long long i=0;

    long long temp=0;


    // Removing iteration count dependency on secret variable
    // replacing len(secret_variable) with 100 
    while(i < 100)
    {
        // Balancing branches 
        if(i<len)
        {
            long long m = msg_val[i];
            long long k = 1;

            for(long long j = 0; j < key ; j++)
            {
                long long time_stamp = time_count;

                // Calling fixed latency parallel compensation code
                thread t1(parallel_compensationCode);

                k=opMult(k,m);
                k=opMod(k,n);
            
                //Waiting for the completion of parallel compensation code
                t1.join();

                if(time_count < time_stamp + fixed_latency)
                {
                    time_count = time_stamp + fixed_latency;
                }
            }
            enc_msg[i] = k;
            time_count += (5*577);
            temp++;
        }

        //Same latency compensation code to mitigate dependency on len(secret_variable)
        if(i>=len)
        {
            long long k = 1;
            long long m=100;
            for(long long j=0; j< key ; j++)
            {
                
                long long time_stamp=time_count;

                // Calling fixed latency parallel compensation code
                thread t1(parallel_compensationCode);

                k=opMult(k,m);
                k=opMod(k,n);
                
                //Waiting for the completion of parallel compensation code
                t1.join();

                if(time_count < time_stamp + fixed_latency)
                {
                    time_count = time_stamp +fixed_latency;
                }

                
            }

            long long dummy1= 29;

            time_count+=(5*577);

        }
        i++;
        
    }
    enc_msg[temp]=-1;

    time_count+=(6*577);


    cout<<"\nENCRYPTED MESSAGE IS :\t";
    for(i=0; enc_msg[i]!=-1 ; i++)
    {
        cout<<(char)(enc_msg[i]);
    }
    cout<<endl;
    cout<<"Time elapsed in encryption =  "<<time_count<<endl;
}

void decrypt()
{
    long long key = dec_key[0];
    long long i=0;
    while(enc_msg[i] !=-1)
    {
        long long ct= enc_msg[i];
        long long k=1;

        // Removing iteration count dependency on private key
        for(long long j=0; j<10000 ;j++)
        {
            if(j<key)
            {
                long long time_stamp=time_count;

                // Calling fixed latency parallel compensation code
                thread t1(parallel_compensationCode);

                k=opMult(k,ct);
                k=opMod(k,n);

                //Waiting for the completion of parallel compensation code
                t1.join();

                if(time_count < time_stamp + fixed_latency)
                {
                    time_count = time_stamp +fixed_latency;
                }
            }
            if(j>=key)
            {
                long long time_stamp=time_count;

                // Calling fixed latency parallel compensation code
                thread t1(parallel_compensationCode);

                long long dummy=1;
                dummy=opMult(dummy,ct);
                dummy=opMod(dummy,n);

                //Waiting for the completion of parallel compensation code
                t1.join();

                if(time_count < time_stamp + fixed_latency)
                {
                    time_count = time_stamp +fixed_latency;
                }


            }

            
            
        }
        msg_val[i]= k;
        i++;

        time_count += (5*577);
    }
    msg_val[i] =-1;

    time_count += (5*577);

    cout<<"\nDECRYPTED MESSAGE IS :\t";
    for(i=0; msg_val[i]!=-1 ; i++)
    {
        cout<<(char)msg_val[i];
    }
    cout<<endl;

    cout<<"Time elapsed in decryption =  "<<time_count<<endl<<endl;
}

//Functions

long long opAdd(long long a, long long b)
{
    time_count += 9929;
    return (a+b);
}

long long opSub(long long a, long long b)
{
    time_count += 7789;
    return (a-b);
}

long long opMult(long long a, long long b)
{
    long long cnt = 997;
    for(long long i=63;i>=1;i--)
    {
        if((a&(1<<i))!=0)
        {
            cnt=cnt*i;
            break;
        }
    }
    for(long long i=63;i>=1;i--)
    {
        if((b&(1<<i))!=0)
        {
            cnt=cnt*i;
            break;
        }
    }
    time_count+=cnt;
    return (a*b);
}
long long opDiv( long long a, long long b)
{
    long long cnt = 2293;
    for(long long i=63;i>=1;i--)
    {
        if((a&(1<<i))!=0)
        {
            cnt=cnt*i;
            break;
        }
    }
    time_count+=cnt;
    return (a/b);

}

long long opMod(long long a, long long b)
{
    long long cnt = 1831;
    for(long long i=63;i>=1;i--)
    {
        if((a&(1<<i))!=0)
        {
            cnt=cnt*i;
            break;
        }
    }
    time_count+=cnt;
    return (a%b);

}

void parallel_compensationCode()
{
    long long k=789893;
    long long m=129323;
    long long n=11921019;
    for(int i=0;i<5;i++)
    {
        k=k*m;
        k=k%n;
    }
    return;
    
}

bool prime( long long val)
{
    long long sq=(long long)sqrt(val);
    for(long long i=2;i<=sq;i++)
    {
        if(val % i ==0)return false;
    }
    return true;
} 

// SAT Problem for encryption part

// Phi( public_key , m1 ) = {c1, t1}
// Phi( public_key , m2 ) = {c2, t2}

// SAT Problem
// (c1 != c2 ) || (t1 != t2)

// If SAT   -> Not verified
// If UNSAT -> Verified

//Program Execution
// g++ RSA_with_countermeasures.cpp -pthread
// ./a.out

