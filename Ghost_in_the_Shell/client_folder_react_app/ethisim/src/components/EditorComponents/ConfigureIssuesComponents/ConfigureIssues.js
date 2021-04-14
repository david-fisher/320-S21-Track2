import React, { useState, useEffect } from 'react';
import {
    Typography,
    Button,
    Grid,
    TextField,
    MenuItem,
    Dialog,
    DialogTitle,
    DialogContent,
    DialogContentText,
    DialogActions,
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import EntryFields from './IssueEntryFieldList';
import get from '../../../universalHTTPRequests/get';
import LoadingSpinner from '../../LoadingSpinner';
import RefreshIcon from '@material-ui/icons/Refresh';
import ErrorIcon from '@material-ui/icons/Error';
import PropTypes from 'prop-types';
import IssueMatrix from './IssueCoverageMatrix';
import MaterialTable from 'material-table';
var axios = require('axios');

//Need scenarioID
const endpointGET = '/api/issues/?SCENARIO=';
const baseURL = 'http://127.0.0.1:8000';

const useStyles = makeStyles((theme) => ({
    issue: {
        marginTop: theme.spacing(2),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    spacing: {
        padding: theme.spacing(1),
    },
    saveButton: {
        margin: theme.spacing(2),
        float: 'right',
        textTransform: 'unset',
    },
    container: {
        padding: theme.spacing(1),
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
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
}));

ConfigureIssues.propTypes = {
    scenario_ID: PropTypes.number,
};
let values = {};

export default function ConfigureIssues({ scenario_ID }) {
    const addStakeHolders = () => {
        // if (!checkTime(setCurrentTime, currentTime)) {
        //     return;
        // }
        // setLoading(true);

        var data = JSON.stringify({
            SCENARIO: scenario_ID,
        });

        var config = {
            method: 'post',
            url: baseURL + '/stakeholder',
            headers: {
                'Content-Type': 'application/json',
            },
            data: data,
        };
        axios(config)
            .then(function (response) {
                //console.log(values)
                response.data['NAME'] = values['NAME'];
                response.data['DESCRIPTION'] = values['DESCRIPTION'];
                response.data['INTRODUCTION'] = values['INTRODUCTION'];
                response.data['JOB'] = values['JOB'];
                saveStakeHolders(response.data);
                // setStakeHolders([...stakeHolders, response.data]);
                // setSuccessBannerMessage(
                //     'Successfully created a new stakeholder!'
                // );
                //setSuccessBannerFade(true);
            })
            .catch(function (error) {
                // setErrorBannerMessage(
                //     'Failed to create a stakeholder! Please try again.'
                // );
                // setErrorBannerFade(true);
            });
    };
    const saveStakeHolders = (data) => {
        //var data = [...values]

        var config = {
            method: 'put',
            url: baseURL + '/multi_stake?SCENARIO=' + scenario_ID,
            headers: {
                'Content-Type': 'application/json',
            },
            data: [data],
        };

        axios(config)
            .then(function (response) {
                getData();
                // setSuccessBannerMessage('Successfully saved the stakeholders!');
                // setSuccessBannerFade(true);
            })
            .catch(function (error) {
                // setErrorBannerMessage(
                //     'Failed to save the stakeholders! Please try again.'
                // );
                // setErrorBannerFade(true);
            });
    };

    const [open, setOpen] = React.useState(false);
    const [open2, setOpen2] = React.useState(false);
    const handleClickOpen = () => {
        setOpen(true);
    };
    const handleClose = () => {
        addStakeHolders();
        setOpen(false);
    };
    const handleClickOpen2 = () => {
        setOpen2(true);
    };
    const handleClose2 =()=>{
        console.log(issueValues)
        // issueEntryFieldList =[issueValues]
        // setIssueEntryFieldList={setIssueEntryFieldList}
        //scenarioID={scenario_ID}
        getData()
        setOpen2(false);
    }

    const classes = useStyles();
    const [issueEntryFieldList, setIssueEntryFieldList] = useState({
        data: null,
        loading: true,
        error: null,
    });
    const [issueCoverageMatrix, setIssueCoverageMatrix] = useState({
        data: null,
        loading: true,
        error: null,
    });

    let getData = () => {
        get(setIssueEntryFieldList, endpointGET + scenario_ID);
        get(setIssueCoverageMatrix, endpointGET + scenario_ID);
    };

    useEffect(getData, []);

    if (issueEntryFieldList.loading || issueCoverageMatrix.loading) {
        return <LoadingSpinner />;
    }

    if (issueEntryFieldList.error) {
        return (
            <div className={classes.issue}>
                <div className={classes.container}>
                    <ErrorIcon className={classes.iconError} />
                    <Typography align="center" variant="h3">
                        Error in fetching issues.
                    </Typography>
                </div>
                <Button variant="contained" color="primary" onClick={getData}>
                    <RefreshIcon className={classes.iconRefreshLarge} />
                </Button>
            </div>
        );
    }

    /* <EntryFields
            issueEntryFieldList={
                issueEntryFieldList !== null ? issueEntryFieldList : []
            }
            setIssueEntryFieldList={setIssueEntryFieldList}
            scenarioID={scenario_ID}
    />*/

    /*return (
        <div className={classes.issue}>
            <Typography align="center" variant="h2">
                Configure Ethical Issues
            </Typography>
            <div className={classes.spacing}>
                <Button variant="contained" color="primary" onClick={getData}>
                    <RefreshIcon className={classes.iconRefreshSmall} />
                </Button>
            </div>
            <MaterialTable>
                issueCoverageMatrix = {issueCoverageMatrix}
                setIssueCoverageMatrix = {setissueCoverageMatrix}
            </MaterialTable>
        </div>
    );*/
    //for info button
    let issueValues = {}
    let values = {
        STAKEHOLDER: 1,
        NAME: '',
        DESCRIPTION: '',
        INTRODUCTION: '',
        SCENARIO: scenario_ID,
        VERSION: 1,
        JOB: '',
    };
    const getName = (e) => {
        values['NAME'] = e.target.value;
    };
    const getDes = (e) => {
        values['DESCRIPTION'] = e.target.value;
    };
    const getIntro = (e) => {
        values['INTRODUCTION'] = e.target.value;
    };
    const getJob = (e) => {
        values['JOB'] = e.target.value;
    };
    const getIssueName = (e)=>{issueValues['NAME']=e.target.value;}
    const getImportance =(e)=>{issueValues['IMPORTANCE_SCORE']=e.target.value;}

    return (
        <div className={classes.issue}>
            <Typography align="center" variant="h2">
                Configure Ethical Issues
            </Typography>

            <div className={classes.spacing}>
                <Button variant="contained" color="primary" onClick={getData}>
                    <RefreshIcon className={classes.iconRefreshSmall} />
                </Button>
            </div>

            <EntryFields
                issueEntryFieldList={
                    issueEntryFieldList !== null ? issueEntryFieldList : []
                }
                setIssueEntryFieldList={setIssueEntryFieldList}
                scenarioID={scenario_ID}
            />
              <Button
                className={classes.button}
                id="button"
                onClick={handleClickOpen2}
                variant="contained"
                color="primary"
            >
                {' '}
                Add Issues
            </Button>

            <Dialog
                open={open2}
                onClose={handleClose2}
                aria-labelledby=""
                aria-describedby=""
            >
                <DialogTitle id="Add stakeholder">
                    {'Add Stakeholder'}
                </DialogTitle>
                <Grid container direction="row" justify="centre">
                    <Grid item xs={8}>
                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Issue Name"
                            label="Issue Name"
                            id="scenariopageAdder"
                            onChange={(e) => getIssueName(e)}
                        ></TextField>

                        
                         <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Importance Factor"
                            label="Importance Factor"
                            id="scenariopageAdder"
                            onChange={(e) => getImportance(e)}
                        ></TextField>
                    </Grid>
                </Grid>
                <DialogActions>
                    <Button onClick={handleClose2} color="primary">
                        Add
                    </Button>
                </DialogActions>
            </Dialog>

            <Button
                className={classes.button}
                id="button"
                onClick={handleClickOpen}
                variant="contained"
                color="primary"
            >
                {' '}
                Add Stakeholders
            </Button>
            
            <Dialog
                open={open}
                onClose={handleClose}
                aria-labelledby=""
                aria-describedby=""
            >
                <DialogTitle id="Add stakeholder">
                    {'Add Stakeholder'}
                </DialogTitle>
                <Grid container direction="row" justify="centre">
                    <Grid item xs={8}>
                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="StakeHolder name"
                            label="Stakeholder name"
                            id="scenariopageAdder"
                            onChange={(e) => getName(e)}
                        ></TextField>

                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Job"
                            label="Job"
                            id="scenariopageAdder"
                            onChange={(e) => getJob(e)}
                        ></TextField>

                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Description"
                            label="Description"
                            id="scenariopageAdder"
                            onChange={(e) => getDes(e)}
                        ></TextField>
                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Bio"
                            label="Bio"
                            id="scenariopageAdder"
                            onChange={(e) => getIntro(e)}
                        ></TextField>
                    </Grid>
                </Grid>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                        Add
                    </Button>
                </DialogActions>
            </Dialog>

            <IssueMatrix /*this might need to be edited, sends scenario id to IssueCoverageMatrix*/
                scenario={scenario_ID}
            />
        </div>
    );
}


