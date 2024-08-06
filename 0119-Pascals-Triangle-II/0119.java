import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<Integer> getRow(int rowIndex) {

        List<Integer> result = Arrays.asList(1);

        for (int i = 0; i < rowIndex; i++) {
            List<Integer> next_row = new ArrayList<>(Collections.nCopies(result.size() + 1, 0));

            for (int j = 0; j < result.size(); j++) {
                next_row.set(j, next_row.get(j) + result.get(j));
                next_row.set(j + 1, next_row.get(j + 1) + result.get(j));
            }

            result = next_row;

        }

        return result;
    }

    public List<Integer> getRow1(int rowIndex) {
        var prevRow = Arrays.asList(1);

        for (int i = 1; i <= rowIndex; i++) {
            var currentRow = new ArrayList<Integer>(i + 1);
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    currentRow.add(1);
                    continue;
                }
                currentRow.add(prevRow.get(j) + prevRow.get(j - 1));
            }
            prevRow = currentRow;
        }
        return prevRow;
    }
}