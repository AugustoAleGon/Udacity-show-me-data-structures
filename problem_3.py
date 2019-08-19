import sys

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

def char_frequence(sentence):
    #Create a dictionary that contains frequence of a word
    count_words = {}
    for char in sentence:
        if char in count_words:
            count_words[char] += 1
        else:
            count_words[char] = 1
    return count_words

def sort_char(dict):
    frequence_char_tuple = list(dict.items())
    frequence_char_tuple.sort(key=lambda x: x[1])
    return frequence_char_tuple

def huffman_encoding(data):
    if not data:
        return data, None
    else:
        map_sort_frequence = list(map(lambda x: Node(x[0], x[1]), sort_char(char_frequence(data))))
        tree = None

        while(len(map_sort_frequence) > 1):
            first_leaf = map_sort_frequence.pop(0)
            second_leaf = map_sort_frequence.pop(0)
            root_node = Node(first_leaf.value + second_leaf.value, first_leaf.value + second_leaf.value)
            root_node.left = first_leaf
            root_node.right = second_leaf
            insert_element(root_node, map_sort_frequence)
            if(len(map_sort_frequence) == 0):
                tree = Tree(root_node)
        
        if tree is None and len(map_sort_frequence) == 1:
            first_leaf = map_sort_frequence.pop(0)
            tree = Tree(Node(first_leaf.value, first_leaf.value))
            tree.root.left = Node(first_leaf.key, first_leaf.value)

        encoded_char = {}
        encode_tree(tree.root, "", encoded_char)
        encode_string = ""
        for char in data:
            encode_string += encoded_char[char]
        return encode_string, tree

def insert_element(node, sort_frecuence):
    for index, element in enumerate(sort_frecuence):
        if node.value < element.value:
            sort_frecuence.insert(index, node)
            break
        elif index == len(sort_frecuence) -1:
            sort_frecuence.append(node)
            break

def encode_tree(root, string, huffman_encodes):
    if root.right is None and root.left is None:
        huffman_encodes[root.key] = string
    else:
        if root.left != None:
            encode_tree(root.left, string + "0", huffman_encodes)
        if root.right != None:
            encode_tree(root.right, string + "1", huffman_encodes)
            

def huffman_decoding(data,root):
    if root is None:
        return data
    def decode(data, root, index, decode_string):
        if (root.left is None and root.right is None):
            decode_string += root.key
            return index, decode_string
        elif (data[index] == "0"):
            return decode(data, root.left, index + 1, decode_string)
        else:
            return decode(data, root.right, index + 1, decode_string)
    index = 0
    decode_string = ""
    while (index <= len(data) -1):
        index, decode_string = decode(data, root, index, decode_string)
    return decode_string

def test_one_word_sentence():
    one_word_sentence = "Udacity"

    print("The size of the data is: {}\n".format(sys.getsizeof(one_word_sentence)))
    print("The content of the data is: {}\n".format(one_word_sentence))

    encoded_data, tree = huffman_encoding(one_word_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree.root)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))


def test_great_sentence():
    value_great_sentence = "The bird is a word"

    print("The size of the data is: {}\n".format(sys.getsizeof(value_great_sentence)))
    print("The content of the data is: {}\n".format(value_great_sentence))

    encoded_data, tree = huffman_encoding(value_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree.root)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))


def test_empty_sentence():
    empty_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(empty_sentence)))
    print("The content of the data is: {}\n".format(empty_sentence))

    encoded_data, tree = huffman_encoding(empty_sentence)

    # data not encoded
    if not encoded_data and not tree:
        print("success", "data not encoded")


test_one_word_sentence()
test_great_sentence()
test_empty_sentence()