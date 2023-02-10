# CMPS 2200  Recitation 02

**Name (Team Member 1):**_____Jiayi xu____________  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Make sure you have a Github account.
- Login to Github.
- Login to repl.it, using "sign in with github"
- Click on the assignment link sent through canvas and accept the assignment.
- Click on your personal github repository for the assignment.
- Click on the "Work in Repl.it" button. This will launch an instance of `repl.it` initialized with the code from your repository.
- You'll work with a partner to complete this recitation. To do so, we'll break you into Zoom rooms. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.

## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest main.py` will run all tests
  + `pytest main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Version Control" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**TODO: your answer goes here**

Let's choose $a=2$ and $b=2$, then: 

For $f(n)=1$, it's leaf dominated and $O(n)=n$. We take input(10,20,40,80,160,320,640), we get results(15,31,63,127,255,511,1023), it is linear, so my prediction it correct.

For $f(n)=\log n$, it's leaf dominated and $O(n)=n$.We take input(10,20,40,80,160,320,640), results are (19.9,44.2,93.8,193.9,395.2,798.8,1607.0), it is approximately linear, so it match my derivation.

For $f(n)=n$, it's balanced and $O(n)=n\log n$. We take input(10,20,40,80,160,320,640), results(36,92,224,528,1216,2752,6144), after calcuating, it's similar to $n\log n$.




- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

**TODO: your answer goes here**

When $c > \log_b a$, it's root dominated and the asypmtotic behavior of $W(n)$ would be $O(n^c)$. When $c < \log_b a$, it's leaf dominated and leaves number is $a^{\log_b n}=n^{\log_b a}$ and the asypmtotic behavior of $W(n)$ would be $O(n^{\log_b a})$.

Take $a=4$,$b=2$,$c=1$, as W_1, it's in situation $c < \log_b a$, and take $a=4$,$b=2$,$c=3$, as W_2, it's in situation $c > \log_b a$, we get results as following:
|   n |    W_1 |       W_2 |
|-----|--------|-----------|
|  10 |    126 |      1692 |
|  20 |    524 |     14768 |
|  40 |   2136 |    123072 |
|  80 |   8624 |   1004288 |
| 160 |  34656 |   8113152 |
| 320 | 138944 |  65220608 |
| 640 | 556416 | 523026432 |

For W_1, everytime n times by 2, results approximately times by 4. It meets my prediction of $O(n^{\log_b a})$, which is $O(n^2)$ in the case. For W_2, inputs and results are in a relationship of $n^x$, where x is a number between 3.1 and 3.2, which is also close to my prediction of $O(n^c)$.

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**TODO: your answer goes here**

Based on the condition in problem 4,

For $f(n)=1$, span is $O(n)=\log n$. We take input(10,20,40,80,160,320,640), we get results(4,5,6,7,8,9,10), it is logarithmic, so it matches my derivation.

For $f(n)=\log n$, span is $O(n)=\log^2 n$.We take input(10,20,40,80,160,320,640), results are (7.6,11.9,17.2,23.6,30.9,39.2,48.5), after calcuating, it's similar to $\log^2 n$.

For $f(n)=n$, span is $O(n)=n\log n$. We take input(10,20,40,80,160,320,640), results(18,38,78,158,318,368,1278), after calcuating, it's similar to $n\log n$.
