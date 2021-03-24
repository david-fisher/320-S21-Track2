import React from 'react';
import { Route } from "react-router-dom";
import Summary from "./pages/summary";
import Dashboard from "./pages/sim_dashboard";
import SimulationWindow from "./pages/simulationWindow";
import RadarTest from "./pages/chartTest";
import CssBaseline from "@material-ui/core/CssBaseline";
import './App.css';
import Dashboard from '../../../Ghost_in_the_Shell/client_folder_react_app/ethisim/src/pages/dashboard';

function App() {
  return (
    <>
      <CssBaseline />
      <Route exact path="/home" component={Dashboard} />
      <Route exact path="/summary" component={Summary}/>
      <Route exact path="/simulation" component={SimulationWindow}/>
      <Route exact path="/chartTest" component={RadarTest}/>
    </>
  );
}

export default App;


