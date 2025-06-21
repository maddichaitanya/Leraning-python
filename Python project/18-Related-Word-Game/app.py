import time
import random

print("=== 🔄 WORD ASSOCIATION GAME 🔄 ===")
print("✨ Respond with a related word quickly! ✨")

word_pairs = {
    "sky": ["blue", "cloud", "bird", "sun", "fly"],
    "water": ["drink", "ocean", "swim", "fish", "boat"],
    "food": ["eat", "cook", "meal", "tasty", "restaurant"],
    "music": ["rock", "love", "pop", "dance", "listen", "band"],
    "book": ["read", "story", "page", "author", "library"],
    "tree": ["leaf", "root", "green", "wood", "forest"],
    "car": ["color", "speed", "race", "travel", "road"],
    "dog": ["pet", "bark", "walk", "puppy", "loyal"]
}

score = 0
rounds = 0

while True:
    prompt = random.choice(list(word_pairs.keys()))
    related_words = word_pairs[prompt]

    print(f"\nPrompt Word: {prompt.upper()}")
    print("Quickly! Type a word related to this prompt!")

    start_time = time.time()
    response = input("> ").lower().strip()
    response_time = time.time() - start_time

    if response in related_words:
        points = max(1, 5 - int(response_time))  # points: 5 if fast, 1 if slow
        score += points
        print(f"👏 Good Association! +{points} points (Answered in {response_time:.1f}s)")
    else:
        print(f"❌ Wrong association. Related words are: {', '.join(related_words)}")

    rounds += 1
    print(f"Current Score: {score} / {rounds * 5} possible points")

    if input("\nPlay again? (y/n): ").lower().startswith('n'):
        print(f"\n🏁 Final Score: {score} out of {rounds * 5} possible points.")
        print("🎉 Thanks for playing this game!")
        break
