import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loggedIn, setLoggedIn] = useState(false);
  const [report, setReport] = useState(null);
  const [userId, setUserId] = useState("");

  const handleLogin = async () => {
    if (!username || !password) return setError("Enter username & password");

    try {
      const res = await fetch("http://localhost:5001/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password, role: "patient" }),
      });
      const data = await res.json();
      if (data.success) {
        setUserId(data.user_id);
        setLoggedIn(true);
        setError("");
      } else {
        setError(data.message);
      }
    } catch (err) {
      setError("Login failed");
      console.error(err);
    }
  };

  useEffect(() => {
    if (loggedIn && userId) {
      fetch(`http://localhost:5001/heatmap/${userId}`)
        .then((res) => res.json())
        .then((data) => setReport(data))
        .catch((err) => console.error(err));
    }
  }, [loggedIn, userId]);

  if (!loggedIn)
    return (
      <div className="container">
        <h1>HealthCore Patient Login</h1>
        <input
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button onClick={handleLogin}>Login</button>
        {error && <p style={{ color: "red" }}>{error}</p>}
      </div>
    );

  return (
    <div className="container">
      <h1>My AI Report</h1>
      {report ? (
        <ul>
          <li>Top Left: {report[0][0]}</li>
          <li>Top Right: {report[0][1]}</li>
          <li>Bottom Left: {report[1][0]}</li>
          <li>Bottom Right: {report[1][1]}</li>
        </ul>
      ) : (
        <p>Loading report...</p>
      )}
    </div>
  );
}

export default App;