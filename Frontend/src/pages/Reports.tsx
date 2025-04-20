
import React, { useState } from 'react';
import MainLayout from '@/components/layout/MainLayout';
import { RefreshCw, Search, Calendar, ChevronDown, Filter } from 'lucide-react';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow
} from '@/components/ui/table';

const Reports = () => {
  const [showDropdown, setShowDropdown] = useState(false);
  
  return (
    <MainLayout>
      <div className="animate-fade-in">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold mb-2">Email Spam Reports & History</h1>
          <p className="text-safetext-secondary">View past email analyses and spam detection logs</p>
        </div>
        
        <div className="max-w-4xl mx-auto bg-white rounded-lg p-6 shadow-sm border">
          <div className="flex flex-col md:flex-row gap-4 mb-6">
            <div className="relative flex-grow">
              <Input
                placeholder="Search by Sender Name, Email, or Subject..."
                className="pl-10 py-6 bg-white border text-safetext"
              />
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-safetext-light w-5 h-5" />
            </div>
            
            <div className="flex gap-3">
              <Button 
                variant="outline"
                className="flex items-center gap-2 min-w-[180px] border-safegray-dark"
              >
                <Filter className="w-4 h-4" />
                <span>Date Range Selector</span>
                <ChevronDown className="w-4 h-4 ml-auto" />
              </Button>
              
              <div className="relative">
                <Button 
                  variant="outline"
                  className="flex items-center gap-2 min-w-[120px] border-safegray-dark"
                  onClick={() => setShowDropdown(!showDropdown)}
                >
                  <span>All Types</span>
                  <ChevronDown className="w-4 h-4 ml-2" />
                </Button>
                
                {showDropdown && (
                  <div className="absolute top-full left-0 right-0 mt-1 bg-white border rounded-md shadow-md z-10 animate-fade-in">
                    <button className="w-full px-4 py-2 text-left hover:bg-safegray-light transition-colors">
                      All Types
                    </button>
                    <button className="w-full px-4 py-2 text-left hover:bg-safegray-light transition-colors">
                      Phishing
                    </button>
                    <button className="w-full px-4 py-2 text-left hover:bg-safegray-light transition-colors">
                      Promotions
                    </button>
                    <button className="w-full px-4 py-2 text-left hover:bg-safegray-light transition-colors">
                      Unknown
                    </button>
                  </div>
                )}
              </div>
            </div>
          </div>
          
          <div className="flex justify-center mt-8 mb-8">
            <Button 
              className="flex items-center gap-2 bg-safeblue hover:bg-safeblue-dark px-8 py-6 rounded-lg"
            >
              <RefreshCw className="w-5 h-5" />
              <span className="text-base">Fetch Data</span>
            </Button>
          </div>
          
          <div className="mt-8 text-center">
            <div className="p-16 border border-dashed rounded-lg bg-safegray-light flex flex-col items-center justify-center">
              <p className="text-safetext-secondary mb-2">No records found</p>
              <p className="text-sm text-safetext-light">Apply filters and fetch data to see results</p>
            </div>
          </div>
        </div>
      </div>
    </MainLayout>
  );
};

export default Reports;
