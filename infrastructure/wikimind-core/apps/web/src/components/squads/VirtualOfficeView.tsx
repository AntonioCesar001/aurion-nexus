import React, { useState, useEffect } from "react";
import { Activity, Shield, Code, BrainCircuit, RefreshCw, Layers } from "lucide-react";

interface AgentStatus {
  id: string;
  name: string;
  role: string;
  status: "idle" | "working" | "waiting";
  currentTask: string;
  tokenUsage: number;
}

export function VirtualOfficeView() {
  const [agents, setAgents] = useState<AgentStatus[]>([
    { id: "aurion", name: "Aurion", role: "Chief of Staff", status: "idle", currentTask: "Awaiting mission", tokenUsage: 0 },
    { id: "aurora", name: "Aurora", role: "Executor", status: "idle", currentTask: "Standing by", tokenUsage: 0 },
    { id: "investigator", name: "Scanner", role: "Investigator", status: "idle", currentTask: "Standing by", tokenUsage: 0 }
  ]);
  
  const [activeSession, setActiveSession] = useState<string | null>(null);

  // Mock real-time updates for demonstration
  useEffect(() => {
    const interval = setInterval(() => {
      setAgents(prev => 
        prev.map(agent => {
          if (agent.id === "aurion" && activeSession) {
             return { ...agent, status: "working", currentTask: "Orchestrating sub-agents & reviewing output", tokenUsage: agent.tokenUsage + Math.floor(Math.random() * 50) };
          }
          if (agent.id === "aurora" && activeSession) {
             return { ...agent, status: "working", currentTask: "Executing file modifications...", tokenUsage: agent.tokenUsage + Math.floor(Math.random() * 80) };
          }
          return agent;
        })
      );
    }, 3000);
    return () => clearInterval(interval);
  }, [activeSession]);

  const toggleMockSession = () => {
    if (activeSession) {
      setActiveSession(null);
      setAgents(agents.map(a => ({ ...a, status: "idle", currentTask: "Awaiting mission" })));
    } else {
      setActiveSession("session-" + Date.now());
    }
  };

  return (
    <div className="flex flex-col h-full bg-slate-950 text-slate-200">
      <header className="px-6 py-4 border-b border-slate-800 flex justify-between items-center text-white bg-slate-900/50">
        <div className="flex items-center gap-3">
          <Layers className="w-6 h-6 text-indigo-400" />
          <h1 className="text-xl font-semibold tracking-tight text-white">Nexus Virtual Office</h1>
        </div>
        <div className="flex gap-4 items-center">
          <div className="flex items-center gap-2 text-sm text-slate-400">
            <Shield className="w-4 h-4 text-emerald-400" />
            <span>AgentShield Active</span>
          </div>
          <button 
            onClick={toggleMockSession}
            className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
              activeSession 
                ? "bg-red-500/10 text-red-400 hover:bg-red-500/20" 
                : "bg-indigo-500 hover:bg-indigo-600 text-white"
            }`}
          >
            {activeSession ? "Halt Mission" : "Mock Dispatch Mission"}
          </button>
        </div>
      </header>

      <main className="p-6 flex-1 overflow-auto">
        <div className="mb-6">
          <h2 className="text-lg font-medium text-slate-300 mb-2">Active Squad Overview</h2>
          <p className="text-sm text-slate-500">Monitor agent pipelines, real-time status, and system resources.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {agents.map((agent) => (
            <div key={agent.id} className="bg-slate-900 rounded-xl border border-slate-800 p-5 shadow-sm relative overflow-hidden">
              {agent.status === "working" && (
                <div className="absolute top-0 left-0 w-full h-1 bg-indigo-500 animate-pulse"></div>
              )}
              
              <div className="flex justify-between items-start mb-4">
                <div className="flex items-center gap-3">
                  <div className={`p-2 rounded-lg ${
                    agent.id === "aurion" ? "bg-amber-500/10 text-amber-500" :
                    agent.id === "aurora" ? "bg-indigo-500/10 text-indigo-500" :
                    "bg-emerald-500/10 text-emerald-500"
                  }`}>
                    {agent.id === "aurion" ? <BrainCircuit className="w-5 h-5" /> : 
                     agent.id === "aurora" ? <Code className="w-5 h-5" /> : 
                     <Activity className="w-5 h-5" />}
                  </div>
                  <div>
                    <h3 className="font-medium text-slate-200">{agent.name}</h3>
                    <p className="text-xs text-slate-500">{agent.role}</p>
                  </div>
                </div>
                <div className={`text-xs px-2 py-1 rounded-full border ${
                  agent.status === "working" ? "bg-indigo-500/10 border-indigo-500/30 text-indigo-400" :
                  agent.status === "idle" ? "bg-slate-800/50 border-slate-700 text-slate-400" :
                  "bg-amber-500/10 border-amber-500/30 text-amber-400"
                }`}>
                  {agent.status.toUpperCase()}
                  {agent.status === "working" && <RefreshCw className="inline-block w-3 h-3 ml-1 animate-spin" />}
                </div>
              </div>
              
              <div className="bg-slate-950 rounded-lg p-3 border border-slate-800/50 min-h-[80px]">
                <p className="text-sm font-mono text-slate-400">
                  <span className="text-emerald-500 font-bold">&gt; </span>
                  {agent.currentTask}
                </p>
              </div>
              
              <div className="mt-4 flex justify-between items-center text-xs text-slate-500">
                <span>Tokens Consumed</span>
                <span className="font-mono bg-slate-800 px-2 py-1 rounded">{agent.tokenUsage.toLocaleString()} TK</span>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}
