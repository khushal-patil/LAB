import java.io.*;

class MDT {
    String stmnt;

    public MDT() {
    }

    public MDT(String stmnt) {
        this.stmnt = stmnt;
    }
}

class MNT {
    String name;
    int addr;
    int arg_cnt;

    public MNT(String name, int addr, int arg_cnt) {
        this.name = name;
        this.addr = addr;
        this.arg_cnt = arg_cnt;
    }
}

class Arglist {
    String argname;
    String value;

    public Arglist(String argname) {
        this.argname = argname;
        this.value = "";
    }

    public Arglist(String argname, String value) {
        this.argname = argname;
        this.value = value;
    }
}

public class Pass2MacroProcessor {
    public static void main(String args[]) throws IOException {
        MDT[] MDT = new MDT[20];
        MNT[] MNT = new MNT[4];
        Arglist[] formalParameter = new Arglist[10];
        Arglist[] actualParameter = new Arglist[10];

        int macroAddr = -1;
        boolean macroStart = false, macroEnd = false;
        int macroCall = -1;
        int mdtCnt = 0, mntCnt = 0, formalArglistCnt = 0, actualArglistCnt = 0;

        // Read MNT table
        BufferedReader br1 = new BufferedReader(new FileReader("MNT.txt"));
        String line;
        while ((line = br1.readLine()) != null) {
            String[] parts = line.split("\\s+");
            MNT[mntCnt++] = new MNT(parts[0], Integer.parseInt(parts[1]), Integer.parseInt(parts[2]));
        }
        br1.close();

        // Read ARG table (formal parameters)
        br1 = new BufferedReader(new FileReader("ARG.txt"));
        while ((line = br1.readLine()) != null) {
            String[] parameters = line.split("\\s+");
            formalParameter[formalArglistCnt++] = new Arglist(parameters[0],
                    parameters.length > 1 ? parameters[1] : "");
        }
        br1.close();

        // Read MDT table
        br1 = new BufferedReader(new FileReader("MDT.txt"));
        while ((line = br1.readLine()) != null) {
            MDT[mdtCnt++] = new MDT(line);
        }
        br1.close();

        // Prepare output
        BufferedWriter bw1 = new BufferedWriter(new FileWriter("Output_Pass2.txt"));
        br1 = new BufferedReader(new FileReader("input.txt"));

        while ((line = br1.readLine()) != null) {
            line = line.replaceAll(",", " ");
            String[] tokens = line.split("\\s+");
            boolean isMacroFound = false;
            actualArglistCnt = 0;

            for (String token : tokens) {
                if (token.equalsIgnoreCase("MEND")) {
                    macroEnd = true;
                    macroStart = false;
                    bw1.write("MEND\n");
                } else if (token.equalsIgnoreCase("MACRO")) {
                    macroStart = true;
                    macroEnd = false;
                } else if (macroEnd && !macroStart) {
                    // Check if the token is a macro call
                    for (int i = 0; i < mntCnt; i++) {
                        if (token.equals(MNT[i].name)) {
                            macroCall = i;
                            isMacroFound = true;
                            break;
                        }
                    }
                    // Write non-macro lines directly to output
                    if (!isMacroFound) {
                        bw1.write(token + "\t");
                    }
                }
            }

            // Process macro expansion if a macro call was found
            if (macroCall != -1) {
                macroAddr = MNT[macroCall].addr + 1;
                while (!MDT[macroAddr].stmnt.contains("MEND")) {
                    bw1.write("\n");
                    String[] tempTokens = MDT[macroAddr++].stmnt.split("\\s+");

                    for (String temp : tempTokens) {
                        if (temp.matches("#[0-9]+") || temp.matches(",#[0-9]+")) {
                            int num = Integer.parseInt(temp.replaceAll("[^0-9]+", ""));
                            bw1.write(actualParameter[num - 1].argname + "\t");
                        } else {
                            bw1.write(temp + "\t");
                        }
                    }
                }
                bw1.write("MEND\n"); // Append MEND for each macro
                macroCall = -1;
            }
            bw1.write("\n");
        }
        bw1.close();
    }
}
