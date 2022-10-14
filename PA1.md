Measuring the similarity between different sequences of DNA may tell us how related the owners of those sequences are. 

A molecule of DNA consists of two chains made up of repeating sub-units called nucleotides. There are four different types of nucleotides in DNA: adenine (A), thymine (T), guanine (G), and cytosine (C)[1]. Programmatically, DNA we can have represent it as a string, where each character must be one of A, G, C, or T.

Let's **pretend** that o measure similarity, there are two simple measures:

**NUMBER OF MATCHES:** for the first one, we will compare the alignment between two sequences of DNA checking each position. Most probably there are better ways of assessing DNA similarity, but we will use this as a case for our programming assignment. By aligning the sequences pairwise, we can count the number of matches

MAXIMUM CONTIGUOUS CHAIN: In this case, we will analyze the sequences following the same pairwise comparison. However, we will try to search the highest number of contiguous matches. In the example above, one solution could be to shift the sequence 1 by 3, which results in a contiguous chain with 2 matching nucleotides.





Short description of approach to solve the problem
```
To begin with, I have gone through the question carefully and then I have opted for an approach to divide the problem into functions so that my work becomes easy. I have categorized the code into different functions for each operation. For example, I have used def match_number()  to calculate the number of matching elements from the two files. Then I used def contiguous_chain(seq1, seq2)  which calculates the matching pairs adjacent and continuous. To shift the elements I have used def shift_sequence1() and def shift_sequence2() functions. Another important function to focus on which I have used is def file_to_seq() where the file operations take place like opening the text file, reading the file, and closing the file. Then I used the main function for taking inputs and printing outputs. The input files are taken as text files with the “.txt” extension only. Mostly, I have used “try and except” which helps in handling the errors. In this approach, since python interprets the code line-by-line, the flow goes to the try statement and checks if it is true. If the goal is accomplished by the code then the except block is ignored and processed. In case, any exception in the try block exists then the except block is approached and starts to execute the except block.
This approach of using a try-except block to handle exceptions in python is called  “catching an exception”.
I have opted for this approach because if I can figure out the error, I can make the required changes, and even if a particular block of code is wrong then I can remove it without affecting the whole code.
```

CODE
```
def match_number(seq1, seq2):
    match = 0
    for a, b in zip(seq1, seq2):
        if a == b and a != '-' and b != '-':
            match += 1
    # print(match)
    return match


def contiguous_chain(seq1, seq2):
    temp = 0
    chain = 0
    for a, b in zip(seq1, seq2):
        if a == b and a != '-' and b != '-':
            temp += 1
            # print(a,b,chain)
            if temp > chain:
                chain = temp
                # print(a,b,chain,temp)
        else:
            temp = 0
    # print(chain)
    return chain


def shift_sequence1(seq1, seq2, shifts):
    ss1 = []
    ss2 = []
    for i in range(shifts):
        seq1 = (''.join(['-', seq1]))
        ss1.append(seq1)
        seq2 = (''.join([seq2, '-']))
        ss2.append(seq2)
    # print(ss1,ss2)
    return ss1, ss2


def shift_sequence2(seq1, seq2, shifts):
    ss1 = []
    ss2 = []
    for i in range(shifts):
        seq1 = ''.join([seq1, '-'])
        ss1.append(seq1)
        seq2 = ''.join(['-', seq2])
        ss2.append(seq2)
    # print(ss1,ss2)
    return ss1, ss2


def shifted_sequences(seq1, seq2, shifts):
    ss1 = []
    ss2 = []

    a, b = shift_sequence1(seq1, seq2, shifts)
    # print('ss1: ', a,b)
    aa, bb = shift_sequence2(seq1, seq2, shifts)
    # print('ss2: ', aa,bb)
    ss1 = a + aa
    ss2 = b + bb
    # print(ss1, ss2)
    return ss1, ss2


# this function takes in file names that contains sequences and return both sequences
def file_to_seq(fname1, fname2):
    try:
        with open(fname1) as fobj1:
            seq1 = fobj1.read()
        with open(fname2) as fobj2:
            seq2 = fobj2.read()
        # print(seq1,seq2)
        fobj1.close()
        fobj2.close()
    except FileNotFoundError:
        print('entered file is not there. check again')
    except UnboundLocalError:
        print('Local variable referenced before assignment')

    return seq1, seq2


def main():
    matches = []
    chains = []

    try:
        f_seq1 = input('enter sequence 1 file : ')
        f_seq2 = input('enter sequence 2 file : ')
        max_shifts = int(input('enter maximum number of shifts needed : '))
        approach_used = int(input('enter approach: enter \'0\' - number of matches & \'1\' - maximum chain : '))

        seq1, seq2 = file_to_seq(f_seq1, f_seq2)
        if len(seq1) == len(seq2):
            shifted_sequence1, shifted_sequence2 = shifted_sequences(seq1, seq2, max_shifts)
            # print(shifted_sequence1, shifted_sequence2)

            for i in range(len(shifted_sequence1)):
                matches.append(match_number(shifted_sequence1[i], shifted_sequence2[i]))
                chains.append(contiguous_chain(shifted_sequence1[i], shifted_sequence2[i]))
            # print(matches,chains)

            if approach_used:
                print('the maximum contiguous chain that matches the sequences : ', max(chains),
                      '\nshifted sequence-1 for which max contiguous chain resulted : ',
                      shifted_sequence1[chains.index(max(chains))],
                      '\nshifted sequence-2 for which max contiguous chain resulted : ',
                      shifted_sequence2[chains.index(max(chains))])
            else:
                print('maximum number of matches (score) : ', max(matches),
                      '\nshifted sequence-1 for which max score resulted : ',
                      shifted_sequence1[matches.index(max(matches))],
                      '\nshifted sequence-2 for which max score resulted : ',
                      shifted_sequence2[matches.index(max(matches))])

        else:
            print('Sequence 1 length is ', len(seq1), '\nSequence 2 length is ', len(seq2),
                  '\nSequence lengths are not same')
    except TypeError:
        print('Sequences are empty or null')
    except ValueError:
        print('Check data type of variables in code')
    except AttributeError:
        print('Attribute reference or Assignment failed')
    except UnboundLocalError:
        print('Local variable referenced before assignment')

main()
```
The text files used as seq1.txt and seq2.txt contains the following sequences 
seq1 - ACTGATCAC--
seq2 - --TTAGCTCGA
Links to seq1 and seq2 are 

OUTPUT
```
OUTPUT 1 - Shifting the sequences by 1 position and finding maximum matches 

C:\Users\hi\PycharmProjects\PA1\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/PA1/DNAmatch.py
enter sequence 1 file : seq1.txt
enter sequence 2 file : seq2.txt
enter maximum number of shifts needed : 1
enter approach: enter '0' - number of matches & '1' - maximum chain : 0
maximum number of matches (score) :  1 
shifted sequence-1 for which max score resulted :  -ACTGATCAC-- 
shifted sequence-2 for which max score resulted :  --TTAGCTCGA-

Process finished with exit code 0


OUTPUT 2 - Shifting by the sequences 2 positions and finding maximum contiguous chain that matches the sequence

C:\Users\hi\PycharmProjects\PA1\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/PA1/DNAmatch.py
enter sequence 1 file : seq1.txt
enter sequence 2 file : seq2.txt
enter maximum number of shifts needed : 2
enter approach: enter '0' - number of matches & '1' - maximum chain : 1
the maximum contiguous chain that matches the sequences :  2 
shifted sequence-1 for which max contiguous chain resulted :  --ACTGATCAC-- 
shifted sequence-2 for which max contiguous chain resulted :  --TTAGCTCGA–

Process finished with exit code 0


OUTPUT 3 - Shifting by the sequences 4 positions and finding the maximum score

C:\Users\hi\PycharmProjects\PA1\venv\Scripts\python.exe C:/Users/hi/PycharmProjects/PA1/DNAmatch.py
enter sequence 1 file : seq1.txt
enter sequence 2 file : seq2.txt
enter maximum number of shifts needed : 4
enter approach: enter '0' - number of matches & '1' - maximum chain : 0
maximum number of matches (score) :  3 
shifted sequence-1 for which max score resulted :  --ACTGATCAC-- 
shifted sequence-2 for which max score resulted :  --TTAGCTCGA--

Process finished with exit code 0

```

Hurdles faced and benifits from the approach implemented in this
```
It was difficult to keep track of the different functions used and organize them to get the exact flow of operation and execution. Using try-except helped in this case to overcome the hurdles. In this process, I have become familiar with using functions and try-except blocks. I have become familiar with exception handling and handling errors.

```
