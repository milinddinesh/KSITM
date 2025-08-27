-- Insert roles
INSERT INTO app_role (role_name)
VALUES 
  ('Admin'),
  ('Officer'),
  ('Citizen');

-- Insert demo admin user
-- Assumes role_id = 1 corresponds to 'Admin'
-- Replace salt and password_hash with actual values if using hashed passwords
INSERT INTO app_user (
  name, email, mobile, salt, password_hash, role_id, created_at
)
VALUES (
  'Admin',
  'admin@example.com',
  '9999999999',
  'random_salt_123',
  '2e6baef137f63e2e334f74cc3d2fd523eb2448b9393a443ec6e8a80f21d85397',
  1,
  NOW()
);
