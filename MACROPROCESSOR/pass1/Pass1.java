import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;

public class Pass1 {

	public static void main(String[] args) throws IOException {
		// Buffered reader for input file
		BufferedReader b1 = new BufferedReader(new FileReader("input.txt"));
		// File writers for the output files
		FileWriter f1 = new FileWriter("intermediate.txt");
		FileWriter f2 = new FileWriter("mnt.txt");
		FileWriter f3 = new FileWriter("mdt.txt");
		FileWriter f4 = new FileWriter("kpdt.txt");

		// Parameter Name Table
		HashMap<String, Integer> pntab = new HashMap<>();
		String s; // To store each line from input file
		int paramNo = 1, mdtp = 1, flag = 0, pp = 0, kp = 0, kpdtp = 0;

		while ((s = b1.readLine()) != null) {
			String word[] = s.split("\\s+"); // Split line by space or tab

			// Start of MACRO definition
			if (word[0].equalsIgnoreCase("MACRO")) {
				flag = 1;
				pp = kp = 0;
				paramNo = 1;

				// Handle the macro definition name and parameters
				if (word.length >= 2) {
					String macroName = word[1]; // Macro name
					String paramString = (word.length > 2) ? word[2] : "";

					// Split the parameter string by commas
					if (!paramString.isEmpty()) {
						String[] params = paramString.split(",");
						for (String param : params) {
							if (param.contains("=")) {
								// Keyword parameter
								kp++;
								String[] keywordParam = param.split("=");
								String paramName = keywordParam[0].substring(1); // Remove '&'
								pntab.put(paramName, paramNo++);

								if (keywordParam.length == 2) {
									// Write to kpdt.txt
									f4.write(paramName + "\t" + keywordParam[1] + "\n");
								} else {
									f4.write(paramName + "\t-\n"); // No default value
								}

							} else {
								// Positional parameter
								pp++;
								String paramName = param.substring(1); // Remove '&'
								pntab.put(paramName, paramNo++);
							}
						}
					}

					// Write to mnt.txt
					f2.write(macroName + "\t" + pp + "\t" + kp + "\t" + mdtp + "\t" + (kp == 0 ? kpdtp : (kpdtp + 1))
							+ "\n");

					kpdtp += kp; // Update kpdtp for future macros
				}

			} else if (word[0].equalsIgnoreCase("MEND")) {
				// End of MACRO definition
				f3.write(s + '\n'); // Write "MEND" to MDT
				flag = 0; // Reset flag as macro definition ends
				pntab.clear(); // Clear the parameter table for the next macro
				mdtp++; // Move MDT pointer to next position

			} else if (flag == 1) {
				// Inside macro definition
				// Convert parameters into placeholders in MDT (#1, #2, etc.)
				for (int i = 0; i < s.length(); i++) {
					if (s.charAt(i) == '&') {
						i++; // Skip '&'
						StringBuilder paramName = new StringBuilder();
						while (i < s.length() && (s.charAt(i) != ' ' && s.charAt(i) != ',')) {
							paramName.append(s.charAt(i));
							i++;
						}
						f3.write("#" + pntab.get(paramName.toString())); // Write parameter placeholder
					} else {
						f3.write(s.charAt(i)); // Write normal text
					}
				}
				f3.write("\n"); // New line after each statement in MDT
				mdtp++; // Move MDT pointer

			} else {
				// Non-macro instructions, write to intermediate file
				f1.write(s + '\n');
			}
		}

		// Close all file readers and writers
		b1.close();
		f1.close();
		f2.close();
		f3.close();
		f4.close();
	}
}
