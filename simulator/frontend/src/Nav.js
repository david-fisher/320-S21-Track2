import React from "react";

import Summary from "./pages/summary";
import RadarTest from "./pages/chartTest";
import Dashboard from "./pages/sim_dashboard";

import {
  ThemeProvider,
  createMuiTheme,
  makeStyles,
  AppBar,
  Toolbar,
  Typography,
  Button,
  IconButton,
} from "@material-ui/core";
import MenuIcon from "@material-ui/icons/Menu";

import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";
import SimulationWindow from './pages/simulator_window';
import { ConvLimitProvider } from './pages/context/ConvContext';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
    backgroundColor: "#ced4da",
  },
  title: {
    flexGrow: 1,
    color: "#FFF",
  },
  link: {
    "&:hover": {
      color: "#000000",
      textDecoration: "none",
    },
  },
}));

const theme = createMuiTheme({
  palette: {
    primary: {
      main: "#881c1c",
    },
  },
  background: {
    color: '#444e58'
  }
});

export const ScenariosContext = React.createContext();

function Nav() {
  const classes = useStyles();
  const scenariosState = React.useState({});

  return (
    <div className={classes.root}>
      <Router basename="/simulator">
        <div>
          <ThemeProvider theme={theme}>
            <AppBar position="static" color="primary">
              <Toolbar>
                <IconButton
                  edge="start"
                  className={classes.menuButton}
                  color="inherit"
                  aria-label="menu"
                >
                <MenuIcon />
                </IconButton>
                <Typography variant="h6" className={classes.title}>
                  <Link className={classes.link} to="/">
                    <Button className={classes.title} color="inherit">
                      Home
                    </Button>
                  </Link>
                </Typography>
                <Button color="inherit">LogOut</Button>
              </Toolbar>
            </AppBar>
          {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
            <Switch>
              <ConvLimitProvider>
                <Route exact path="/" component={Dashboard} />
                <Route path="/summary" component={Summary} />
                <ScenariosContext.Provider value={scenariosState}>
                  <Route path="/simulation/:sid([0-9]+)" component={SimulationWindow} />
                </ScenariosContext.Provider>
                <Route path="/chartTest" exact component={RadarTest} />
              </ConvLimitProvider>
            </Switch>
          </ThemeProvider>
        </div>
      </Router>
    </div>
  );
}

export default Nav;
