import React, { useState } from 'react';
import MainLayout from '@/components/layout/MainLayout';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';
import { toast } from 'sonner';
import { useNavigate } from 'react-router-dom';

const AnalyzeEmail = () => {
  const [emailText, setEmailText] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const navigate = useNavigate();

  const handleAnalyze = async () => {
    if (!emailText.trim()) {
      toast.error('Please enter email text to analyze');
      return;
    }

    setIsAnalyzing(true);

    try {
      const response = await fetch('http://localhost:5001/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email_text: emailText }),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch prediction');
      }

      const data = await response.json();

      toast.success('Email analysis complete');

      // You can store the result in localStorage, global state, or query param
      localStorage.setItem('analysis_result', JSON.stringify(data));

      navigate('/analysis-result');
    } catch (err) {
      console.error(err);
      toast.error('Something went wrong while analyzing');
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <MainLayout>
      <div className="max-w-3xl mx-auto animate-fade-in">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold mb-2">Email Spam Detector</h1>
          <p className="text-safetext-secondary">Analyze emails for potential spam indicators</p>
        </div>

        <div className="bg-white rounded-lg border p-6 shadow-sm">
          <Textarea
            placeholder="Enter email text here..."
            className="min-h-[240px] resize-none border-dashed text-safetext-secondary focus-visible:ring-safeblue"
            value={emailText}
            onChange={(e) => setEmailText(e.target.value)}
          />

          <div className="mt-4 flex justify-center">
            <Button
              onClick={handleAnalyze}
              disabled={isAnalyzing}
              className="w-40 bg-safeblue hover:bg-safeblue-dark transition-all"
            >
              {isAnalyzing ? 'Analyzing...' : 'Analyze'}
            </Button>
          </div>
        </div>
      </div>
    </MainLayout>
  );
};

export default AnalyzeEmail;
