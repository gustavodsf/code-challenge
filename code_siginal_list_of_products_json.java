import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class ProductFetcher {

    public static void main(String[] args) {
        try {
            String url = "http://127.0.0.1:8081/products";
            HttpURLConnection connection = (HttpURLConnection) new URL(url).openConnection();
            connection.setRequestMethod("GET");

            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder content = new StringBuilder();
            String inputLine;
            while ((inputLine = in.readLine()) != null) {
                content.append(inputLine);
            }
            in.close();
            connection.disconnect();

            String json = content.toString();
            parseAndPrintProducts(json);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void parseAndPrintProducts(String json) {
        json = json.trim();
        if (json.startsWith("[")) {
            json = json.substring(1, json.length() - 1); // Remove the surrounding brackets
        }

        String[] products = json.split("\\},\\{");
        for (String product : products) {
            product = product.replace("{", "").replace("}", "").replace("\"", "");
            String[] fields = product.split(",");
            String name = "";
            double price = 0.0;
            String manufacturer = "no manufacturer";

            for (String field : fields) {
                String[] keyValue = field.split(":");
                String key = keyValue[0].trim();
                String value = keyValue[1].trim();

                switch (key) {
                    case "name":
                        name = value;
                        break;
                    case "price":
                        price = Double.parseDouble(value);
                        break;
                    case "manufacturer":
                        manufacturer = value;
                        break;
                }
            }

            if ("no manufacturer".equals(manufacturer)) {
                System.out.println("Product " + name + " has price " + price + " and no manufacturer");
            } else {
                System.out.println("Product " + name + " has price " + price + " and manufacturer " + manufacturer);
            }
        }
    }
}
