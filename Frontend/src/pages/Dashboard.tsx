import React from 'react';
import MainLayout from '@/components/layout/MainLayout';
import { Search, Filter, Lock, Shield, MoreHorizontal } from 'lucide-react';
import { Input } from '@/components/ui/input';
import { Progress } from '@/components/ui/progress';

const emailData = [
  { id: 1, date: '9:45 AM', sender: 'intel123@gmail.com', title: "Let's build this awesome product! - Do it! Together, He.", color: 'blue' },
  { id: 2, date: '9:45 AM', sender: 'intel123@gmail.com', title: "Let's build this awesome product! - Do it! Together, He.", color: 'orange' },
  { id: 3, date: '9:45 AM', sender: 'intel123@gmail.com', title: "Let's build this awesome product! - Do it! Together, He.", color: 'pink' },
  { id: 4, date: '9:45 AM', sender: 'intel123@gmail.com', title: "Let's build this awesome product! - Do it! Together, He.", color: 'green' },
  { id: 5, date: '9:45 AM', sender: 'intel123@gmail.com', title: "Let's build this awesome product! - Do it! Together, He.", color: 'red' },
  { id: 6, date: '9:45 AM', sender: 'intel123@gmail.com', title: "Let's build this awesome product! - Do it! Together, He.", color: 'blue' },
  { id: 7, date: '9:45 AM', sender: 'intel123@gmail.com', title: "Let's build this awesome product! - Do it! Together, He.", color: 'purple' },
  { id: 8, date: '9:45 AM', sender: 'intel123@gmail.com', title: "Let's build this awesome product! - Do it! Together, He.", color: 'blue' },
];

const CircularProgress = ({ value, label, color }: { value: number, label: string, color: string }) => {
  // Calculate the stroke-dasharray and stroke-dashoffset for SVG circle
  const radius = 40; // Reduced from 50
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (value / 100) * circumference;
  
  return (
    <div className="flex-1 p-4 bg-white rounded-lg border shadow-sm flex flex-col items-center">
      <div className="relative w-24 h-24 flex items-center justify-center">
        <svg width="100%" height="100%" viewBox="0 0 100 100">
          <circle 
            cx="50" 
            cy="50" 
            r={radius} 
            fill="none" 
            stroke="#E6E8EB" 
            strokeWidth="8"
          />
          <circle 
            cx="50" 
            cy="50" 
            r={radius}
            fill="none" 
            stroke={color} 
            strokeWidth="8" 
            strokeDasharray={circumference} 
            strokeDashoffset={offset}
            transform="rotate(-90 50 50)"
            strokeLinecap="round"
          />
        </svg>
        <div className="absolute text-2xl font-bold">{value}%</div>
      </div>
      <div className="mt-2 text-center text-safetext-secondary font-medium text-sm">{label}</div>
    </div>
  );
};

const Dashboard = () => {
  return (
    <MainLayout>
      <div className="animate-fade-in">
        <div className="mb-6 grid grid-cols-1 md:grid-cols-3 gap-4">
          <CircularProgress value={78} label="Clean Emails" color="#4361EE" />
          <CircularProgress value={22} label="Spam Detected" color="#F87171" />
          <CircularProgress value={56} label="Phishing Blocked" color="#4361EE" />
        </div>
        
        <div className="relative mb-6">
          <Input
            placeholder="Search by name, email or more"
            className="pl-10 py-5 bg-white border rounded-lg"
          />
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-safetext-light w-5 h-5" />
          <div className="absolute right-3 top-1/2 transform -translate-y-1/2">
            <Filter className="text-safetext-light w-5 h-5" />
          </div>
        </div>
        
        <div className="overflow-x-auto rounded-lg border bg-white">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-safegray-light">
              <tr>
                <th scope="col" className="w-10 px-4 py-3">
                  <input type="checkbox" className="rounded text-safeblue focus:ring-safeblue" />
                </th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-medium text-safetext-secondary uppercase tracking-wider">
                  Date
                </th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-medium text-safetext-secondary uppercase tracking-wider">
                  Communication Partner
                </th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-medium text-safetext-secondary uppercase tracking-wider">
                  To
                </th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-medium text-safetext-secondary uppercase tracking-wider">
                  Title
                </th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-medium text-safetext-secondary uppercase tracking-wider">
                  Actions
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-100">
              {emailData.map((email) => (
                <tr 
                  key={email.id} 
                  className="hover:bg-safegray-light transition-colors cursor-pointer"
                >
                  <td className="px-4 py-4 whitespace-nowrap">
                    <input type="checkbox" className="rounded text-safeblue focus:ring-safeblue" />
                  </td>
                  <td className="px-4 py-4 whitespace-nowrap text-sm text-safetext">
                    {email.date}
                  </td>
                  <td className="px-4 py-4 whitespace-nowrap text-sm text-safetext">
                    {email.sender}
                  </td>
                  <td className="px-4 py-4 whitespace-nowrap">
                    <div className="w-8 h-8 rounded-full bg-safegray overflow-hidden">
                      <img 
                        src="/lovable-uploads/04823b2a-a9c1-4700-97aa-0480cb2edecc.png"
                        alt="User avatar" 
                        className="w-full h-full object-cover"
                      />
                    </div>
                  </td>
                  <td className="px-4 py-4 whitespace-nowrap text-sm text-safetext">
                    {email.title}
                  </td>
                  <td className="px-4 py-4 whitespace-nowrap text-sm flex items-center gap-2">
                    <button className="p-1.5 rounded-full text-safetext-light hover:bg-safegray transition-colors">
                      <Lock className="w-4 h-4" />
                    </button>
                    <button className="p-1.5 rounded-full text-safetext-light hover:bg-safegray transition-colors">
                      <Shield className="w-4 h-4" />
                    </button>
                    <button className="p-1.5 rounded-full text-safetext-light hover:bg-safegray transition-colors">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M7 17L17 7M7 7L17 17" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                      </svg>
                    </button>
                    <div className={`w-4 h-4 rounded-full bg-${email.color}-500 ml-1`}></div>
                    <button className="p-1.5 rounded-full text-safetext-light hover:bg-safegray transition-colors ml-1">
                      <MoreHorizontal className="w-4 h-4" />
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </MainLayout>
  );
};

export default Dashboard;
