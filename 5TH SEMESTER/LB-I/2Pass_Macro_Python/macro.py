# Read input file
with open("input.txt", "r") as f:
    file = f.readlines()

# Initialize MDT (Macro Definition Table) pointer and empty lists
mdt_pointer = 1
mnt_pointer = 1
ala = []  # Argument List Array

# Create and clear MDT, MNT, and IC files
with open("mdt.txt", "w") as mdt, open("mnt.txt", "w") as mnt, open("ic.txt", "w") as ic:
    pass  # Just clear files

# Open files for writing macro definitions and intermediate code
mdt = open("mdt.txt", "a")
mnt = open("mnt.txt", "a")
ic = open("ic.txt", "a")

is_macro = False  # Flag to indicate macro definition

# Pass 1: Process macros and create MDT, MNT
for line in file:
    line = line.strip()

    if line == "MACRO":
        is_macro = True
    elif line == "MEND":
        mdt.write("MEND\n")
        mdt_pointer += 1
        is_macro = False
    elif is_macro:
        tokens = line.split()
        macro_name = tokens[0]
        parameters = tokens[1:] if len(tokens) > 1 else []
        mnt.write(f"{mnt_pointer} {macro_name} {mdt_pointer}\n")
        mnt_pointer += 1
        ala = parameters  # Store arguments in ALA
        mdt.write(line + "\n")
        mdt_pointer += 1
    else:
        ic.write(line + "\n")  # Write non-macro lines to IC

# Close files after Pass 1
mdt.close()
mnt.close()
ic.close()

# Open files for Pass 2
with open("ic.txt", "r") as ic, open("mnt.txt", "r") as mnt, open("mdt.txt", "r") as mdt:
    ic_lines = ic.readlines()
    mnt_lines = mnt.readlines()
    mdt_lines = mdt.readlines()

# Open output and argument files
output = open("output.txt", "w")
arg_file = open("arg.txt", "w")

# Pass 2: Expand macros
for line in ic_lines:
    line_tokens = line.split()
    if not line_tokens:
        continue
    macro_call = line_tokens[0]
    found_macro = False

    # Check if the line matches any macro in MNT
    for mnt_entry in mnt_lines:
        mnt_tokens = mnt_entry.split()
        if mnt_tokens[1] == macro_call:
            found_macro = True
            mdt_pointer = int(mnt_tokens[2])
            break

    if found_macro:
        # Retrieve actual arguments from macro call
        actual_args = line_tokens[1].split(",") if len(line_tokens) > 1 else []
        
        # Retrieve macro definition from MDT
        expanded_lines = []
        for mdt_line in mdt_lines[mdt_pointer - 1:]:
            mdt_line = mdt_line.strip()
            if mdt_line == "MEND":
                break
            expanded_lines.append(mdt_line)

        formal_args = []
        for idx, exp_line in enumerate(expanded_lines):
            tokens = exp_line.split()
            if idx == 0:
                formal_args = tokens[1:]
                arg_file.write(f"Macro Name: {macro_call}\n")
                arg_file.write("Formal Parameters: " + ", ".join(formal_args) + "\n")
                arg_file.write("Actual Parameters: " + ", ".join(actual_args) + "\n\n")
            else:
                output.write(tokens[0] + " ")

                # Substitute formal parameters with actual arguments
                args = []
                for param in tokens[1].split(","):
                    for j, formal in enumerate(formal_args):
                        if param == formal:
                            args.append(actual_args[j] if j < len(actual_args) else param)
                            break
                    else:
                        args.append(param)
                output.write(",".join(args) + "\n")
    else:
        # Write non-macro lines directly to output
        output.write(line)

# Close output and argument files
output.close()
arg_file.close()
