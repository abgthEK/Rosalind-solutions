# Organizing Strings of Different Lengths

In “Enumerating k-mers Lexicographically”, we introduced the lexicographic order for strings of the same length constructed from some ordered underlying alphabet. However, our experience with dictionaries suggests that we should be able to order strings of different lengths just as easily. That is, we already have an intuitive sense that "APPLE" comes before "APPLET", which comes before "ARTS," and so we should be able to apply this intuition toward cataloguing genetic strings of varying lengths.

# [Problem](http://rosalind.info/problems/lexv/)

Say that we have strings s = s1 s2⋯sm and t = t1 t2⋯tn with m<n. Consider the substring t′ = t[1:m]. 

We have two cases:

1. If s = t′, then we set s<Lext because s is shorter than t (e.g., APPLE<APPLET).

2. Otherwise, s ≠ t′. We define s < Lext if s < Lext′ and define s > Lext if s > Lext′ (e.g., APPLET < LexARTS because APPL < LexARTS).

Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n ≤ 4).

Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)

**Sample Dataset**

D N A

3

**Sample Output**

D
DD
DDD
DDN
DDA
DN
DND
DNN
DNA
DA
DAD
DAN
DAA
N
ND
NDD
NDN
NDA
NN
NND
NNN
NNA
NA
NAD
NAN
NAA
A
AD
ADD
ADN
ADA
AN
AND
ANN
ANA
AA
AAD
AAN
AAA