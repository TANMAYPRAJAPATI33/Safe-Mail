import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Mail, Lock, Apple, Eye, EyeOff } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { toast } from 'sonner';

const LoginPage = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [activeTab, setActiveTab] = useState('login');

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || !password) {
      toast.error('Please enter both email and password');
      return;
    }
    
    // Simulate login
    setTimeout(() => {
      toast.success('Login successful!');
      navigate('/dashboard');
    }, 1000);
  };

  return (
    <div className="min-h-screen flex flex-col md:flex-row">
      {/* Left side - Hero section with new gradient */}
      <div className="bg-gradient-to-b from-[#6565CF] to-[#F1F1F1] w-full md:w-2/5 p-8 flex flex-col justify-center relative overflow-hidden">
        <div className="z-10 animate-fade-in">
          <h1 className="text-white text-4xl md:text-5xl font-bold mb-4">
            Secure Your Inbox,
            <br />
            <span className="mt-2 inline-block">Detect Spam Instantly</span>
          </h1>
        </div>
        
        {/* Decorative elements */}
        <div className="absolute bottom-10 right-10 w-24 h-24 bg-yellow-400 rounded-full blur-xl opacity-20"></div>
        <div className="absolute top-20 left-20 w-16 h-16 bg-green-400 rounded-full blur-xl opacity-20"></div>
      </div>
      
      {/* Right side - Login form */}
      <div className="w-full md:w-3/5 p-8 flex items-center justify-center">
        <div className="w-full max-w-md space-y-8 animate-fade-in">
          <div className="flex justify-center mb-6">
            <div className="font-bold text-3xl text-[#4361EE]">
              <span>SAFE MAIL</span>
            </div>
          </div>
          
          <div className="text-center">
            <h2 className="text-2xl font-bold mb-1">Welcome Back!</h2>
            <p className="text-safetext-secondary">Get Started with Email Spam Detection</p>
          </div>
          
          <div className="flex bg-safegray-light rounded-lg p-1">
            <button 
              className={`flex-1 py-2 rounded-md transition-all ${activeTab === 'login' ? 'bg-white shadow-sm font-medium' : 'text-safetext-secondary'}`}
              onClick={() => setActiveTab('login')}
            >
              Log in
            </button>
            <button 
              className={`flex-1 py-2 rounded-md transition-all ${activeTab === 'signup' ? 'bg-white shadow-sm font-medium' : 'text-safetext-secondary'}`}
              onClick={() => setActiveTab('signup')}
            >
              Sign Up
            </button>
          </div>
          
          <form onSubmit={handleLogin} className="space-y-4">
            <div className="space-y-2">
              <label htmlFor="email" className="block text-sm font-medium text-safetext-secondary">
                Email
              </label>
              <div className="relative">
                <Input 
                  id="email"
                  type="email" 
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="pl-10 py-6 bg-safegray-light border-0 focus-visible:ring-1 focus-visible:ring-safeblue"
                  placeholder="Enter your email"
                />
                <Mail className="absolute left-3 top-1/2 transform -translate-y-1/2 text-safetext-light w-5 h-5" />
              </div>
            </div>
            
            <div className="space-y-2">
              <div className="flex justify-between">
                <label htmlFor="password" className="block text-sm font-medium text-safetext-secondary">
                  Password
                </label>
                <a href="#" className="text-sm text-safeblue hover:underline">
                  Forgot?
                </a>
              </div>
              <div className="relative">
                <Input 
                  id="password"
                  type={showPassword ? "text" : "password"} 
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="pl-10 py-6 bg-safegray-light border-0 focus-visible:ring-1 focus-visible:ring-safeblue"
                  placeholder="Enter your password"
                />
                <Lock className="absolute left-3 top-1/2 transform -translate-y-1/2 text-safetext-light w-5 h-5" />
                <button 
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3 top-1/2 transform -translate-y-1/2 text-safetext-light hover:text-safetext transition-colors"
                >
                  {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                </button>
              </div>
            </div>
            
            <Button 
              type="submit" 
              className="w-full py-6 bg-safeblue hover:bg-safeblue-dark transition-all"
            >
              Sign In
            </Button>
          </form>
          
          <div className="relative mt-8">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t border-gray-200"></div>
            </div>
            <div className="relative flex justify-center text-sm">
              <span className="px-4 bg-white text-safetext-light">Or Continue With</span>
            </div>
          </div>
          
          <div className="flex gap-4 mt-4">
            <button className="flex-1 flex items-center justify-center gap-2 py-2.5 border rounded-lg hover:bg-safegray-light transition-colors">
              <svg viewBox="0 0 24 24" width="24" height="24" xmlns="http://www.w3.org/2000/svg">
                <g transform="matrix(1, 0, 0, 1, 27.009001, -39.238998)">
                  <path fill="#4285F4" d="M -3.264 51.509 C -3.264 50.719 -3.334 49.969 -3.454 49.239 L -14.754 49.239 L -14.754 53.749 L -8.284 53.749 C -8.574 55.229 -9.424 56.479 -10.684 57.329 L -10.684 60.329 L -6.824 60.329 C -4.564 58.239 -3.264 55.159 -3.264 51.509 Z" />
                  <path fill="#34A853" d="M -14.754 63.239 C -11.514 63.239 -8.804 62.159 -6.824 60.329 L -10.684 57.329 C -11.764 58.049 -13.134 58.489 -14.754 58.489 C -17.884 58.489 -20.534 56.379 -21.484 53.529 L -25.464 53.529 L -25.464 56.619 C -23.494 60.539 -19.444 63.239 -14.754 63.239 Z" />
                  <path fill="#FBBC05" d="M -21.484 53.529 C -21.734 52.809 -21.864 52.039 -21.864 51.239 C -21.864 50.439 -21.724 49.669 -21.484 48.949 L -21.484 45.859 L -25.464 45.859 C -26.284 47.479 -26.754 49.299 -26.754 51.239 C -26.754 53.179 -26.284 54.999 -25.464 56.619 L -21.484 53.529 Z" />
                  <path fill="#EA4335" d="M -14.754 43.989 C -12.984 43.989 -11.404 44.599 -10.154 45.789 L -6.734 42.369 C -8.804 40.429 -11.514 39.239 -14.754 39.239 C -19.444 39.239 -23.494 41.939 -25.464 45.859 L -21.484 48.949 C -20.534 46.099 -17.884 43.989 -14.754 43.989 Z" />
                </g>
              </svg>
            </button>
            <button className="flex-1 flex items-center justify-center gap-2 py-2.5 border rounded-lg hover:bg-safegray-light transition-colors">
              <Apple className="w-6 h-6" />
            </button>
          </div>
          
          <p className="text-center text-sm text-safetext-secondary mt-6">
            Already have an account? <a href="#" className="text-safeblue hover:underline">Log in</a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
