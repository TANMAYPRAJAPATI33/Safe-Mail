
import React from 'react';
import MainLayout from '@/components/layout/MainLayout';
import { Button } from '@/components/ui/button';
import { Download, Share } from 'lucide-react';

const EmailReport = () => {
  return (
    <MainLayout>
      <div className="max-w-3xl mx-auto animate-fade-in">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold">Email Report Details</h1>
        </div>
        
        <div className="bg-white rounded-lg border shadow-sm p-8">
          <div className="space-y-6">
            <div className="flex flex-col md:flex-row md:items-center justify-between py-4 border-b">
              <div className="text-safeblue text-xl font-medium">Sender Information:</div>
              <div className="font-semibold text-xl">Mr.Rahul Singh</div>
            </div>
            
            <div className="flex flex-col md:flex-row md:items-center justify-between py-4 border-b">
              <div className="text-safeblue text-xl font-medium">Spam Reasoning:</div>
              <div className="font-semibold text-xl">Phishing</div>
            </div>
            
            <div className="flex flex-col md:flex-row md:items-center justify-between py-4 border-b">
              <div className="text-safeblue text-xl font-medium">Spam Score Breakdown:</div>
              <div className="font-semibold text-xl">85/100</div>
            </div>
            
            <div className="flex flex-col md:flex-row md:items-center justify-between py-4">
              <div className="text-safeblue text-xl font-medium">Email Authenticity Check:</div>
              <div className="font-semibold text-xl">DMARC Results</div>
            </div>
          </div>
          
          <div className="flex justify-center gap-4 mt-8">
            <Button 
              variant="outline"
              className="flex items-center gap-2 border-safeblue text-safeblue hover:bg-safeblue/5"
            >
              <Download className="w-4 h-4" />
              <span>Download Report</span>
            </Button>
            
            <Button 
              className="flex items-center gap-2 bg-safeblue hover:bg-safeblue-dark"
            >
              <Share className="w-4 h-4" />
              <span>Export Full Analysis</span>
            </Button>
          </div>
        </div>
      </div>
    </MainLayout>
  );
};

export default EmailReport;
