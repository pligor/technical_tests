package searcher;

/**
 * Created by pligor
 */
public class Tuple {
    private String id;
    private String title;

    Tuple(String id, String title) {
        this.id = id;
        this.title = title;
    }

    @Override
    public String toString() {
        return id + "," + title;
    }
}
