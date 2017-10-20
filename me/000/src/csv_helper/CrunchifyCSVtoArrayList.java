package csv_helper;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/**
 * Created by pligor
 */
public class CrunchifyCSVtoArrayList {
    // Utility which converts CSV to ArrayList using Split Operation
    public static ArrayList<String> crunchifyCSVtoArrayList(String crunchifyCSV) {
        ArrayList<String> crunchifyResult = new ArrayList<String>();

        if (crunchifyCSV != null) {
            String[] splitData = crunchifyCSV.split("\\s*,\\s*");
            for (int i = 0; i < splitData.length; i++) {
                if (!(splitData[i] == null) || !(splitData[i].length() == 0)) {
                    crunchifyResult.add(splitData[i].trim());
                }
            }
        }

        return crunchifyResult;
    }

}
