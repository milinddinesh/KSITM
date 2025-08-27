// src/pages/Home.jsx
import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <header style={{ marginBottom: '2rem' }}>
        <h1>Citizen Service Requests & Fees – GovTech Simulation</h1>
        <p>A secure, scalable platform built with Django + React</p>
      </header>

      <nav style={{ marginBottom: '2rem' }}>
        <p>Please signup if you are a new user.</p>
        <Link to="/login" style={{ marginRight: '1rem' }}>Login</Link>
        <Link to="/signup">Signup</Link>
      </nav>

      <main>
        <p>User Roles : Admin, Officer , Citizen</p>
      </main>
    </div>
  );
};

export default Home;
