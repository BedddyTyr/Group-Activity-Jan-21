# Group-Activity-Jan-21
Persistent calculator

Members:

Marabe\
Misajon\
Orencia\
Samuya\
Sonquipal


# Second-Lab-Activity
## Execution-time
Method - Execution Order - GWA Output - Execution time\
Multithreading - Outputs are not ordered; threads execute concurrently. - 87.5 - 4.9298s\
Multiprocessing - Order varies because each process runs separately. - 87.50 - 0.519812s


1. Which approach demonstrates true parallelism in Python? Explain.
    - Multiprocessing demonstrates true parallelism because each process runs on a separate CPU core.
2. Compare execution times between multithreading and multiprocessing.
    - Multiprocessing (0.519812s) is faster.
3. Can Python handle true parallelism using threads? Why or why not?
    - No, due to the interpreter to being locked from global use.
4. What happens if you input a large number of grades (e.g., 1000)? Which
method is faster and why?
    - Multiprocessing is faster because it spreads computations across multiple cores.
5. Which method is better for CPU-bound tasks and which for I/O-bound
tasks?
    - Multiprocessing for CPU-bound and multithreading for I/O-bound.
6. How did your group apply creative coding or algorithmic solutions in this
lab?
    - The creative liberty utilized in this activity was the structuring of both programs to highlight parallel computing, this way both programs can be graded equally.
