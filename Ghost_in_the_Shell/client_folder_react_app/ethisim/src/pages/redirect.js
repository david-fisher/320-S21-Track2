import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Button, Box, Container, Typography } from '@material-ui/core';
import { Link as RouterLink } from 'react-router-dom';
import Copyright from '../components/Copyright';
import RedLogo from '../shared/RedLogo.png';
import LoadingSpinner from '../components/LoadingSpinner';

const useStyles = makeStyles((theme) => ({
    container: {
        marginTop: theme.spacing(10),
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

export default function RedirectPage() {
    const classes = useStyles();

    const [didGetLoginInfo, setDidGetLoginInfo] = useState(false);

    const [loginInfo, setLoginInfo] = useState([]);
    const [isLoading, setLoading] = useState(false);
    var axios = require('axios');

    const [errorMessage, setErrorMessage] = useState('');
    const [showError, setShowError] = useState(false);

    function getLoginData() {
        setLoading(true);

        /*var data = { SCENARIO: { scenario } };
        var config = {
            method: 'get',
            url: baseURL + '/api/stakeholders/?SCENARIO=' + 1,
            headers: {
                'Content-Type': 'application/json',
            },
            data: data,
        };

        axios(config)
            .then(function (response) {
                setLoginInfo(response.data);
            })
            .catch(function (error) {
                setErrorMessage(
                    'Failed to get login information! Please return to the homepage and try again.'
                );
                setShowError(true);
            }); */

        setTimeout(function () {
            setLoading(false);
        }, 2000);
        //setLoading(false);
    }

    if (isLoading) {
        return <LoadingSpinner />;
    }

    if (!didGetLoginInfo) {
        setDidGetLoginInfo(true);
        getLoginData();
    }

    if (showError) {
        return (
            <Container component="main" maxWidth="xs">
                <div className={classes.container}>
                    <img
                        src={RedLogo}
                        alt="EthismLogo"
                        className={classes.logo}
                    />
                    <form className={classes.form}>
                        <Button
                            className={classes.submit}
                            component={RouterLink}
                            to={'/home'}
                            type="submit"
                            fullWidth
                            variant="contained"
                            align="center"
                        >
                            {errorMessage}
                        </Button>
                    </form>
                </div>
                <Box className={classes.copyright}>
                    <Copyright />
                </Box>
                <form className={classes.form}>
                    <Typography align="center" variant="h6"></Typography>
                </form>
            </Container>
        );
    }

    if (!showError) {
        return (
            <Container component="main" maxWidth="xs">
                <div className={classes.container}>
                    <img
                        src={RedLogo}
                        alt="EthismLogo"
                        className={classes.logo}
                    />
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
                            to={'/toSimulator'}
                            type="submit"
                            fullWidth
                            variant="contained"
                        >
                            Simulator
                        </Button>
                        <Button
                            className={classes.submit}
                            component={RouterLink}
                            to={'/home'}
                            type="submit"
                            fullWidth
                            variant="contained"
                        >
                            Return to the Homepage
                        </Button>
                    </form>
                </div>
                <Box className={classes.copyright}>
                    <Copyright />
                </Box>
            </Container>
        );
    }
}
