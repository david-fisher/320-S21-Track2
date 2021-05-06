import React from "react";

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

import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import SimulationWindow from './pages/simulator_window';
import Dashboard from "./pages/sim_dashboard";
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
    textDecoration: "none",
    "&:hover": {
      color: "#000000"
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

  const handleLogout = () => {
    window.location.href = "https://ethisim2.cs.umass.edu/Shibboleth.sso/Logout?return=https://webauth.umass.edu/Logout";
  };

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
                <Button color="inherit" onClick={handleLogout}>LogOut</Button>
              </Toolbar>
            </AppBar>
          {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
            <Switch>
              <ConvLimitProvider>
                <Route exact path="/" component={Dashboard} />
                <ScenariosContext.Provider value={scenariosState}>
                  <Route path="/simulation/:sid([0-9]+)" component={SimulationWindow} />
                </ScenariosContext.Provider>
              </ConvLimitProvider>
            </Switch>
          </ThemeProvider>
        </div>
      </Router>
    </div>
  );
}

export default Nav;
