---
layout: inmassingle
permalink: /inmas2021/
author_profile: false
---
# INMAS 2021: Modeling and Optimization
This is the webpage for the Modeling and Optimization portion of Inmas 2021. All material for the course will be posted here. 

Instructor: Alex Estes  
email: <este0100@umn.edu>

TAs:  
Nik Wojtalewicz  
email: <npw2@illinois.edu>  

Vaibhav Karve  
email: <vkarve2@illinois.edu>  

## Overview
This workshop introduces optimization models and methods for solving decision-making problems in areas such as engineering, business, economy, manufacturing, finance and healthcare. The ultimate goal is to teach students how to solve large-scale optimization problems from the real world. The course will introduce the following topics: 
- Formulating decision problems into mathematical optimization models.
- Transforming an optimization model into a format that is compatible with optimization solvers (e.g. Gurobi and CPLEX).
- The capability and limitations of a variety of optimization solver software.
- Basic principles of some optimization algorithms.

## Pre-workshop Preparations
Please do the following prior to the workshop:
1. Install Python (see <https://www.python.org>). We will be using the Python interface to Gurobi in order to solve optimization models discussed in class, so you will need a copy. The examples that I give will use Python 3, so I recommend using Python 3. Otherwise, you might have to make some modifications to get the examples to work. A popular distribution is [Anaconda](https://anaconda.com/products/individual). It is easier to configure Gurobi to work with your Python environment when you are using Anaconda, but you do not have to use Anaconda.
2. Install Gurobi on your computer Quickstart reference guides are available on the Gurobi webpage (<https://www.gurobi.com/documentation/quickstart.html>). Follow the quickstart guide for your operating system. The first step of the quickstart guide will direct you to a obtain a Gurobi license; follow the directions for the free academic license. Later in the process, you will have to associate the license with your computer. This will require an active internet connection. In this step, Gurobi checks that your IP address is registered with an academic institution. If you are not on a university network, you may have to connect to a university network via VPN to carry out this step.
3. Configure Gurobi with your python distribution. Gurobi provides guides for this on their website; links: [windows](https://www.gurobi.com/documentation/9.1/quickstart_windows/cs_python_installation_opt.html) [mac](https://www.gurobi.com/documentation/9.1/quickstart_linux/cs_python_installation_opt.html) [linux](https://www.gurobi.com/documentation/9.1/quickstart_linux/index.html)
4. In order to confirm that you have set up Gurobi correctly, run one of the example scripts provided by Gurobi (examples can be found in \<installdir\>/examples/python).
4. (Optional, but recommended) Read the introduction to mathematical programming available on the Gurobi website (<http://www.gurobi.com/resources/getting-started/modeling-basics>).

If you run into any problems in any of these steps, feel free to reach out to Alex Estes.

## Workshop Schedule
Zoom meeting link: [click here](https://umn.zoom.us/j/94999533278?pwd=TGpPTXA0UXlmc21zYlFVLzR1YlZhdz09)

All following times are in Central time.  
Session 1: Friday, April 23rd, 2:00 p.m. to 5:00 p.m.
- Slides: [click here](/files/inmas_2021_mo_day1.pdf).  
- Gurobi examples: [piecontest.py](/files/piecontest.py), [prodplanning_linexpr.py](/files/prodplanning_linexpr.py), [productionplanning.py](productionplanning.py)
- Problems: [click here](/files/inmas_session1_hw.pdf)

Session 2: Saturday, April 24th, 9:00 a.m. to 12:00 p.m.
- Slides: [click here](/files/inmas_2021_mo_day2.pdf).  
- Problems: [click here](/files/inmas_session2_hw.pdf)

Session 3: Saturday, April 24th, 2:00 p.m. to 5:00 p.m.
- Slides: [click here](/files/inmas_2021_mo_day3.pdf).  
- Problems: [click here](/files/inmas_session3_hw.pdf)

Session 4: Sunday, April 25th, 9:00 a.m. to 12:00 p.m.
- Slides: [click here](/files/inmas_2021_mo_day4.pdf). 
- Gurobi examples: [tsp.py](tsp.py)
- Problems: [click here](/files/inmas_session4_hw.pdf)

## Further reading:
Some good resources on optimization:
- Walker, R. (1999). Introduction to Mathematical Programming. New Jersey: Prentice Hall. 
- Bertsimas D. and Tsitsiklis J.N. (1997). Introduction to Linear Optimization. Belmont, MA: Athena Scientific.
- Nemhauser, G.L. and Wolsey L. (1999). Integer and Combinatorial Optimization. John Wiley and Sons.
- Boyd, S. and Vandenberghe, L. (2004). Convex Optimization. Cambridge University Press.
- Nocedal, J. and Wright, S. (2006). Numerical Optimization. Springer Science and Business Media.
- Birge, J. and Louveaux F. (2011). Introduction to Stochastic Programming (2nd edition). Springer Science and Business Media.
- Papadimitriou, C.H. and Seiglitz, K. (1998). Combinatorial Optimization: Algorithms and Complexity. Dover. 