package searcher;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import static csv_helper.CrunchifyCSVtoArrayList.crunchifyCSVtoArrayList;

/**
 * Created by pligor
 */
public class Searcher {
    private static int indexCol = 0;
    private static int titleCol = 1;

    public static List<Tuple> search(final String filepath, final String[] queries) {
        try {
            BufferedReader crunchifyBuffer = new BufferedReader(new FileReader(filepath));

            String crunchifyLine = null;

            ArrayList<Tuple> tuples = new ArrayList<>();

            while ((crunchifyLine = crunchifyBuffer.readLine()) != null) {
                ArrayList<String> arrayList = crunchifyCSVtoArrayList(crunchifyLine);
                boolean check = doesLineContainsAllQueries(arrayList, queries);
                if(check) {
                    tuples.add(new Tuple(arrayList.get(indexCol), arrayList.get(titleCol)));
                }
            }

            return tuples;
        } catch (FileNotFoundException ee) {
            System.out.println("the filepath " + filepath + " you provided is not there");
        } catch (IOException ee) {
            System.out.println("error while reading the file: " + filepath);
        }

        return null;
    }

    private static boolean doesLineContainsAllQueries(ArrayList<String> arrayList, final String[] queries) {
        int ii = 1; //we do NOT search first column of csv
        while (ii < arrayList.size()) {
            String str = arrayList.get(ii);
            boolean check = doesStrContainsAllQueries(str, queries);
            if(check) {
                return true;
            }
            ii += 1;
        }
        return false;
    }

    private static boolean doesStrContainsAllQueries(final String str, final String[] queries) {
        boolean check = true;
        for (String query : queries) {
            check = check && str.indexOf(query) > -1;
            //indexof is faster than contains: https://stackoverflow.com/questions/18340097/what-is-the-fastest-substring-search-method-in-java
        }
        return check;
    }
}
