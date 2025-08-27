import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Signup = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: '',
    email: '',
    mobile: '',
    password: '',
    confirmPassword: '',
  });

  const handleChange = (e) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

const handleSubmit = async (e) => {
  e.preventDefault();

  const { name, email, mobile, password, confirmPassword } = formData;

  // Frontend validations
  if (password !== confirmPassword) {
    alert("Passwords do not match");
    return;
  }

const passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_[\]{}:;<>,.?~\\/-]).{6,}$/;

  if (!passwordRegex.test(password)) {
    alert("Password must contain at least one uppercase letter, one number, and one special character.");
    return;
  }

  const emailRegex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
  if (!emailRegex.test(email)) {
    alert("Please enter a valid email address.");
    return;
  }

  const mobileRegex = /^\d{12}$/;
  if (!mobileRegex.test(mobile)) {
    alert("Mobile number must be 12 digits (country code + 10-digit number).");
    return;
  }

  // POST to backend
  try {
    const response = await fetch("http://localhost:8000/api/signup/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, email, mobile, password }),
    });

    const result = await response.json();

    if (!response.ok) {
      // Backend returned an error
      alert(result.error || "Signup failed. Please try again.");
      return;
    }

    // Success
    alert("Signup successful!");
    navigate('/');
  } catch (error) {
    console.error("Error during signup:", error);
    alert("Something went wrong. Please check your connection and try again.");
  }
};

//sign up form 
  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', maxWidth: '400px' }}>
        <label>Name:</label>
        <input type="text" name="name" value={formData.name} onChange={handleChange} required />

        <label>Email:</label>
        <input type="email" name="email" value={formData.email} onChange={handleChange} required />

        <label>Mobile:</label>
        <input type="tel" name="mobile" value={formData.mobile} onChange={handleChange} required />

        <label>Password:</label>
        <input type="password" name="password" value={formData.password} onChange={handleChange} required />

        <label>Re-type Password:</label>
        <input type="password" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} required />

        <button type="submit" style={{ marginTop: '1rem' }}>Sign Up</button>
        <button type="button" onClick={() => navigate('/')} style={{ marginTop: '0.5rem' }}>Back</button>
      </form>
    </div>
  );
};

export default Signup;
