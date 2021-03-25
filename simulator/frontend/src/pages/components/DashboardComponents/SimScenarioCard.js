import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Link } from 'react-router-dom';
import { Typography, Grid, Card, CardContent, Button } from '@material-ui/core';
import PropTypes from 'prop-types';
import Tooltip from '@material-ui/core/Tooltip';

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
    description: PropTypes.string,
    due_date: PropTypes.string,
}

export default function SimScenarioCard({
    id,
    name,
    description,
    due_date,
    onClick,
}) {

    const classes = useStyles();

    const startButton = (
        <Tooltip title="Let's Begin!" arrow placement="bottom" classes={classes}>
        <Button
            className={classes.buttonText}
            variant="contained"
            color="primary"
            component={Link}
            to={{
                pathname: '/simulation',
            }}
            onClick={onClick(id)}
            className={classes.button}
            item
            fullWidth="true"
        >
            <Typography variant="subtitle1" noWrap>
                Start
            </Typography>
        </Button>
        </Tooltip>
    )

    const due = new Date(due_date).toString();

    return (
        <Grid key={id} item xs="auto">
            <Card>
                <CardContent className={classes.scenarioContainer}>
                    <Typography variant="h5" display="block" noWrap>
                        {name}
                    </Typography>
                    <Typography variant="h6" display="block" noWrap>
                        {description}
                    </Typography>
                    <Typography
                        variant="subtitle1"
                        color="textSecondary"
                        display="block"
                    >
                        Due: {due}
                    </Typography>
                    {startButton}
                </CardContent>
            </Card>
        </Grid>
    )
}