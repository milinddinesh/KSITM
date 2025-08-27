import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const navigate = useNavigate();

  const [credentials, setCredentials] = useState({
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    setCredentials(prev => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Placeholder for actual login logic
    console.log("Logging in with:", credentials);
    alert("Login successful!");

    navigate('/'); // Redirect to home after login
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', maxWidth: '400px' }}>
        <label>Email:</label>
        <input type="email" name="email" value={credentials.email} onChange={handleChange} required />

        <label>Password:</label>
        <input type="password" name="password" value={credentials.password} onChange={handleChange} required />

        <button type="submit" style={{ marginTop: '1rem' }}>Login</button>
        <button type="button" onClick={() => navigate('/')} style={{ marginTop: '0.5rem' }}>Back</button>
      </form>
    </div>
  );
};

export default Login;
