# Required databases
macro_definition_table = {}  # Storing all macro definitions with their names
macro_name_table = {}  # Storing macro names and their index
arguments_table = {}  # Storing macro arguments for each macro name
intermediate_code = []  # Storing intermediate code for Pass 1

##########################################################################
def process_pass1(source_code):
    mdt_index = 0
    macro_definition = []
    current_macro_name = None
    inside_macro = False
    current_arguments = []

    for line in source_code:
        tokens = line.strip().split()  # store each word of the line of source code

        if not tokens:  # skips blank lines
            continue

        if tokens[0] == 'MACRO':  # beginning of macro definition
            inside_macro = True
            continue

        if inside_macro and tokens[0] == 'MEND':  # if end of macro is reached
            inside_macro = False
            macro_definition_table[current_macro_name] = macro_definition[:]
            macro_name_table[current_macro_name] = mdt_index
            arguments_table[current_macro_name] = current_arguments[:]
            mdt_index += len(macro_definition)
            macro_definition = []
            current_arguments = []
            current_macro_name = None
            continue

        if inside_macro:  # processing contents of macro
            if not current_macro_name:
                current_macro_name = tokens[0]
                current_arguments = tokens[1:]  # Store arguments for the macro
            macro_definition.append(line.strip())
        else:
            intermediate_code.append(line.strip())  # Add non-macro lines to intermediate code

##########################################################################
def process_pass2(source_code):
    output = []
    inside_macro = False

    for line in source_code:
        tokens = line.strip().split()

        if not tokens or tokens[0] == 'MACRO':
            inside_macro = True
            continue
        elif tokens[0] == 'MEND':
            inside_macro = False
            continue

        if inside_macro:
            continue

        macro_name = tokens[0]
        if macro_name in macro_name_table:
            args = tokens[1:]
            macro_def = macro_definition_table[macro_name]
            for expanded_line in macro_def:
                # Replace each argument placeholder with the actual arguments provided in the macro call
                for i, arg in enumerate(args):
                    expanded_line = expanded_line.replace(f"&ARG{i+1}", arg)
                # Avoid printing macro name during expansion
                if not expanded_line.startswith(macro_name):
                    output.append(expanded_line)
        else:
            output.append(line.strip())

    return output

##########################################################################
def display():
    print("Macro Name Table (MNT):")
    for name, index in macro_name_table.items():
        print(f"Macro Name: {name} | Index: {index}")

    print("\nMacro Definition Table (MDT):")
    for name, definition in macro_definition_table.items():
        print(f"Macro: {name}")
        for line in definition:
            print(f"\t{line}")

    print("\nArguments Table:")
    for name, args in arguments_table.items():
        print(f"Macro: {name} | Arguments: {', '.join(args)}")

##########################################################################
def print_intermediate_code():
    print("\nIntermediate Code for Pass 1:")
    for line in intermediate_code:
        print(line)

##########################################################################
source_code = [
    "MACRO",
    "INCR &ARG1, &ARG2",
    "ADD &AREG, &ARG1",
    "MOVER &BREG, &ARG1",
    "MEND",
    "MACRO",
    "DECR &ARG2, &ARG1",
    "SUB &AREG, &ARG2",
    "MOVER &CREG, &ARG1",
    "MEND",
    "START",
    "INCR &A, &B",
    "DECR &C, &D",
    "END"
]
##########################################################################
process_pass1(source_code)
display()
print_intermediate_code()
print("\nPASS 2:")
expanded_code = process_pass2(source_code)
for line in expanded_code:
    print(line)
# END OF CODE
