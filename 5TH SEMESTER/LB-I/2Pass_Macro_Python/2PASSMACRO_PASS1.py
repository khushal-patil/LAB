
macro_definition_table = {}  
macro_name_table = {}  
arguments_table = {}  
intermediate_code = [] 


def process_pass1(source_code):
    mdt_index = 1
    macro_definition = []
    current_macro_name = None
    inside_macro = False
    current_arguments = []

    for line in source_code:
        tokens = line.strip().split()  

        if not tokens: 
            continue

        if tokens[0] == 'MACRO': 
            inside_macro = True
            
            continue
            
        if inside_macro and tokens[0] == 'MEND':  
            inside_macro = False
            macro_definition_table[current_macro_name] = macro_definition[:]
            macro_name_table[current_macro_name] = mdt_index
            arguments_table[current_macro_name] = current_arguments[:]
            mdt_index += len(macro_definition)
            mdt_index+=1
            macro_definition = []
            current_arguments = []
            current_macro_name = None
            
            continue

        if inside_macro: 
            if not current_macro_name:
                current_macro_name = tokens[0]
                current_arguments = tokens[1:] 
            macro_definition.append(line.strip())
           
        else:
            intermediate_code.append(line.strip())
              
        
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
                
                for i, arg in enumerate(args):
                    expanded_line = expanded_line.replace(arg, args[i] if i < len(args) else '')
               
                if not expanded_line.startswith(macro_name):
                    output.append(expanded_line)
        else:
            output.append(line.strip())

    return output

def display():
    print("Macro Name Table (MNT):")
    for name, index in macro_name_table.items():
        
        print("Macro Name:", name, "| Index:", index)
        

    print("\nMacro Definition Table (MDT):")
    for name, definition in macro_definition_table.items():
        print("Macro:", name)
        for line in definition:
            print("\t", line)

    print("\nArguments Table:")
    for name, args in arguments_table.items():
        print("Macro:", name, "| Arguments:", args)

    print("\nIntermediate Code for Pass 1:")
    for line in intermediate_code:
        print(line)

source_code = [
    "MACRO",
    "INCR &ARG1, &ARG2",
    "ADD &AREG, &ARG1",
    "MOVER &BREG, &ARG1",
    "MEND",
    "MACRO",
    "DECR &ARG2, &ARG1, &ARG3",
    "SUB &AREG, &ARG3",
    "MOVER &CREG, &ARG1",
    "MEND",
    "START",
    "INCR &A, &B",
    "DECR &C, &D, &E",
    "END"
]

process_pass1(source_code)
display()
print("\nPASS 2:")
expanded_code = process_pass2(source_code)
for line in expanded_code:
    print(line)
