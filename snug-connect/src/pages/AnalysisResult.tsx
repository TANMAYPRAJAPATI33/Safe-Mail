import React, { useState, useEffect } from 'react';
import MainLayout from '@/components/layout/MainLayout';
import { Button } from '@/components/ui/button';
import { Check, AlertTriangle, Trash2 } from 'lucide-react';
import { toast } from 'sonner';

const AnalysisResult = () => {
  const [result, setResult] = useState<any | null>(null);

  useEffect(() => {
    const stored = localStorage.getItem('analysis_result');
    if (!stored) {
      toast.error('No analysis result found.');
      return;
    }

    try {
      const storedResult = JSON.parse(stored);

      if (storedResult?.prediction) {
        const spamProb = storedResult.spam_prob ?? storedResult.confidence;
        const spamScore =
          typeof spamProb === 'number' ? (spamProb * 100).toFixed(2) : 'N/A';

        const processedResult = {
          prediction: storedResult.prediction,
          spamScore,
          riskLevel: storedResult.prediction === 'spam' ? 'High' : 'Low',
          formattedResult: storedResult.prediction === 'spam' ? 'Spam' : 'Not Spam',
          spamReason: storedResult.reasons
            ? storedResult.reasons.join(', ')
            : storedResult.prediction === 'spam'
            ? 'This email contains suspicious content'
            : 'No spam indicators detected',
        };

        setResult(processedResult);
      } else {
        toast.error('Invalid analysis result.');
      }
    } catch (err) {
      toast.error('Error parsing analysis result.');
    }
  }, []);

  const handleMarkAsSpam = () => {
    toast.success('Email marked as spam');
  };

  const handleDeleteEmail = () => {
    toast.success('Email deleted successfully');
  };

  if (!result) {
    return (
      <MainLayout>
        <div className="max-w-2xl mx-auto text-center mt-20">
          <h1 className="text-4xl font-bold mb-6">Loading...</h1>
        </div>
      </MainLayout>
    );
  }

  return (
    <MainLayout>
      <div className="max-w-3xl mx-auto animate-fade-in">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold mb-2">Spam Analysis Result</h1>
        </div>

        <div className="bg-white rounded-lg border shadow-sm p-8 space-y-6">
          <div className="space-y-4">
            {/* Spam Score */}
            <div className="flex justify-between items-center py-2">
              <div className="text-safeblue font-medium">Spam Score:</div>
              <div className="flex items-center">
                <div className="font-semibold text-xl">
                  {typeof result.spamScore === 'string'
                    ? `${result.spamScore}/100`
                    : 'N/A'}
                </div>
              </div>
            </div>

            {/* Risk Level */}
            <div className="flex justify-between items-center py-2">
              <div className="text-safeblue font-medium">Risk Level Indicator:</div>
              <div className="flex items-center gap-2">
                <span className="font-semibold">{result.riskLevel}</span>
                <span
                  className={`w-4 h-4 rounded-full ${
                    result.riskLevel === 'High' ? 'bg-red-500' : 'bg-green-500'
                  }`}
                ></span>
              </div>
            </div>

            {/* Display Format */}
            <div className="flex justify-between items-center py-2">
              <div className="text-safeblue font-medium">Display Format:</div>
              <div className="font-semibold">{result.formattedResult}</div>
            </div>
          </div>

          {/* Spam Reasoning */}
          <div className="border-t border-b py-4 my-4">
            <div className="mb-3">
              <div className="text-safeblue font-medium mb-2">Spam Reasoning:</div>
              <div className="flex items-center gap-2 bg-red-50 text-red-700 px-4 py-3 rounded">
                <AlertTriangle className="w-5 h-5" />
                <span>{result.spamReason}</span>
              </div>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex justify-center gap-4">
            <Button
              onClick={handleMarkAsSpam}
              className="flex items-center gap-2 bg-green-600 hover:bg-green-700"
            >
              <Check className="w-4 h-4" />
              <span>Mark as Spam</span>
            </Button>

            <Button
              onClick={handleDeleteEmail}
              variant="outline"
              className="flex items-center gap-2 border-red-300 text-red-600 hover:bg-red-50"
            >
              <Trash2 className="w-4 h-4" />
              <span>Delete Email</span>
            </Button>
          </div>
        </div>
      </div>
    </MainLayout>
  );
};

export default AnalysisResult;
