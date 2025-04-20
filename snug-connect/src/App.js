import React, { useState } from 'react';

function App() {
  const [emailText, setEmailText] = useState('');
  const [prediction, setPrediction] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setPrediction("Loading...");

    try {
      const response = await fetch('http://localhost:5001/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email_text: emailText }),
      });

      const data = await response.json();

      if (response.ok) {
        setPrediction(data.prediction);
      } else {
        setPrediction(`Error: ${data.error}`);
      }
    } catch (error) {
      setPrediction(`Request failed: ${error.message}`);
    }
  };

  return (
    <div style={{ padding: '40px', fontFamily: 'sans-serif' }}>
      <h1>Spam Email Detector</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="8"
          cols="60"
          placeholder="Paste your email text here..."
          value={emailText}
          onChange={(e) => setEmailText(e.target.value)}
          required
        />
        <br /><br />
        <button type="submit">Check for Spam</button>
      </form>

      <div style={{ marginTop: '30px', fontSize: '18px' }}>
        <strong>Prediction:</strong> {prediction}
      </div>
    </div>
  );
}

export default App;
