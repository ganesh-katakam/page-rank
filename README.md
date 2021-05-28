# Page Rank Algorith Implmentation using Matrix Multiplication in Python

---

#### Page Rank :
	Page Rank (PR) is an algorithm used by Google Search to rank websites in their search results. It is a way of measuring the importance of web pages. It is named after Larry Page, one of the co-founder of Google. In short, Page Rank is a “vote”, by all the other pages in the web, about how important a page is.

	A link to a Page counts as a support. Page Rank Algorithm outputs a probability distribution used to represent the likelihood that a person randomly clicking on links will arrive at any particular page. It can be calculated for documents of any size.

	There are many ways to find the Rank of a Page. One of them is by using the Matrix Multiplication.

#### Algorithm :
Step 1 : Find the adjacency matrix of the web graph.
Step 2 : Now deduce the adjacency to a probability matrix(The row sum of the matrix should be 1).
Step 3 : Now we use the transpose of the probability matrix.
Step 4 : Now we multiply the transpose of the probability matrix with the column vector. Step 5 : For each iteration the column vector is updated with the result of the previous iteration operation and then multiplied with the transpose matrix.
Step 6 : We will stop the iterations when two consecutive iterations get the same result. Step 7 : The resulting column vector is the final page rank value of each page and the node with highest rank value is considered the best.

#### Calculations :
Let G (V,E) be a graph with web pages as Vertices and the links between them as Edges.
Let A be the adjacency matrix derived from graph G.
We find the probability matrix M from A with the sum of values in a row equal to 1. Now we find the transpose of the matrix M i.e., MT.
Let d be the damping factor.
The column vector is P with each value as d.
For each iteration, we will multiply MT with P i.e., MT X P and update the value of P. We will stop the process after k iterations when Pk = Pk-1 .