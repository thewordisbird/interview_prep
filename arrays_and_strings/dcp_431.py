def sentence_check(sentence):
    upper = {chr(i) for i in range(ord("A"), ord("Z") + 1)}
    lower = {chr(i) for i in range(ord("a"), ord("z") + 1)}
    separator = {",", ";", ":"}
    terminator = {".", "?", "!"}

    # Check for constant time rules (first and last character rules)
    if sentence[0] not in upper:
        return False

    if sentence[1] not in lower and sentence[1] != " ":
        return False

    if sentence[-1] not in terminator:
        return False
    
    if sentence[-2] not in lower:
        return False

    # Iterate over rest of sentence to enforce other rules:
    for i in range(2, len(sentence)-3):
        if sentence[i] not in lower and sentence[i] not in separator and sentence[i] != " ":
            return False

        if sentence[i] == " " and (sentence[i-1] == " " or sentence[i+1] == " "):
            return False

    return sentence


if __name__ == "__main__":
    sentence = input("Type Sentence: ")
    while sentence_check(sentence) == False:
        sentence = input("Type Sentence: ")

    print(sentence)
