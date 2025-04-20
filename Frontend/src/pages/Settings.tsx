
import React, { useState } from 'react';
import MainLayout from '@/components/layout/MainLayout';
import { Switch } from '@/components/ui/switch';
import { Button } from '@/components/ui/button';
import { Slider } from '@/components/ui/slider';
import { toast } from 'sonner';

const Settings = () => {
  const [autoFilter, setAutoFilter] = useState(true);
  const [notifications, setNotifications] = useState(true);
  const [autoLearn, setAutoLearn] = useState(true);
  const [sensitivity, setSensitivity] = useState(70);
  
  const handleSaveSettings = () => {
    toast.success('Settings saved successfully');
  };

  return (
    <MainLayout>
      <div className="max-w-3xl mx-auto animate-fade-in">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">Spam Settings</h1>
          <p className="text-safetext-secondary">Configure your spam detection preferences</p>
        </div>
        
        <div className="bg-white rounded-lg border shadow-sm p-8">
          <div className="space-y-8">
            <div className="flex justify-between items-center">
              <div>
                <h3 className="text-xl font-medium mb-1">Automatically Filter Spam</h3>
                <p className="text-safetext-secondary text-sm">Detected spam will be moved to spam folder</p>
              </div>
              <Switch 
                checked={autoFilter} 
                onCheckedChange={setAutoFilter} 
                className="data-[state=checked]:bg-safeblue"
              />
            </div>
            
            <div className="space-y-4">
              <div>
                <h3 className="text-xl font-medium mb-1">Detection Sensitivity</h3>
                <p className="text-safetext-secondary text-sm">Higher sensitivity may lead to more false positives</p>
              </div>
              <div className="flex items-center gap-8">
                <div className="flex-grow">
                  <Slider
                    value={[sensitivity]}
                    onValueChange={(value) => setSensitivity(value[0])}
                    max={100}
                    step={1}
                    className="data-[state=checked]:bg-safeblue"
                  />
                  <div className="flex justify-between mt-2 text-sm text-safetext-light">
                    <span>Low</span>
                    <span>Medium</span>
                    <span>High</span>
                  </div>
                </div>
                <div className="w-16 text-right font-medium">
                  {sensitivity}%
                </div>
              </div>
            </div>
            
            <div className="flex justify-between items-center">
              <div>
                <h3 className="text-xl font-medium mb-1">Notify on Blocked Emails</h3>
                <p className="text-safetext-secondary text-sm">Get notifications when emails are blocked</p>
              </div>
              <Switch 
                checked={notifications} 
                onCheckedChange={setNotifications}
                className="data-[state=checked]:bg-safeblue"
              />
            </div>
            
            <div className="flex justify-between items-center">
              <div>
                <h3 className="text-xl font-medium mb-1">Auto-learn from Actions</h3>
                <p className="text-safetext-secondary text-sm">Improve detection based on your actions</p>
              </div>
              <Switch 
                checked={autoLearn} 
                onCheckedChange={setAutoLearn}
                className="data-[state=checked]:bg-safeblue"
              />
            </div>
          </div>
          
          <div className="mt-10">
            <Button 
              onClick={handleSaveSettings}
              className="w-full py-6 bg-safeblue hover:bg-safeblue-dark"
            >
              Save Settings
            </Button>
          </div>
        </div>
      </div>
    </MainLayout>
  );
};

export default Settings;
