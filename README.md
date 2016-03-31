# engagement_db
# Purpose
We  build the database to pre calculate the input data

#Defined queries
- Preprocessing Input: 2 time series, X and Y, cut c 
- Query Input: start time t1, end time t2 
- Output: the actual correlation value between X and Y, and the estimate correlation value between X and Y using cut c. 

#Procedures: 
- Preprocessing after preprocessing input: 
    - [X] Normalize the X and Y with definition2. 
    - [X] Use the current cut c to cut both X and Y into smaller pieces. E.g. for N(X), I will have N(X) [0:c], N(X)[c:2c], N(X)[2c:3c]… etc. Same thing goes for N(Y). 
    - [ ] For each pair of N(X) and N(Y), calculate the Euclidean distance E between    each pair with definition 4. 
    - [ ] Store the results into E0, E1, E2 ….E2 For later retrieval. 
- Calculation after query input: 
    - [ ] The real correlationelation result of X[t1,t2] and Y[t1,t2]
    - [ ] The estimated result of X[t1,t2] and Y[t1,t2] using the closest cuts. 
#Thoughts
1. Should we use different compression methods. C. or should we appy data compression methods instead of having a thousand boxes, should we have 1000 points with a given error. 
2. Procedure is fine, we will devise a solution first. To use mssql or nosql. 



