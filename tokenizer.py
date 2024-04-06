def tokenize_and_pad(sentences, vocab, n):
    #Special tokens
    pad_token = '<PAD>'
    unk_token = '<UNK>'
    
    #Special tokens in the vocabulary if they are not already present
    if pad_token not in vocab:
        vocab[pad_token] = len(vocab)
    if unk_token not in vocab:
        vocab[unk_token] = len(vocab)
    
    #Empty list to store tokenized and padded sequences
    tokenized_sequences = []
    
    #When desired length is zero
    if n == 0:
        return [[] for _ in range(len(sentences))]
    
    for sentence in sentences:
        #Considering punctuation as separate tokens
        words = [word.strip(".,!?;:") for word in sentence.split()]
        
        #Using the provided vocab for tokenization
        tokens = [vocab.get(word, vocab[unk_token]) for word in words]
        
        #Truncation if the sequence exceeds the desired length n
        if len(tokens) > n:
            tokens = tokens[:n]
        
        #Padding the sequence to length n
        if len(tokens) < n:
            tokens.extend([vocab[pad_token]] * (n - len(tokens)))
        
        #Getting the tokenized and padded sequence list
        tokenized_sequences.append(tokens)
    
    return tokenized_sequences