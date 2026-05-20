import "./styles.css";
import { useState, useEffect } from "react";

function useFetch(url) {
  const [status, setStatus] = useState("idle");
  const [data, setData] = useState([]);

  useEffect(() => {
    if (!url) return;
    const fetchData = async () => {
      setStatus("fetching");
      const response = await fetch(url);
      const data = await response.json();
      setData(data);
      setStatus("fetched");
    };
    fetchData();
  }, [url]);

  return {
    status,
    data,
  };
}

function Products({ products }) {
  return (
    <table>
      <thead>
        <tr>
          <td> Id </td>
          <td> Name </td>
          <td> Price </td>
        </tr>
      </thead>
      <tbody>
        {products.map(({ id, title, price }, i) => (
          <tr>
            <td>{id}</td>
            <td>{title}</td>
            <td>{price}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default function App() {
  const url = "https://dummyjson.com/products";
  const { status, data } = useFetch(url);
  const { products } = data;
  return (
    <div className="App">
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
      {status === "fetching" && <> Lets go get some data!! </>}
      {status === "fetched" && <Products products={products} />}
    </div>
  );
}
