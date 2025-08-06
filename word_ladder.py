 from collections import deque

def word_ladder(start_word, target_word, words):
    word_set = set(words)
    if target_word not in word_set:
        return 0
    queue = deque([(start_word, 1)])
    visited = set([start_word])

    while queue:
        current_word, steps = queue.popleft()
        if current_word == target_word:
            return steps
        for i in range(len(current_word)):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + letter + current_word[i+1:]
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, steps + 1))
    return 0
if __name__ == "__main__":
    start = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(word_ladder(start, target, words))