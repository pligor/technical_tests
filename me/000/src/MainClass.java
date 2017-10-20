/**
 * Created by pligor
 */
import java.util.Arrays;
import java.util.List;

import searcher.Searcher;
import searcher.Tuple;

public class MainClass {
    public static void main(String[] args) {
        if (args.length > 1) {
            final String filepath = args[0];
            final String[] queries = Arrays.copyOfRange(args, 1, args.length);

            List<Tuple> tuples = Searcher.search(filepath, queries);

            if (tuples == null) {
                //noop
            } else {
                for (Tuple tuple : tuples) {
                    System.out.println(tuple);
                }
            }

            /*BufferedReader crunchifyBuffer = null;

            try {
                String crunchifyLine;
                crunchifyBuffer = new BufferedReader(new FileReader(filepath));

                // How to read file in java line by line?
                while ((crunchifyLine = crunchifyBuffer.readLine()) != null) {
                    System.out.println("Raw CSV data: " + crunchifyLine);
                    System.out.println("Converted ArrayList data: " + crunchifyCSVtoArrayList(crunchifyLine) + "\n");
                }

            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                try {
                    if (crunchifyBuffer != null) crunchifyBuffer.close();
                } catch (IOException crunchifyException) {
                    crunchifyException.printStackTrace();
                }
            }*/

            //Tree structure:
            //https://stackoverflow.com/a/2815269/720484
            //https://stackoverflow.com/a/2816004/720484
        } else {
            System.out.println("You should run your application at the command line as follows:\n" +
                    "java -jar Test.jar <input file CSV> [search term(s) ...]\n");
        }
    }
}


