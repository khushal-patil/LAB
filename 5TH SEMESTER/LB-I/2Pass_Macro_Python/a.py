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
            # Remove commas and process named arguments
            args = [arg.replace(',', '') for arg in args]
            
            # Extract position-based and named arguments
            if macro_name == 'M1':
                arg1, arg2 = args[0], args[1]
                reg_B = args[2].split('=')[1] if '&B=' in args[2] else 'AREG'
                
                # Process and expand macro M1
                for instr in mdt['M1'][:-1]:  # Exclude 'MEND'
                    expanded_instr = (
                        instr.replace("(P,1)", arg1)
                             .replace("(P,2)", arg2)
                             .replace("(P,3)", 'AREG')
                             .replace("(P,4)", reg_B)
                    )
                    print("+" + expanded_instr)
                    
            elif macro_name == 'M2':
                arg1, arg2 = args[0], args[1]
                reg_V = args[2].split('=')[1] if '&V=' in args[2] else 'DREG'
                reg_U = args[3].split('=')[1] if '&U=' in args[3] else 'CREG'
                
                # Process and expand macro M2
                for instr in mdt['M2'][:-1]:  # Exclude 'MEND'
                    expanded_instr = (
                        instr.replace("(P,1)", arg1)
                             .replace("(P,2)", arg2)
                             .replace("(P,3)", reg_U)
                             .replace("(P,4)", reg_V)
                    )
                    print("+" + expanded_instr)

    print("END")

# Run the function to print the output
process_macros()
