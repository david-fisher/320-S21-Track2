import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Button, Box, Container } from '@material-ui/core';
import { Link as RouterLink } from 'react-router-dom';
import Copyright from '../components/Copyright';
import RedLogo from '../shared/RedLogo.png';

const useStyles = makeStyles((theme) => ({
    container: {
        marginTop: theme.spacing(2),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    logo: {
        width: '100px',
    },
    form: {
        marginTop: theme.spacing(1),
        width: '100%',
    },
    submit: {
        marginTop: theme.spacing(2),
        backgroundColor: theme.palette.primary.main,
        color: 'white',
    },
    copyright: {
        margin: theme.spacing(2),
        opacity: 0.5,
    },
}));

export default function ToSimulator() {
    const classes = useStyles();

    return (
        <Container component="main" maxWidth="xs">
            <div className={classes.container}>
                <img src={RedLogo} alt="EthismLogo" className={classes.logo} />
                <form className={classes.form}>
                    <Button
                        className={classes.submit}
                        component={RouterLink}
                        to={'/dashboard'}
                        type="submit"
                        fullWidth
                        variant="contained"
                    >
                        Editor
                    </Button>
                    <Button
                        className={classes.submit}
                        component={RouterLink}
                        to={'/dashboard'}
                        type="submit"
                        fullWidth
                        variant="contained"
                    >
                        Simulator
                    </Button>
                </form>
            </div>
            <Box className={classes.copyright}>
                <Copyright />
            </Box>
        </Container>
    );
}
