def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    pattern_hash = hash(pattern)

    for i in range(n - m + 1):
        substring_hash = hash(text[i:i + m])
        if substring_hash == pattern_hash and text[i:i + m] == pattern:
            matches.append(i)
    return matches


def main():
    print("🔍 Rabin-Karp String Matching Algorithm\n")

    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search: ")

    matches = rabin_karp(text, pattern)

    if matches:
        print(f"\n✅ Pattern found at positions: {matches}")
    else:
        print("\n❌ Pattern not found in the text.")


if __name__ == "__main__":
    main()
