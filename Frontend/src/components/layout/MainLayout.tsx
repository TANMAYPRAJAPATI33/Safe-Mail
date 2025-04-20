
import React from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { Bell, LayoutDashboard, BarChart2, Settings, Search, LogOut } from 'lucide-react';
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar';
import { toast } from 'sonner';

interface MainLayoutProps {
  children: React.ReactNode;
}

const MainLayout: React.FC<MainLayoutProps> = ({
  children
}) => {
  const location = useLocation();
  const navigate = useNavigate();
  
  const isActive = (path: string) => {
    return location.pathname === path;
  };
  
  const handleLogout = () => {
    toast.success('Logged out successfully');
    navigate('/');
  };
  
  return <div className="min-h-screen flex flex-col">
      {/* Header */}
      <header className="h-16 border-b flex items-center px-4 safe-shadow z-10 bg-white">
        <div className="flex items-center gap-2">
          <div className="font-bold text-3xl text-[#4361EE]">
            <span>SAFE</span>
            <span className="ml-2">MAIL</span>
          </div>
        </div>
        
        <div className="ml-auto flex items-center gap-4">
          <Bell className="w-5 h-5 text-safetext cursor-pointer hover:text-safeblue transition-colors" />
          <Avatar className="h-8 w-8">
            <AvatarImage src="/lovable-uploads/ea767c9a-765c-439f-8e86-3acc890d11cd.png" alt="User avatar" />
            <AvatarFallback>User</AvatarFallback>
          </Avatar>
        </div>
      </header>
      
      <div className="flex flex-1">
        {/* Sidebar */}
        <aside className="w-64 border-r bg-safegray-light p-4 animate-fade-in flex flex-col">
          <nav className="space-y-1 mt-6 flex-1">
            <Link to="/dashboard" className={`sidebar-item ${isActive('/dashboard') ? 'active' : ''}`}>
              <LayoutDashboard className="w-5 h-5" />
              <span>Dashboard</span>
            </Link>
            
            <Link to="/analyze" className={`sidebar-item ${isActive('/analyze') ? 'active' : ''}`}>
              <Search className="w-5 h-5" />
              <span>Analyze Email</span>
            </Link>
            
            <Link to="/reports" className={`sidebar-item ${isActive('/reports') ? 'active' : ''}`}>
              <BarChart2 className="w-5 h-5" />
              <span>Reports & History</span>
            </Link>
            
            <Link to="/settings" className={`sidebar-item ${isActive('/settings') ? 'active' : ''}`}>
              <Settings className="w-5 h-5" />
              <span>Spam Setting</span>
            </Link>
          </nav>
          
          {/* Logout button at the bottom */}
          <button 
            onClick={handleLogout} 
            className="sidebar-item mt-auto mb-4 text-red-500 hover:bg-red-50"
          >
            <LogOut className="w-5 h-5" />
            <span>Log Out</span>
          </button>
        </aside>
        
        {/* Main Content */}
        <main className="flex-1 bg-safegray-light p-6">
          {children}
        </main>
      </div>
    </div>;
};

export default MainLayout;
