sentence = input('enter a sentence : ')

print(sentence.upper())
print(sentence.lower())
print('the length of input : ',len(sentence))
print('number of times \'the\' appears :' , sentence.count('the'))

punct_end= False
punctuation_marks=['.' , ',' , '!' , '?' ]
if (sentence.rstrip().endswith(tuple(punctuation_marks))):
    punct_end=True

print('ur input ends with a punctuation mark : ' , punct_end)

print(sentence.replace(' ','-'))
print('the first word of ur input is : ', sentence.split()[0])
