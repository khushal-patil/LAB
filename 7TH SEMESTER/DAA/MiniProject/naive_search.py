def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i)

    return matches


def main():
    print("🔍 Naive String Matching Algorithm\n")

    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search: ")

    matches = naive_string_matching(text, pattern)

    if matches:
        print(f"\n✅ Pattern found at positions: {matches}")
    else:
        print("\n❌ Pattern not found in the text.")


if __name__ == "__main__":
    main()
