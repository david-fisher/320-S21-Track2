import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Container, Box, Typography, Grid, Divider } from '@material-ui/core';
import SimScenarioCard from './components/DashboardComponents/SimScenarioCard';
import Copyright from './components/Copyright';
import get from '../universalHTTPRequests/get';
import DashboardNavBar from './components/DashboardComponents/DashboardNavbar';

const useStyles = makeStyles((theme) => ({
    container: {
        marginTop: theme.spacing(11),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    copyright: {
        margin: theme.spacing(2),
    },
    issue: {
        marginTop: theme.spacing(10),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    errorContainer: {
        marginTop: theme.spacing(2),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    iconError: {
        paddingRight: theme.spacing(2),
        fontSize: '75px',
    },
    iconRefreshLarge: {
        fontSize: '75px',
    },
    iconRefreshSmall: {
        fontSize: '30px',
    },
    border: {
        borderStyle: 'none none solid none',
        marginBottom: theme.spacing(2),
    },
}));

//TODO when Shibboleth gets implemented
const endpointGet = '/scenarios/';
const endpointGetCourses = '/api/courses/';
const endpointPost = '/dashboard';
const endpointDelete = '/api/scenarios/';

const styles = (theme) => ({
    root: {
        margin: 1,
        padding: theme.spacing(2),
    },
    closeButton: {
        position: 'absolute',
        right: theme.spacing(1),
        top: theme.spacing(1),
        color: theme.palette.grey[500],
    },
});

export default function Dashboard({
    setScenario,
}) {
    const classes = useStyles();

    const [openScenarios, setOpenScenarios] = useState(null);
    const [fetchScenariosResponse, setFetchScenariosResponse] = useState({
        data: null,
        loading: false,
        error: null,
    });

    const [errorBannerMessage, setErrorBannerMessage] = useState('');
    const [errorBannerFade, setErrorBannerFade] = useState(false);

    const [shouldFetch, setShouldFetch] = useState(0);

    let getScenarios = () => {
        console.log("Getting Scenarios")
        function onSuccess(res) {
            const scenarios = res.data.slice();
            
            let openScenariosCards = scenarios.map((scenario) => (
                <SimScenarioCard
                    key={scenario.id}
                    id={scenario.id}
                    name={scenario.name}
                    description={scenario.description}
                    due_date={scenario.due_date}
                    onClick={setScenario}
                />
            ));

            setOpenScenarios(openScenariosCards);

            console.log(scenarios);
        }

        function onFailure() {
            //setErrorBannerMessage('Failed to get scenarios! Please try again.');
            //setErrorBannerFade(true);
        }
        get(setFetchScenariosResponse, endpointGet, onFailure, onSuccess);
    };

    useEffect(getScenarios, [shouldFetch])

    return (
        <div>
            <DashboardNavBar />
            <Container
                className={classes.container}
                component="main"
                maxWidth="lg"
            >
                <div className={classes.border}>
                    <Typography variant="h3">Open Scenarios</Typography>
                </div>
                <Grid
                    container
                    spacing={2}
                    direction="row"
                    justify="flex-start"
                    alignItems="stretch"
                >
                    {openScenarios}
                </Grid>
                <Box className={classes.copyright}>
                    <Copyright />
                </Box>
            </Container>
        </div>
    );
}