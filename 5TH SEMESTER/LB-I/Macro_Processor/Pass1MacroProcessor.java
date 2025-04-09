

import java.io.*;

class ArgList {
    String argName, value;

    ArgList(String argument) {
        this.argName = argument;
        this.value = "";
    }
}

class MNT {
    String name;
    int addr;
    int argCount;

    MNT(String name, int addr) {
        this.name = name;
        this.addr = addr;
        this.argCount = 0;
    }
}

class MDT {
    String statement;

    MDT() {
        this.statement = "";
    }
}

public class Pass1MacroProcessor {

    private static MDT[] MDT = new MDT[20];
    private static MNT[] MNT = new MNT[4];
    private static ArgList[] ARG_LIST = new ArgList[10];
    private static int mdtCount = 0, mntCount = 0, argListCount = 0;
    private static boolean macroStart = false, macroEnd = false, fillArgList = false;

    public static void main(String[] args) throws IOException {
        processInputFile("input.txt", "Output_Pass1.txt");
        writeTableToFile(MNT, "MNT.txt", mntCount);
        writeArgListToFile("ARG.txt");
        writeTableToFile(MDT, "MDT.txt", mdtCount);
    }

    private static void processInputFile(String inputFileName, String outputFileName) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(inputFileName));
        BufferedWriter writer = new BufferedWriter(new FileWriter(outputFileName));
        String line;
        boolean start = false;

        while ((line = reader.readLine()) != null) {
            line = line.replaceAll(",", " ");
            String[] words = line.split("\\s+");

            MDT[mdtCount] = new MDT();
            if (line.contains("START"))
                start = true;

            for (int i = 0; i < words.length; i++) {
                if (line.contains("MEND")) {
                    handleMend(words[i]);
                    break;
                }
                if (line.contains("MACRO")) {
                    handleMacro(words[i]);
                } else if (!macroEnd) {
                    if (macroStart) {
                        defineMacroName(words[i]);
                    }
                    if (fillArgList) {
                        i = fillArgumentList(words, i);
                    } else {
                        processStatement(words[i]);
                    }
                } else if (!line.contains("MEND")) {
                    writer.write(words[i] + "\t");
                }
            }
            if (start)
                writer.write("\n");
            if (!macroEnd && !MDT[mdtCount].statement.isEmpty())
                mdtCount++;
        }

        reader.close();
        writer.close();
    }

    private static void handleMend(String word) {
        MDT[mdtCount].statement = "\t" + word;
        mdtCount++; // Increment after the entry is made
        macroEnd = true;
    }

    private static void handleMacro(String word) {
        macroStart = true;
        macroEnd = false;
        fillArgList = false;
    }

    private static void defineMacroName(String word) {
        MNT[mntCount++] = new MNT(word, mdtCount + 1); // Adjusted to mdtCount + 1 for 1-based indexing
        macroStart = false;
        fillArgList = true;
    }

    private static int fillArgumentList(String[] words, int i) {
        boolean first = true;
        while (i < words.length) {
            if (words[i].equals("=")) {
                ARG_LIST[argListCount - 1].value = words[++i];
            } else if (words[i].matches("&[a-zA-Z]+") || words[i].matches("&[a-zA-Z]+[0-9]+")) {
                if (first) {
                    MDT[mdtCount].statement += "\t" + words[i];
                    first = false;
                } else {
                    MDT[mdtCount].statement += "\t," + words[i];
                }
                ARG_LIST[argListCount++] = new ArgList(words[i]);
                MNT[mntCount - 1].argCount++;
            } else {
                MDT[mdtCount].statement += "\t" + words[i];
            }
            i++;
        }
        fillArgList = false;
        return i - 1;
    }

    private static void processStatement(String word) {
        if (word.matches("[a-zA-Z]+") || word.matches("[a-zA-Z]+[0-9]+") || word.matches("[0-9]+")) {
            MDT[mdtCount].statement += "\t" + word;
        } else if (word.matches("&[a-zA-Z]+") || word.matches("&[a-zA-Z]+[0-9]+")) {
            for (int j = 0; j < argListCount; j++) {
                if (word.equals(ARG_LIST[j].argName)) {
                    MDT[mdtCount].statement += "\t" + (j != 0 ? ",#" : "#") + (j + 1);
                }
            }
        }
    }

    private static void writeTableToFile(Object[] table, String fileName, int count) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
        for (int i = 0; i < count; i++) {
            if (table[i] instanceof MNT) {
                MNT entry = (MNT) table[i];
                writer.write(entry.name + "\t" + entry.addr + "\t" + entry.argCount + "\n");
            } else if (table[i] instanceof MDT) {
                MDT entry = (MDT) table[i];
                writer.write(entry.statement + "\n");
            }
        }
        writer.close();
    }

    private static void writeArgListToFile(String fileName) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
        for (int i = 0; i < argListCount; i++) {
            writer.write(ARG_LIST[i].argName + "\t" + ARG_LIST[i].value + "\n");
        }
        writer.close();
    }
}
