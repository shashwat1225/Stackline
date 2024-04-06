from tokenizer import tokenize_and_pad

def additional_test():
    vocab = {'<PAD>': 0, '<UNK>': 1, 'I': 2, 'love': 3, 'coding': 4}
    sentences = ['I love coding', 'coding is fun']
    n = 5

    result = tokenize_and_pad(sentences, vocab, n)
    text_case = """
vocab = {'<PAD>': 0, '<UNK>': 1, 'I': 2, 'love': 3, 'coding': 4}
    sentences = ['I love coding', 'coding is fun']
    n = 5

    result = tokenize_and_pad(sentences, vocab, n)
"""
    print("Question's Test case:", text_case)
    print("Tokenizer's output:", result)
    

def test_tokenize_and_pad():
    vocab = {'<PAD>': 0, '<UNK>': 1, 'I': 2, 'love': 3, 'coding': 4, 'is': 5, 'fun': 6}

    #Test case 1: Empty sentences list
    sentences1 = []
    n1 = 5
    expected_output1 = []
    assert tokenize_and_pad(sentences1, vocab, n1) == expected_output1

    #Test case 2: Single sentence with all known words
    sentences2 = ['I love coding']
    n2 = 5
    expected_output2 = [[2, 3, 4, 0, 0]]
    assert tokenize_and_pad(sentences2, vocab, n2) == expected_output2

    #Test case 3: Single sentence with unknown words
    sentences3 = ['I love programming']
    n3 = 5
    expected_output3 = [[2, 3, 1, 0, 0]]
    assert tokenize_and_pad(sentences3, vocab, n3) == expected_output3

    #Test case 4: Multiple sentences with known and unknown words
    sentences4 = ['I love coding', 'coding is fun', 'I enjoy programming']
    n4 = 5
    expected_output4 = [[2, 3, 4, 0, 0], [4, 5, 6, 0, 0], [2, 1, 1, 0, 0]]
    assert tokenize_and_pad(sentences4, vocab, n4) == expected_output4

    #Test case 5: Sentence longer than the desired length
    sentences5 = ['I love coding and it is fun']
    n5 = 4
    expected_output5 = [[2, 3, 4, 1]]
    assert tokenize_and_pad(sentences5, vocab, n5) == expected_output5

    #Test case 6: Sentence shorter than the desired length
    sentences6 = ['coding is fun']
    n6 = 6
    expected_output6 = [[4, 5, 6, 0, 0, 0]]
    assert tokenize_and_pad(sentences6, vocab, n6) == expected_output6

    #Test case 7: Sentence with exactly the desired length
    sentences7 = ['I love coding is fun']
    n7 = 5
    expected_output7 = [[2, 3, 4, 5, 6]]
    assert tokenize_and_pad(sentences7, vocab, n7) == expected_output7

    #Test case 8: Empty vocab
    sentences8 = ['I love coding']
    vocab8 = {}
    n8 = 5
    expected_output8 = [[1, 1, 1, 0, 0]]
    assert tokenize_and_pad(sentences8, vocab8, n8) == expected_output8

    #Test case 9: Vocab with only special tokens
    sentences9 = ['I love coding']
    vocab9 = {'<PAD>': 0, '<UNK>': 1}
    n9 = 5
    expected_output9 = [[1, 1, 1, 0, 0]]
    assert tokenize_and_pad(sentences9, vocab9, n9) == expected_output9

    #Test case 10: Sentence with only unknown words
    sentences10 = ['John enjoys playing guitar']
    n10 = 5
    expected_output10 = [[1, 1, 1, 1, 0]]
    assert tokenize_and_pad(sentences10, vocab, n10) == expected_output10

    #Test case 11: Sentence with repeated words
    sentences11 = ['I love coding and I love coding']
    n11 = 7
    expected_output11 = [[2, 3, 4, 1, 2, 3, 4]]
    assert tokenize_and_pad(sentences11, vocab, n11) == expected_output11

    #Test case 12: Multiple sentences with varying lengths
    sentences12 = ['I love coding', 'coding', 'coding is fun and exciting']
    n12 = 6
    expected_output12 = [[2, 3, 4, 0, 0, 0], [4, 0, 0, 0, 0, 0], [4, 5, 6, 1, 1, 0]]
    assert tokenize_and_pad(sentences12, vocab, n12) == expected_output12

    #Test case 13: Desired length is zero
    sentences13 = ['I love coding']
    n13 = 0
    expected_output13 = [[]]
    assert tokenize_and_pad(sentences13, vocab, n13) == expected_output13

    #Test case 14: Desired length is negative
    sentences14 = ['I love coding']
    n14 = -5
    expected_output14 = [[]]
    assert tokenize_and_pad(sentences14, vocab, n14) == expected_output14

    #Test case 15: Sentence with leading and trailing whitespace
    sentences15 = ['  I love coding  ']
    n15 = 5
    expected_output15 = [[2, 3, 4, 0, 0]]
    assert tokenize_and_pad(sentences15, vocab, n15) == expected_output15

    #Test case 16: Sentence with multiple whitespace between words
    sentences16 = ['I   love    coding']
    n16 = 5
    expected_output16 = [[2, 3, 4, 0, 0]]
    assert tokenize_and_pad(sentences16, vocab, n16) == expected_output16

    #Test case 17: Sentence with punctuation
    sentences17 = ['I love coding, it is fun!']
    n17 = 5
    expected_output17 = [[2, 3, 4, 1, 5]]
    assert tokenize_and_pad(sentences17, vocab, n17) == expected_output17

    #Test case 18: Sentence with numbers
    sentences18 = ['I love coding since 2010']
    n18 = 5
    expected_output18 = [[2, 3, 4, 1, 1]]
    assert tokenize_and_pad(sentences18, vocab, n18) == expected_output18

    #Test case 19: Sentence with mixed case words
    sentences19 = ['I LoVe CoDiNg']
    n19 = 5
    expected_output19 = [[2, 1, 1, 0, 0]]
    assert tokenize_and_pad(sentences19, vocab, n19) == expected_output19

    # Test case 20: Sentence with non-alphanumeric characters
    sentences20 = ['I love @coding!']
    n20 = 5
    expected_output20 = [[2, 3, 1, 0, 0]]
    assert tokenize_and_pad(sentences20, vocab, n20) == expected_output20

    print("All test cases designed by the candidate passed!")


if __name__ == "__main__":
    test_tokenize_and_pad()
    additional_test()