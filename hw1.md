---
layout: default
title: Homework 1 | EM
active_tab: syllabus
---

The EM Algorithm <span class="text-muted">Homework 1</span>
=============================================================

The EM algorithm is an approach to unsupervised learning
where the missing labels are considered to be data hidden
from the learner and the EM algorithm assumes a posterior
distribution over the missing labels and learns the 
parameters for the complete data using the posterior.

---
**## Inputs ##**

`output labels` $${\cal Y}$$
: the output label set $${\cal Y} = \{ 1, \ldots, k \}$$. Each label $$y \in {\cal Y}$$.

`training examples`
: $$x^{(i)}$$ for $$i = 1, \ldots, n$$ where each $$x^{(i)} \in {\cal X}$$

`model` $$p(x, y; \theta)$$
: assigns a probability to each $$(x,y)$$ such that $$x \in {\cal X}$$ and $$y \in {\cal Y}$$ using parameters $$\theta$$

`possible parameter values` $$\Omega$$
: the set $$\Omega$$ is the set of possible parameters: $$\theta \in \Omega$$.

---
**## Initialization ##**

* set $$\theta^0$$ to an initial value from $$\Omega$$
{: .list-unstyled}

**## Iterative Re-estimation ##**

* for $$t = 1, \ldots, T$$
    <p>$$ \theta^t = \arg\max_{\theta \in \Omega} Q(\theta, \theta^{t-1})$$ </p>
* where
    <p>$$ Q(\theta, \theta^{t-1}) = \sum_{i=1}^n \sum_{y \in {\cal Y}} \delta(y \mid i) \log p(x^{(i)}, y; \theta) $$ </p>
* and
    <p>$$ \delta(y \mid i) = p(y \mid x^{(i)}; \theta^{t-1}) = \frac{ p(x^{(i)}, y; \theta^{t-1}) }{ \sum_{y \in {\cal Y}} p(x^{(i)}, y; \theta^{t-1}) } $$</p>
{: .list-unstyled}

**## Output ##**

* return $$\theta^T$$
{: .list-unstyled}
---

Taking the $$\arg\max$$ of $$Q(\theta, \theta^{t-1})$$ involves
taking the derivative of $$Q$$ wrt the parameters and setting it
to zero to find the parameters values that would take the gradient
to zero (which gives the local maxima of the $$Q$$ function).  The
difficulty of writing out the derivative depends on the model $$p(x,
y; \theta)$$.

Getting Started
---------------

You must have git installed on your system.
Once you've confirmed this, run this command:

    git clone https://github.com/anoopsarkar/decipherment-class-hw.git

In the repository directory you will see an `em-algo` directory.
This directory contains some data files you will use for this
homework.

The Challenge
-------------

Your task is to use the EM algorithm to solve the following
hidden data problems.

### Three Coins

Implement EM for the three coins problem which is discussed in:

> [The EM algorithm](assets/notes/collns-em-1997.pdf). Michael Collins. 1997.

Write down a Python program (or equivalent) that can be run using the following commands:

    python three_coins.py number-of-EM-iterations init-for-coin0 init-for-coin1 init-for-coin2 observation-list ...

Run your program on the following inputs:

    python three_coins.py 5 0.3 0.3 0.6 HHH TTT HHH TTT HHH
    python three_coins.py 5 0.3 0.3 0.6 HHH TTT HHH TTT
    python three_coins.py 5 0.3 0.7 0.7 HHH TTT HHH TTT 
    python three_coins.py 11 0.3 0.7001 0.7 HHH TTT HHH TTT 
    python three_coins.py 11 0.3 0.6999 0.7 HHH TTT HHH TTT 

### Naive Bayes

Implement EM for Naive Bayes which is discussed in:

> [The Naive Bayes Model, Maximum-Likelihood Estimation, and the EM Algorithm](http://www.cs.columbia.edu/~mcollins/em.pdf). Michael Collins. 2014.

*Warning* do not re-estimate the class prior $$q(y)$$. Keep it fixed to be uniform over the labels $$y$$.

Run your implementation on `example-data.txt` and `voynich.txt` (this is the so-called Currier transcription). Use only two class labels and name them `A` and `B`. After EM training of the parameters, compute the $$\arg\max$$ for each example in training. The output of your program on the `example-data.txt` should look like this:

    0 FINAL 01P Obama/McCain B -0.693147528283
    1 FINAL 02P Obama/McCain B -0.693147528283
    2 FINAL 03P Obama/McCain B -0.693147528283
    3 FINAL 04S Giants/Patriots A -0.778657762454
    4 FINAL 05S Giants/Patriots A -0.778657762454
    5 FINAL 06S Giants/Patriots A -0.778657762454
    corpus likelihood -249.945083149

And the output on the Voynich data should look similar.

### Hidden Markov Models <span class="text-muted">optional</span>

Use a two-state Hidden Markov model to model words in the Voynich data: `voynich.txt`. After EM training compute the $$\arg\max$$ over the data, essentially tagging the data using the two-state HMM. See if you can replicate the famous Currier result about evidence of "two hands" in Voynich.

Ground Rules
------------

* Each person should work on their own. You can share ideas and help each other understand the material but all coding should be your own work.
* You must turn in the following:
  1. The python program `three_coins.py` which implements EM for Three Coins problem and your python program `em-nb.py` which implements EM for Naive Bayes.
  1. The trace of running your implementation of the EM algorithm for Naive Bayes on the following two data sets:
     * `example-data.txt`
     * `voynich.txt` 
  1. Optionally your analysis of using Hidden Markov Models on the Voynich manuscript.
  1. Upload a zip file or tar file with the above files to [Coursys](https://courses.cs.sfu.ca) as the submission for Homework 1. The code should be self-contained, self-documenting, and easy to use.
* You can optionally submit a written description to help me understand your homework solution. You can use plain ASCII but for math equations it is better to use either [latex](http://www.latex-project.org/) or [kramdown](https://github.com/gettalong/kramdown).  Do __not__ use any proprietary or binary file formats such as Microsoft Word.  

If you have any questions or you're confused about anything, just ask.

