import streamlit as st

st.markdown("""
## Exercise 5.1
In many classification problems one has the option either of assigning $x$ to class $j$ or, if you are too uncertain, 
of choosing the **reject option.** If the cost of rejects is less than the cost of falsely classifying the object, 
it may be the optimal action. Let $\\alpha_i$ mean you choose action $i$ for $i = 1:C+1$, where $C$ is the number of 
classes and $C+1$ is the reject action. Let $Y=j$ be the true (but unknown) **state of nature**. Define the loss function 
as follows \n
""")
st.latex(r"""
\lambda(\alpha_{i}|Y = j) =
\left\{ \begin{array}{cc}
0 & if\ \ i=j\ and\ \ i,j \in \{1, ..., C\} 
\\
\lambda_{r} & if\ \ i = C+1
\\
\lambda_{s} & otherwise
\end{array}
\right.
""")
st.markdown("""
In other words, you incur $0$ loss if you correctly classify. You incur $\lambda_{r}$ loss (cost) if you choose the reject
option, and you incur $\lambda_{s}$ loss (cost) if you make a substitution error (misclassification).\n
1. Show that the minimum risk is obtained if we decide $Y=j$ if $p(Y=j|x) \ge p(Y=k|x)$ for all $k$ (i.e., $j$ is the
most probable class) and if $p(Y=j|x) \ge 1- \dfrac{\lambda_{r}}{\lambda_{s}}$; otherwise we decide to reject.
2. Describe qualitatively what happens as $\dfrac{\lambda_r}{\lambda_{s}}$ is increased from 0 to 1 (i.e. the relative
cost of rejection increases)
""")

st.markdown(""""
## Solution
We have information/observation $x$. using this information and prior distribution of $p(Y=j)$ we can compute 
posterior distribution $p(Y=j|x)$ 

Now using the cost/risk function we can compute the risk of taking an action $\\alpha_{i}$.
\n
$R(\\alpha_{i}|x)_{i \\ne C+1} = \displaystyle\sum_{j}^C p(Y=j|x) * \lambda(\\alpha_{i}|Y=j)$\n
since $\lambda(\\alpha_{i}|Y=j) = 0\ \ for\ \ i = j$\n
$R(\\alpha_{i}|x)_{i \\ne C+1} = \displaystyle\sum_{j \\ne i}^C p(Y=j|x) * \lambda(\\alpha_{i}|Y=j)$\n
$\Rightarrow \displaystyle\sum_{j \\ne i}^C p(Y=j|x) * \lambda_{s} $\n
$\Rightarrow \lambda_{s}\displaystyle\sum_{j \\ne i}^C p(Y=j|x) $\n
$
R(\\alpha_{i}|x)_{i \\ne C+1} =  \lambda_{s}(1- p(Y=i|x)) \   \    \dots (1)
$ \n
The have the lowest risk we need to minimize the risk. to minimize the above we need to choose $\\alpha_{i}$ for which
$p(Y=i|x)$ is the highest. aka action corresponding to maximum posterior probability.\n
if the action is to select a class then we decide $Y = j$ if $p(Y=j|x) \ge p(Y=k|x)$ for all  $k$


If there is a reject option then we need to consider the cost of reject option $\\alpha_{i=C+1}$ as well\n.
$R(\\alpha_{i=C+1}|x) = \lambda_{r} \   \dots (2)$

To select an action corresponding to maximum posterior probability, the cost of rejection($R(\\alpha_{i=C+1}|x)$) has to be less than cost of 
selecting $\\alpha_{i \\ne C+1}$ which is ($R(\\alpha_{i}|x)_{i \\ne C+1}$)
\n 

$R(\\alpha_{i}|x)_{i \\ne C+1} < R(\\alpha_{i=C+1}|x)$\n
$\lambda_{s}(1- p(Y=i|x)) < \lambda_{r}$\n
$p(Y=i|x) > 1 - \dfrac{\\lambda_r}{\\lambda_s}$\n

2.

If $\dfrac{\\lambda_r}{\\lambda_s}$ increases from 0 to 1 then the quatity $1 - \dfrac{\\lambda_r}{\\lambda_s}$ will approach
to zero and we would more likely to take an action rather than choose the reject option. 

""")

