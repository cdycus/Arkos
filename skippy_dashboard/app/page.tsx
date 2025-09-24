'use client';
import React, { useState, useEffect } from 'react';
import Head from 'next/head';

export default function Home() {
  const [mode, setMode] = useState('state');
  const [context, setContext] = useState('{}');
  const [response, setResponse] = useState(null);
  const [logs, setLogs] = useState([]);
  const [mood, setMood] = useState(null);
  const [intent, setIntent] = useState(null);
  const [focus, setFocus] = useState(null);
  const [lastExpression, setLastExpression] = useState(null);

  async function submitToSkippy() {
    try {
      const res = await fetch('http://localhost:8088/mind', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode, context: JSON.parse(context) })
      });
      const json = await res.json();
      setResponse(json);
      setLogs(prev => [{ mode, context, response: json }, ...prev]);

      if (json.mood) setMood(json.mood);
      if (json.intent_selected) setIntent(json.intent_selected);
    } catch (err) {
      setResponse({ error: 'Failed to connect to Skippy API' });
    }
  }

  useEffect(() => {
    fetch('/data/mood_log.jsonl').then(res => res.text()).then(text => {
      const entries = text.trim().split('\n');
      if (entries.length > 0) {
        const last = JSON.parse(entries.pop());
        setMood(last.mood);
      }
    });

    fetch('/data/intent_log.jsonl').then(res => res.text()).then(text => {
      const entries = text.trim().split('\n');
      if (entries.length > 0) {
        const last = JSON.parse(entries.pop());
        setIntent(last.intent);
      }
    });

    fetch('/data/attention_snapshot.json').then(res => res.json()).then(setFocus);
    fetch('/data/expression_snapshot_log.jsonl').then(res => res.text()).then(text => {
      const entries = text.trim().split('\n');
      if (entries.length > 0) {
        const last = JSON.parse(entries.pop());
        setLastExpression(last.expression);
      }
    });
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <Head><title>Skippy Dashboard</title></Head>
      <div className="max-w-4xl mx-auto space-y-6">
        <header className="flex justify-between items-center">
          <h1 className="text-3xl font-bold">🧠 Skippy Mind Dashboard</h1>
          <span className="text-xs bg-black text-white px-2 py-1 rounded">v1.0</span>
        </header>

        <section className="bg-white p-4 rounded shadow space-y-4">
          <h2 className="text-xl font-semibold">Interact with Skippy</h2>
          <div>
            <label className="block mb-1">Cognitive Mode:</label>
            <select className="w-full p-2 border rounded" value={mode} onChange={e => setMode(e.target.value)}>
              <option value="reflect">🪞 Reflect</option>
              <option value="state">📊 State</option>
              <option value="expression">🗣️ Expression</option>
              <option value="intent">🎯 Intent</option>
            </select>
          </div>
          <div>
            <label className="block mb-1">Context JSON:</label>
            <textarea className="w-full p-2 border rounded h-24" value={context} onChange={e => setContext(e.target.value)} />
          </div>
          <button onClick={submitToSkippy} className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Submit</button>
        </section>

        <section className="grid grid-cols-2 gap-4">
          <div className="bg-white p-4 rounded shadow space-y-2">
            <h2 className="text-lg font-bold">🧠 Current State</h2>
            <p><strong>Mood:</strong> <span className="capitalize">{mood}</span></p>
            <p><strong>Intent:</strong> {intent}</p>
            <p><strong>Top Focus:</strong> {focus?.[0]?.type}</p>
            <p><strong>Last Expression:</strong> {lastExpression}</p>
          </div>

          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">🧠 Live Response</h2>
            {response && <pre className="bg-gray-100 p-2 rounded text-sm overflow-auto">{JSON.stringify(response, null, 2)}</pre>}
          </div>
        </section>

        <section className="bg-white p-4 rounded shadow">
          <h2 className="text-lg font-bold mb-2">📝 Interaction Log</h2>
          <ul className="space-y-2 max-h-64 overflow-auto text-sm">
            {logs.map((log, i) => (
              <li key={i} className="border-b pb-2">
                <strong>Mode:</strong> {log.mode} | <strong>Context:</strong> {log.context}<br />
                <code className="block bg-gray-50 p-1 rounded mt-1">{JSON.stringify(log.response)}</code>
              </li>
            ))}
          </ul>
        </section>
      </div>
    </div>
  );
}
