import streamlit as st
st.markdown("""
### Exercise 5.2
\[Newsvendor Problem\]\n
Consider the following classic problem in decision theory / economics. SUppose you are trying to decide how much 
quantity $Q$ of some product (e.g. newspapers) to buy to maximize your profits. The optimal amount will depend upon how
much demand $D$ you think there is for your product, as well as its cost to you $C$ and its selling price $P$.
Suppose $D$ is unknown but has pdf $f(D)$ and cdf $F(D)$ we can evaluate the expected profit by considering 2 cases:
if $D > Q$, then we sell all $Q$ items and make profit $\pi = (P-C)Q$; but if $D < Q$, we only sell $D$ items, at profit 
$(P-C)D$, but we have wasted $C(Q-D)$ on the unsold items. So the expected profit if we buy quantity $Q$ is:\n
$E_{\pi}(Q) = \int_{Q}^{\infty}(P-C)Q\ f(D)\ dD + \int_{0}^{Q}(P-C)D\ f(D)\ dD - \int_{0}^{Q} C(Q-D)\ f(D)\ dD$\n
Simplify this expression and then take derivatives wrt $Q$ to show that the optimal quantity $Q^*$ (which maximizes
the expected profit) satisfies\n
$$F(Q^*) = \dfrac{P-C}{P}$$
""")

st.markdown("""
### Solution:
lets simplify the integrals\n
$\\Rightarrow \int_{Q}^{\infty} Q(P-C)\ f(D)\ dD + \int_{0}^{Q} PD \ f(D)\ dD - \cancel{\int_{0}^{Q} CD\ f(D)\ dD} - \int_{0}^{Q} CQ\ f(D)\ dD + \cancel{\int_{0}^{Q} CD\ f(D)\ dD}$\n
Since $\int_{Q}^{\infty} f(D)\ dD = [1-\int_{0}^{Q} f(D)\ dD]$\n
And $\int_{0}^{Q} f(D)\ dD] = F(Q)$\n
$\\Rightarrow (P-C)Q[1-F(Q)] + \int_{0}^{Q} PD \ f(D)\ dD - CQ\ F(Q)$\n
$\\Rightarrow (P-C)Q - PQ\ F(Q) + \cancel{CQ\ F(Q)} + \int_{0}^{Q} PD \ f(D)\ dD - \cancel{CQ\ F(Q)}$\n
Differentiate wrt $Q$ and equate it = 0 to find the maximum expected profit\n
$\dfrac{\delta E_{\pi}(Q)}{\delta Q} = P - C - P F(Q) - \cancel{PQ f(Q)} + \cancel{PQf(Q)} = 0$\n
$P-C - PF(Q^*) = 0$\n
$F(Q^*) = \dfrac{P-C}{P}$

The $\dfrac{\delta^2 E_{\pi}(Q)}{\delta Q^2} = - P f(Q)$\n
Since the $f(Q)$ is a probability distribution $f(Q) \gt 0$ making  $\dfrac{\delta^2 E_{\pi}(Q)}{\delta Q^2} \lt 0$


""")
