import random

def append_random_numbers(number_list, quantity = 1):
    
    for i in range(quantity):
        number_list.append(random.uniform(0,100))
    return number_list
def append_random_words(words_list,quantity = 1):
    wordseed = ['car', 'bus', 'stop','feet','house','castle','plain',
                'orange','mellon', 'beach','boat', 'ship', 'hope']
    for i in range(quantity):
        words_list.append(random.choice(wordseed))
    return words_list

def main():

    numbers = [16.2, 75.1, 52.3]
    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers,3)
    print(numbers)

    word_list = ['join', 'love', 'smile', 'love', 'cloud', 'head']
    words = ['join', 'love', 'smile', 'love', 'cloud', 'head','car', 'bus', 'stop','feet','house', 
             'castle', 'plain', 'orange','mellon', 'beach','boat', 'ship', 'hope']
    
    print(word_list)

    append_random_words(word_list)
    print(word_list)
    
    append_random_words(word_list, 2)
    print(word_list)

    append_random_words(word_list, 3)
    print(word_list)


if __name__ == "__main__":
    main()