import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Container, Box, Typography, Grid } from '@material-ui/core';
import SimScenarioCard from './components/DashboardComponents/SimScenarioCard';
import Copyright from './components/Copyright';
import { BASE_URL, STUDENT_ID } from '../constants/config';

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

export default function Dashboard({setScenario}) {

    const classes = useStyles();

    const [openScenarios, setOpenScenarios] = useState(null);

    const [shouldFetch, setShouldFetch] = useState(0);

    // get all scenarios assigned to student with id parameter
    async function getScenarioData() {

        const response = await fetch(`${BASE_URL}/dashboard/?student_id=${STUDENT_ID}`, {
            "method": "GET",
        });
        
        const scenarios = await response.json();

        return scenarios;
    }

    // Retrieves all scenarios and creates their cards to be displayed into the dashboard
    useEffect(() => {
        getScenarioData().then(scenariosData => {
            const scenarios = scenariosData.slice();

            console.log(scenarios);
            
            let openScenariosCards = scenarios.map((scenario) => (
                <SimScenarioCard
                    key={scenario.scenario_id}
                    id={scenario.scenario_id}
                    name={scenario.name}
                    convLimit={scenario.num_conversation}
                />
            ));

            setOpenScenarios(openScenariosCards);
        })

    }, [shouldFetch]);

    return (
        <div>
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
                <div className={classes.border}>
                    <Typography variant="h3">Completed Scenarios</Typography>
                </div>
                <Grid
                    container
                    spacing={2}
                    direction="row"
                    justify="flex-start"
                    alignItems="stretch"
                >
                    {}
                </Grid>
                <Box className={classes.copyright}>
                    <Copyright />
                </Box>
            </Container>
        </div>
    );
}