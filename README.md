# Text Processor

Inês is new to programming. She is writing a simple application to handle text. So far, the app only supports adding text to a blank document. Rita, her restless little sister, is fascinated with all the different symbols on Inês’ screen and wants to play with it, not letting Inês work any longer. In order to be able to continue working, Inês decides to turn it into a game for Rita.

Inês will let Rita write whatever she likes in the app. Then, Inês will select portions of the document with width W and challenge Rita to guess how many distinct sequences of symbols there are in that portion of text. Rita is excited to play, but there is a problem: Inês doesn’t know yet how to write a program to find the right answer for her own questions. Can you help her out?

# Task

Given the description of the game being played by the two sisters: the text written in the document, and Inês’ questions, find the number of distinct (non-empty) substrings for each of the questions. A substring is a sequence of contiguous letters in the document.

# Input

The first line of the input contains the text written by Rita. The text is composed only by letters [a−z]
. The second line has two space separated integers: Q and W. Q is the number of questions and W the fixed width of Inês’ questions. Each of the following Q lines contains a single integer i, describing a question to know the number of distinct substrings in the range [i,i+W−1].

# Constraints

1≤|D|≤100000 Number of letters in a document.

1≤Q≤100000 Number of questions.

1≤W≤|D| Width of Inês’ questions.

1≤i≤|D|−W+1 The question range is one-indexed and inside the document bounds.

# Output

The output contains the answer to each question in the same order as in the input, one per line.

# Sample Output Explanation

In the first sample, the first question concerns the range [1,3]→aca, which has 5 distinct substrings {a,c,ac,ca,aca}.
The second question corresponds to cat, which has 6 distinct substrings: {a,c,t,ca,at,cat}.

![](sample_IO.png)

Details : [Southwestern Europe Regional Contest (SWERC) 2015](https://open.kattis.com/problems/textprocessor)
