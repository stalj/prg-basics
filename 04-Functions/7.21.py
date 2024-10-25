def n_prime(number):
    prime=0
    count_primes=0
    i=2
    while count_primes!=number:
        while i>1:
            error=0
            for j in range(2,i+1):
                if i!=j and i%j==0:
                    error+=1
                    break    
            if error==0:
                prime=i
                count_primes+=1
            i+=1
            break      
                
    return prime