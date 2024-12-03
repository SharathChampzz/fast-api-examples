import React, { useEffect, useState, useRef } from "react";
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

// Register Chart.js components
ChartJS.register(LineElement, PointElement, LinearScale, CategoryScale, Title, Tooltip, Legend);

function App() {
  const [prices, setPrices] = useState([]);
  const [timestamps, setTimestamps] = useState([]);
  const [news, setNews] = useState([]);

  const chartRef = useRef(null); // To hold the chart instance

  useEffect(() => {
    // Connect to the prices stream
    const priceEventSource = new EventSource("http://127.0.0.1:8000/prices");
    priceEventSource.onmessage = (event) => {
      const { price } = JSON.parse(event.data);
      setPrices((prevPrices) => [...prevPrices.slice(-99), price]);
      setTimestamps((prevTimestamps) => [
        ...prevTimestamps.slice(-99),
        new Date().toLocaleTimeString(),
      ]);
    };

    // Connect to the news stream
    const newsEventSource = new EventSource("http://127.0.0.1:8000/news");
    newsEventSource.onmessage = (event) => {
      const { news } = JSON.parse(event.data);
      setNews((prevNews) => [...prevNews, news]);
      toast(news, { autoClose: 5000 });
    };

    return () => {
      // Close the EventSource connections
      priceEventSource.close();
      newsEventSource.close();
    };
  }, []);

  const chartData = {
    labels: timestamps,
    datasets: [
      {
        label: "CHAMPZZ Stock Price",
        data: prices,
        fill: false,
        borderColor: prices.length > 1 && prices[prices.length - 1] < prices[prices.length - 2] ? "red" : "green",
        tension: 0.1,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: { display: false },
    },
    scales: {
      x: { title: { display: true, text: "Time" } },
      y: { title: { display: true, text: "Price (USD)" } },
    },
  };

  return (
    <div style={{ margin: "20px" }}>
      <h1>CHAMPZZ Real-Time Stock Tracker</h1>
      <div style={{ height: "70vh", marginBottom: "20px" }}>
        <Line ref={chartRef} data={chartData} options={chartOptions} />
      </div>
      <ToastContainer />
    </div>
  );
}

export default App;
