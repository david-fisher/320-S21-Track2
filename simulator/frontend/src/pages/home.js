import React, { useState } from 'react';
import '../App.css';
import Dashboard from './sim_dashboard';

export default function Home() {
  
  /** TODO: Set scenarioID picked from dashboard */
  const [scenario, setScenario] = useState(null);

  // let pickedScenario = (scenarioID) => {
  //   setScenario(scenarioID)
  // }

  return (
    <Dashboard
      setScenario={setScenario}
    />
  );
}