# Define the Macro Definition Table (MDT)
mdt = {
    'M1': [
        'MOVER (P,3) (P,1)',
        'ADD (P,3) =\'1\'',
        'MOVER (P,4) (P,2)',
        'ADD (P,4) =\'5\'',
        'MEND'
    ],
    'M2': [
        'MOVER (P,3) (P,1)',
        'MOVER (P,4) (P,2)',
        'ADD (P,3) =\'15\'',
        'ADD (P,4) =\'10\'',
        'MEND'
    ]
}

# Define the Macro Name Table (MNT)
mnt = {
    'M1': [2, 2, 1, 1],
    'M2': [2, 2, 6, 3]
}

# Define the Intermediate Code (macro calls and arguments)
intermediate_code = [
    'START 100',
    'M1 10, 20, &B=CREG',
    'M2 100, 200, &V=AREG, &U=BREG',
    'END'
]

# Output generation
def process_macros():
    
    print("START 100")
    
    # Process each line in the intermediate code
    for line in intermediate_code:
        if line.startswith('M1') or line.startswith('M2'):
            macro_name, *args = line.split()
            if macro_name in mdt:
                # Get the macro definition (MDT entries)
                mdt_instructions = mdt[macro_name]
                
                # Map the arguments from the intermediate code to the macro definition
                if macro_name == 'M1':
                    # Example for M1: M1 10, 20, &B=CREG
                    arg1, arg2, arg3 = args[0], args[1], args[2]
                    # Replace placeholders (P, 1), (P, 2), etc. in the macro definition with the arguments
                    mdt_instructions[0] = mdt_instructions[0].replace("(P,3)", arg1)
                    mdt_instructions[1] = mdt_instructions[1].replace("(P,3)", arg1)
                    mdt_instructions[2] = mdt_instructions[2].replace("(P,4)", arg2)
                    mdt_instructions[3] = mdt_instructions[3].replace("(P,4)", arg2)
                    
                    # Replace the register names (CREG, etc.)
                    mdt_instructions[0] = mdt_instructions[0].replace("CREG", "&B")
                    mdt_instructions[1] = mdt_instructions[1].replace("CREG", "&B")
                    
                    # Print each instruction from the expanded macro
                    for instr in mdt_instructions[:-1]:  # Exclude 'MEND'
                        print("+" + instr.replace("(P,1)", arg1).replace("(P,2)", arg2))
                
                elif macro_name == 'M2':
                    # Example for M2: M2 100, 200, &V=AREG, &U=BREG
                    arg1, arg2, arg3, arg4 = args[0], args[1], args[2], args[3]
                    # Replace placeholders (P, 1), (P, 2), etc. in the macro definition with the arguments
                    mdt_instructions[0] = mdt_instructions[0].replace("(P,3)", arg1)
                    mdt_instructions[1] = mdt_instructions[1].replace("(P,4)", arg2)
                    mdt_instructions[2] = mdt_instructions[2].replace("(P,3)", arg1)
                    mdt_instructions[3] = mdt_instructions[3].replace("(P,4)", arg2)
                    
                    # Replace the register names (AREG, BREG)
                    mdt_instructions[0] = mdt_instructions[0].replace("AREG", "&V")
                    mdt_instructions[1] = mdt_instructions[1].replace("AREG", "&V")
                    mdt_instructions[2] = mdt_instructions[2].replace("BREG", "&U")
                    mdt_instructions[3] = mdt_instructions[3].replace("BREG", "&U")
                    
                    # Print each instruction from the expanded macro
                    for instr in mdt_instructions[:-1]:  # Exclude 'MEND'
                        print("+" + instr.replace("(P,1)", arg1).replace("(P,2)", arg2))

    print("END")

# Run the function to print the output
process_macros()
