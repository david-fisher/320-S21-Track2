import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Link } from 'react-router-dom';
import { Typography, Grid, Card, CardContent, Button } from '@material-ui/core';
import PropTypes from 'prop-types';
import Tooltip from '@material-ui/core/Tooltip';
import { ConvLimitConsumer } from '../../context/ConvContext';

const useStyles = makeStyles((theme) => ({
    scenarioContainer: {
        minHeight: '100px',
        minWidth: '200px',
        backgroundColor: "#F7E7E7",
        borderStyle: 'solid',
        borderColor: theme.palette.primary.light,
        border: 2,
        maxWidth: '400px',
    },
    buttonContainer: {
        borderStyle: 'solid',
        borderColor: theme.palette.primary.light,
        border: 3,
    },
    button: {
        borderStyle: 'solid',
        borderColor: theme.palette.primary.light,
        border: 3,
        top: 5,
    },
    buttonText: {
        width: '100%',
        textTransform: 'unset',
    },
    arrow: {
        color: "#881c1c", 
      },
      tooltip: {
        backgroundColor: "#881c1c",
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

SimScenarioCard.propTypes = {
    id: PropTypes.number,
    name: PropTypes.string,
    convLimit: PropTypes.number,
}

export default function SimScenarioCard({
    id,
    name,
    convLimit,
}) {

    const classes = useStyles();

    // to={http://localhost:8000/simulation/:sid}, where sid is the scenario id
    const startButton = (
        <Link to={`/simulation/${id}`}>
            <Tooltip title="Let's Begin!" arrow placement="bottom" classes={classes}>
                <ConvLimitConsumer>
                    {(context) => 
                        <Button
                            className={classes.buttonText}
                            variant="contained"
                            color="primary"
                            className={classes.button}
                            item
                            fullWidth="true"
                            onClick={() => {context.update(convLimit)}}
                        >
                            <Typography variant="subtitle1" noWrap>
                                Start
                            </Typography>
                        </Button>
                    }
                </ConvLimitConsumer>
            </Tooltip>
        </Link>
    )

    return (
        <Grid key={id} item xs="auto">
            <Card>
                <CardContent className={classes.scenarioContainer}>
                    <Typography variant="h5" display="block" noWrap>
                        {name}
                    </Typography>
                    <nav>
                        {startButton}
                    </nav>
                </CardContent>
            </Card>
        </Grid>
    )
}