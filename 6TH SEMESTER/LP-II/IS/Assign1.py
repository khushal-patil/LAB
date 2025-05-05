def and_xor_string(input_string):
    print("Original String:", input_string)
    print("\nResults:")
    print(f"{'Character':<10} {'ASCII':<10} {'AND 127':<10} {'XOR 127':<10}")
    print("-" * 40)
    for char in input_string:
        ascii_value = ord(char)
        and_result = ascii_value & 127
        xor_result = ascii_value ^ 127
        print(f"{char:<10} {ascii_value:<10} {and_result:<10} {xor_result:<10}")


input_string = input("Enter the String: ")
and_xor_string(input_string)
