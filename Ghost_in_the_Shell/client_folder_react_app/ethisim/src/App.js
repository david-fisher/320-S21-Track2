import React from 'react';
import {
  BrowserRouter as Router,

  Route,
  Redirect,
} from "react-router-dom";
import Signup from './pages/signup';
import Login from './pages/login';
import Homepage from './pages/homepage';

export default function App() {
  return (
    <Router>

        <Route exact path="/">
          <Redirect to="/home" />
        </Route>
        <Route path="/login" component={Login}/>
        <Route path="/signup" component={Signup}/>
        <Route path="/home" component={Homepage}/>

    </Router>
  );
}
