n:read0`:projectEuler13.txt;   // read input data
//n:("123";"456";"78";"9") ;   // testing example
s:sum 0^("J"$'neg[max count each n]$(),)@/:n;
answer:10#raze string ({(0=first x)_x:(r,0)+0,x-10*r:x div 10}/) s;
answer


